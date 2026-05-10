# Guia de Reescrita do TCC-RELATORIO

Este guia define como reescrever o `TCC-RELATORIO` a partir do estado atual do projeto técnico em `../TCC-wsl`.

A regra principal é: `TCC-wsl` é a fonte técnica atual; `TCC-RELATORIO` ainda contém texto de fases anteriores. A reescrita deve preservar a motivação do problema de previsão de PM2.5, mas reconstruir escopo, método, resultados e conclusão a partir dos artefatos atuais e comparáveis.

## 0. Estado Atual Consolidado - Não Esquecer na Reescrita

Esta seção tem prioridade sobre textos antigos do relatório. O projeto evoluiu depois do benchmark inicial Sapo 2016-2020 com KNN e sem HPO. O TCC deve deixar essa evolução clara: houve um benchmark fixo inicial, depois uma rodada com HPO simples em 2026-05-09, e o melhor resultado atual vem da suite de 2026-05-10 com contrato `clean_pm10_decoder_proxy`, HPO walk-forward e multi-seed.

### Vencedores Atuais

| Pergunta | Resposta atual |
| --- | --- |
| Melhor modelo por MAE no seed canônico | `cv_hpo_lstm_direct_clean_pm10` |
| Melhor modelo por MAE médio multi-seed | `cv_hpo_lstm_direct_clean_pm10` |
| Melhor RMSE/R2 médio multi-seed | `cv_hpo_lstm_recursive_clean_pm10`, com viés positivo |
| Melhor baseline tabular final | `cv_hpo_xgboost_clean_pm10` |
| Melhor Seq2Seq attention final | `cv_hpo_weighted_l1_clean_pm10` |
| Melhor variante para picos/cauda, não MAE global | LSTM recursiva e Seq2Seq weighted L1 |

Números principais atuais no dataset `clean_pm10_decoder_proxy`:

| Modelo/variante | MAE | RMSE | R2 | MAPE | Peak35 MAE | p99 previsto | Observação |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `cv_hpo_lstm_direct_clean_pm10` | 2.7713 | 3.8346 | 0.5154 | 23.01 | 13.6112 | 28.57 | Vencedor por MAE no seed canônico. |
| `cv_hpo_weighted_l1_clean_pm10` | 2.8658 | 3.9641 | 0.4821 | 23.90 | 12.3697 | 31.57 | Melhor Seq2Seq final; melhora cauda, não vence MAE. |
| `cv_hpo_xgboost_clean_pm10` | 2.8786 | 3.9793 | 0.4781 | 23.80 | 12.2583 | 30.73 | Baseline tabular forte; melhor H1. |
| `cv_hpo_lstm_recursive_clean_pm10` | 2.8876 | 3.8380 | 0.5146 | 24.39 | 12.0392 | 30.49 | Bom em RMSE/R2 e picos, mas com MAE e viés piores. |

Leitura obrigatória dos plots contra métricas:

- MAE, RMSE e R2 elegem o `lstm_direct_clean_pm10_hpo` como vencedor global.
- Nos plots, `lstm_direct` e XGBoost tendem a prever uma curva mais suave e próxima da média. Isso ajuda o erro médio, mas reduz amplitude e subestima muitos picos.
- O Seq2Seq attention com `weighted_l1` não vence o LSTM direct em MAE, mas mostra comportamento visual mais dinâmico, com maior amplitude, p99 mais próximo do observado e menor erro em eventos altos.
- Portanto, a discussão não deve dizer simplesmente "o Seq2Seq é pior". A formulação correta é: o LSTM direct venceu em erro médio; o Seq2Seq weighted L1 ficou competitivo e capturou melhor parte da dinâmica de cauda/picos, sugerindo trade-off entre suavização e resposta a eventos.
- Não escolher o vencedor apenas pelo plot. Também não ignorar o plot só porque o MAE favorece modelos mais suaves.

### Contrato Atual Que Deve Ser Descrito

O contrato atual mais importante é `clean_pm10_decoder_proxy`:

- estação `Sapo` / CMD;
- previsão horária de `PM2.5`;
- tarefa `48 -> 24`;
- split cronológico `70/15/15`;
- dataset final nos artefatos: `2017-01-04 00:30:00` a `2020-12-31 22:30:00`, com 34.991 linhas;
- imputação linear no dataset limpo atual;
- alvo imputado fica fora de loss e métricas quando a máscara de observado está disponível;
- variáveis principais: `PM2.5`, `PM10`, flags `PM2.5__miss` e `PM10__miss`, atributos temporais/Fourier e proxies causais de PM10;
- `PM10_proxy_exante = PM10(t-24)`;
- `PM10_trend_exante = PM10(t-24) - PM10(t-27)`;
- no decoder, somente features conhecidas causalmente: tempo/Fourier, `PM10_proxy_exante` e `PM10_trend_exante`;
- variáveis meteorológicas/gases muito esparsas em Sapo foram removidas do melhor contrato; reintroduzi-las só como nova ablação.

### O Que Já Foi Testado

Não reescrever como se as escolhas atuais tivessem surgido direto. O TCC pode resumir os testes assim:

| Tema testado | Resultado prático |
| --- | --- |
| Benchmark inicial Sapo 70/15/15, KNN, sem HPO | Serviu como benchmark fixo inicial; nele o XGBoost era o vencedor. Não é mais o melhor resultado atual. |
| Linear vs KNN e preocupação com alvo imputado | O contrato atual usa linear e exclui alvo imputado da loss/métricas, evitando medir "verdade" que na verdade era imputada. |
| Remoção de variáveis esparsas | Melhorou a coerência do dataset Sapo; foco atual é PM2.5, PM10, missing flags e tempo. |
| PM10 como proxy causal no decoder | Foi uma das escolhas mais importantes: PM10 t-24 e tendência ex-ante ajudam sem vazamento. |
| HPO em DL e XGBoost | Mudou a conclusão: LSTM direct passou a ser vencedor global; XGBoost permaneceu forte; Seq2Seq attention melhorou, mas não venceu globalmente. |
| Seq2Seq attention canônico e variações | A atenção simples ficou quase uniforme e pouco informativa; várias mudanças não deram ganho determinístico. |
| Luong dot/general/local, multi-head temporal, gates sigmoid, atenção por grupos, query condicionada por horizonte/futuro, DA-RNN e guided attention | Úteis como ablações, mas nenhuma superou de forma estável o ganho obtido por contrato de dados, PM10 causal e loss adequada. |
| `weighted_l1` e perdas voltadas a picos | Melhoraram cauda/picos e tornaram o Seq2Seq mais competitivo; não são regularização L1 clássica, são função de perda ponderada por regime/erro. |
| Lags explícitos de PM2.5/PM10 | Parcialmente redundantes com a sequência do encoder; `lag24` como baseline residual ajudou picos, mas não melhorou o MAE global. |
| Horizonte 12h vs 24h | 12h melhora métricas por ser tarefa mais curta; não comparar como se fosse o mesmo problema. |
| Diário vs horário | Agregado diário muda a pergunta; o TCC final deve preservar previsão horária se o objetivo é curto prazo `48 -> 24`. |
| Outras estações, como Barra Longa e Rio Doce | Estudos auxiliares de generalização/dados; não substituir Sapo como eixo principal sem nova tabela final consolidada. |

### Como Tratar a Ablação Automática Antiga

O TCC não deve apresentar o script antigo de ablação automática como a metodologia oficial final nem usar seus resultados como evidência quantitativa principal. Esse script foi útil para organizar a fase inicial do projeto, mas algumas rodadas antigas tiveram bugs ou ficaram desatualizadas em relação ao contrato atual. Portanto, ele deve ser tratado como histórico de exploração, não como fonte de conclusão.

Formulação recomendada:

> Foram realizadas rodadas exploratórias iniciais de ablação para orientar hipóteses de modelagem. Entretanto, os resultados finais reportados neste trabalho consideram apenas os experimentos consolidados e reexecutados sob o contrato final, com artefatos rastreáveis, mesmo split temporal, mesmo conjunto de variáveis e avaliação no holdout de teste.

Regras para a escrita:

- não usar tabelas, métricas ou vencedores vindos do script antigo se houver suspeita de bug ou inconsistência;
- não reconstruir a narrativa como se um único pipeline sequencial tivesse escolhido todas as decisões finais;
- não gastar espaço tentando defender o script antigo como contribuição central;
- mencionar a ablação automática antiga apenas como fase exploratória, sem números principais;
- basear as conclusões nos artefatos recentes e rastreáveis de 2026-05-09;
- se algum resultado antigo for citado, ele deve ser claramente rotulado como exploratório e não comparável ao benchmark final.

A metodologia oficial deve ser o protocolo final consolidado:

1. dataset `clean_pm10_decoder_proxy`;
2. tarefa horária `48 -> 24`;
3. split cronológico `70/15/15`;
4. alvo imputado excluído de loss e métricas observadas;
5. PM10 causal no decoder por `PM10_proxy_exante` e `PM10_trend_exante`;
6. comparação entre LSTM direct, LSTM recursive, Seq2Seq basic, Seq2Seq attention e XGBoost;
7. HPO documentado para os modelos principais;
8. avaliação por erro médio, horizonte, picos/cauda e inspeção visual.

O HPO atual deve ser descrito como **controlado e suficiente para comparação experimental de TCC**, não como busca exaustiva ou garantia de ótimo global. Já houve HPO para os modelos principais no contrato atual (`lstm_direct`, `lstm_recursive`, `seq2seq_basic`, `seq2seq_attention` e XGBoost), mas o texto deve reconhecer que a busca teve orçamento limitado. Se houver tempo para uma rodada final adicional, a prioridade não é corrigir o script antigo inteiro; é rodar uma bateria pequena, limpa e comparável com o contrato final, idealmente incluindo multi-seed para os dois ou três modelos mais relevantes.

## 1. Escopo Atual do Projeto

O TCC final deve ser apresentado como um estudo experimental de previsão horária de PM2.5 para a estação `Sapo`, no conjunto CMD, com protocolo comparável de modelos e ablações controladas. O benchmark antigo Sapo 2016-2020 sem HPO deve aparecer como etapa histórica; o resultado final consolidado deve usar o contrato `clean_pm10_decoder_proxy` com HPO.

Escopo oficial:

| Item | Definição final |
| --- | --- |
| Poluente-alvo | `PM2.5` horário |
| Estação principal | `Sapo` / CMD |
| Período do artefato atual | `2017-01-04 00:30:00` a `2020-12-31 22:30:00` |
| Tarefa | usar 48 horas passadas para prever as próximas 24 horas (`48 -> 24`) |
| Split | cronológico por proporção `70/15/15` |
| Treino | primeiros 70% do período filtrado |
| Validação | 15% seguintes |
| Teste | 15% finais |
| Imputação do contrato atual | `linear`, com alvo imputado excluído de loss/métricas observadas |
| Feature set principal | `clean_pm10_decoder_proxy` |
| Modelos DL principais | `lstm_recursive`, `lstm_direct`, `seq2seq_basic`, `seq2seq_attention` |
| Baseline tabular | XGBoost `multi_output_tree` |
| Busca de hiperparâmetros no resultado atual | ativada para DL e XGBoost |
| Seleção de checkpoint | validação, preferencialmente `val/mae` ou métrica explicitamente justificada |
| Avaliação final | métricas no holdout de teste |
| Vencedor global atual | `lstm_direct_clean_pm10_hpo` |
| Melhor Seq2Seq attention atual | `weighted_l1_hpo_mae` |

O escopo principal **não é mais Cascata/Piratininga**. Essas estações aparecem apenas em experimentos históricos ou auxiliares de desenvolvimento do Seq2Seq. Elas não devem ser descritas como o objeto central do TCC final.

## 2. Diagnóstico do Relatório Atual

A reescrita ainda deve ser grande.

O texto atual mistura várias fases do projeto: Ibirité/Cascata/Piratininga, horizonte de 12 horas, narrativa M0-M4, SAITS, notebooks antigos, scheduled sampling como conclusão central e resultados que não pertencem ao benchmark Sapo 70/15/15.

Esses elementos devem ser removidos do núcleo do relatório ou rebaixados a histórico, quando forem úteis para explicar a evolução do projeto. O relatório final precisa contar uma história única:

1. existe um problema de previsão horária de PM2.5 em dados ambientais reais;
2. o trabalho fixa um protocolo temporal comparável para a estação Sapo;
3. diferentes famílias de modelos são avaliadas sob o mesmo contrato de dados;
4. ablações metodológicas explicam decisões de imputação, features, treino e desenho do Seq2Seq;
5. os resultados são discutidos com honestidade, separando o vencedor global por erro médio, o baseline tabular forte e o comportamento em picos/cauda.

## 3. Fontes de Verdade

Use estes arquivos antes de escrever qualquer capítulo técnico:

| Fonte | Uso |
| --- | --- |
| `../TCC-wsl/AGENTS.md` | Memória técnica consolidada do projeto, incluindo o contrato `clean_pm10_decoder_proxy` e vencedores atuais. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/cv_hpo_summary.csv` | Tabela principal atual com HPO walk-forward. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/multi_seed_aggregate.csv` | Estabilidade multi-seed dos modelos selecionados. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/naive_baselines.csv` | Baselines ingênuos. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/pm10_causal_ablation.csv` | Ablação PM10 causal. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/mask_imputation_ablation.csv` | Ablação máscara/imputação. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_hpo_vs_reference.csv` | Tabela histórica com HPO simples; não usar como resultado final se conflitar com 2026-05-10. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/datasets/sapo_clean_pm10_decoder_proxy.parquet` | Dataset final do contrato `clean_pm10_decoder_proxy`. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_dataset_summary.json` | Resumo do dataset atual, incluindo período, linhas e missingness. |
| `../TCC-wsl/docs/generated/eda_outras_usinas/dashboard` | EDA comparativa de outras estações/usinas usada para fundamentar a escolha de Sapo. |
| `../TCC-wsl/docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv` | Ranking preliminar de estações por PM2.5, PM10, cobertura, picos e continuidade. |
| `../TCC-wsl/runtime/reports/seq2seq_weighted_l1_hpo_20260509/seq2seq_weighted_l1_hpo_summary.csv` | HPO específico do Seq2Seq attention com `weighted_l1`; melhor Seq2Seq individual. |
| `../TCC-wsl/runtime/reports/seq2seq_weighted_l1_final_ablation_20260509/seq2seq_weighted_l1_final_ablation_summary.csv` | Ablações finais de seed, lag24/lag48, blends e HPO refinado para explicar comportamento de pico/cauda. |
| `../TCC-wsl/scripts/analysis/run_seq2seq_weighted_l1_final_ablation.py` | Script reprodutível da última bateria de ablação do Seq2Seq weighted L1. |
| `../TCC-wsl/configs/ablation_new/step3_architectures_sapo_70_15_15.yaml` | Configuração central do benchmark Sapo 70/15/15, 4 DL + XGB. |
| `../TCC-wsl/configs/data_source/cmd_sapo.yaml` | Fonte de dados e estação Sapo. |
| `../TCC-wsl/configs/period/cmd_sapo_2016_2020_ratio_70_15_15.yaml` | Período usado no benchmark fixo inicial; conferir contra o artefato atual antes de escrever. |
| `../TCC-wsl/configs/experiment/seq_len_48x24_cmd_sapo_70_15_15.yaml` | Formulação `48 -> 24`. |
| `../TCC-wsl/configs/feature_set/lag_cmd_sapo_ratio_70_15_15.yaml` | Feature set do benchmark fixo inicial; o contrato atual consolidado é `clean_pm10_decoder_proxy`. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.csv` | Benchmark fixo inicial Sapo 70/15/15 sem HPO; usar como histórico, não como resultado final mais forte. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.md` | Resumo legível do benchmark fixo inicial. |
| `../TCC-wsl/src/data/imputation.py` | Evidência de imputação fitada no treino e aplicada ao restante. |
| `../TCC-wsl/src/data/processing.py` | Split temporal, feature engineering e janelas. |
| `../TCC-wsl/src/data/datasets.py` | Construção de janelas, máscaras e alvo observado. |
| `../TCC-wsl/src/training/trainer.py` | Treino final, normalização, monitor de validação e teste final. |
| `../TCC-wsl/pipelines/tasks/model_tasks.py` | Contrato do XGBoost multi-output. |
| `../TCC-wsl/runtime/reports/seq2seq_improvement_suite_2026_04_21/` | Ablações auxiliares do Seq2Seq em Cascata. Usar apenas como estudo auxiliar. |
| `../TCC-wsl/runtime/reports/seq2seq_open_hypotheses_2026_04_21/` | Ablações auxiliares: semi-direct, recency, loss de picos, input feeding. |
| `../TCC-wsl/runtime/reports/teacher_forcing_paper_ablation/` | Ablação auxiliar de teacher forcing / scheduled sampling. |
| `referencias_fundamentais/REFERENCIAS_FUNDAMENTAIS.md` | Curadoria bibliográfica inicial. |
| `referencias.bib` | Base BibTeX do relatório. |

Não use valores de notebooks antigos, prints soltos ou runs sem config rastreável como resultado final. Se houver conflito entre a tabela antiga em `results/reports/` e os artefatos de `runtime/reports/*20260509/`, os artefatos de 2026-05-09 representam o estado experimental mais recente.

## 4. Resultado Principal Atual

A tabela principal do TCC deve partir do contrato `clean_pm10_decoder_proxy` com HPO. O benchmark Sapo 70/15/15 antigo, com KNN e sem HPO, pode aparecer como etapa anterior para mostrar a evolução metodológica, mas não deve ser usado para declarar o vencedor final.

| Modelo | MAE | RMSE | MAPE | R2 | H1 MAE | H24 MAE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `cv_hpo_lstm_direct_clean_pm10` | 2.7713 | 3.8346 | 23.01 | 0.5154 | 2.6725 | 2.8670 |
| `cv_hpo_weighted_l1_clean_pm10` | 2.8658 | 3.9641 | 23.90 | 0.4821 | 2.7631 | 2.9695 |
| `cv_hpo_xgboost_clean_pm10` | 2.8786 | 3.9793 | 23.80 | 0.4781 | 2.5618 | 3.0273 |
| `cv_hpo_lstm_recursive_clean_pm10` | 2.8876 | 3.8380 | 24.39 | 0.5146 | 2.7380 | 3.1492 |

Esses valores devem ser conferidos diretamente no CSV oficial no momento da escrita final. A interpretação esperada é:

- `cv_hpo_lstm_direct_clean_pm10` é o vencedor atual por MAE no seed canônico e na média multi-seed;
- XGBoost continua sendo baseline tabular forte, mas o HPO walk-forward final dele teve apenas quatro trials completos;
- `cv_hpo_weighted_l1_clean_pm10` fica competitivo e melhora amplitude/picos, mas abaixo da LSTM direta em MAE;
- `cv_hpo_lstm_recursive_clean_pm10` tem comportamento interessante em RMSE/R2 e picos, mas perde em MAE e apresenta viés positivo;
- a comparação atual inclui HPO walk-forward, multi-seed, baselines ingênuos e ablações de PM10/máscara; não misturar com o benchmark fixo sem HPO como se o orçamento experimental fosse igual.

### 4.1 Resultado Específico do Seq2Seq Attention

Além da tabela principal, o TCC deve registrar que a melhor versão individual do Seq2Seq attention foi obtida com `weighted_l1_hpo_mae`:

| Variante Seq2Seq | MAE | RMSE | R2 | Peak35 MAE | p99 previsto | Interpretação |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `cv_hpo_weighted_l1_clean_pm10` seed 42 | 2.8658 | 3.9641 | 0.4821 | 12.3697 | 31.57 | Resultado final selecionado por walk-forward. |
| `cv_hpo_weighted_l1_clean_pm10` média multi-seed | 2.8646 | 3.9617 | 0.4827 | 13.1103 | 30.49 | Competitivo, mas não supera LSTM direct em MAE. |

O resultado por sementes do `weighted_l1` deve ser tratado com cuidado: média de MAE `2.8646` e desvio `0.0201`. Isso é competitivo, mas não é uma vitória sobre a LSTM direta.

## 5. Eixos Experimentais do TCC

O relatório deve separar claramente três níveis de evidência.

### 5.1 Núcleo Principal

Este é o eixo obrigatório do TCC:

1. estação Sapo;
2. dataset limpo `clean_pm10_decoder_proxy`, com artefato atual de 2017-2020;
3. tarefa `48 -> 24`;
4. split cronológico `70/15/15`;
5. imputação linear com máscara de alvo observado;
6. features enxutas com PM2.5, PM10, missingness, tempo/Fourier, `PM10_proxy_exante` e `PM10_trend_exante`;
7. comparação `4DL + XGB` com HPO;
8. avaliação por MAE, RMSE, MAPE, R2 e métricas por horizonte.

Esse eixo deve ocupar o Capítulo 4 e a parte principal do Capítulo 5.

### 5.2 Ablations Metodológicas

Estas ablações explicam decisões de projeto, mas nem todas são resultado final direto em Sapo:

| Eixo | Como tratar |
| --- | --- |
| Imputação | Discutir `linear`, `knn`, `iterative_rf`; no contrato atual, usar `linear` e excluir alvo imputado da loss/métricas observadas. |
| Dados faltantes no alvo | Explicar que validar/testar contra valor imputado distorce métrica; por isso a máscara de observado é parte do protocolo. |
| Feature set / physics | Não chamar de impacto isolado de física se o conjunto altera também lags, tempo, proxies e colunas. |
| PM10 causal no decoder | Tratar como decisão central: `PM10(t-24)` e tendência `PM10(t-24)-PM10(t-27)` ajudam sem vazamento. |
| Delta/residual learning | Pode entrar como decisão metodológica se houver artefato oficial comparável. |
| Log target / loss / weighted L1 | Tratar como ablação de função objetivo. `weighted_l1` melhorou Seq2Seq e picos, mas muda o objetivo. |
| Stride / orçamento de treino | Discutir como engenharia experimental se for usado para justificar custo e redundância de janelas. |
| HPO | Explicar que a conclusão atual vem de HPO para DL e XGBoost; não comparar com runs sem HPO como se fossem equivalentes. |

Se uma ablação não foi rerodada no contrato `clean_pm10_decoder_proxy`, ela deve ser escrita como estudo auxiliar, não como conclusão final do benchmark.

### 5.3 Ablations Internas do Seq2Seq

Estas ablações são importantes para explicar o desenvolvimento do modelo. Algumas já foram rerodadas no contrato Sapo atual; outras pertencem a escopos auxiliares, principalmente Cascata ou Cascata/Piratininga. Só misturar numericamente com a tabela principal quando estação, período, split, features, imputação, horizonte e orçamento forem comparáveis.

| Tema | Evidência atual | Interpretação correta |
| --- | --- | --- |
| Seq2Seq attention HPO no contrato atual | `sapo_clean_pm10_hpo_all_models_20260509` | Melhorou o Seq2Seq attention, mas não venceu LSTM direct nem XGBoost na tabela principal. |
| `weighted_l1_hpo_mae` | `seq2seq_weighted_l1_hpo_20260509` | Melhor Seq2Seq attention individual; supera XGBoost em MAE, mas não vence LSTM direct. |
| Ablação final weighted L1 | `seq2seq_weighted_l1_final_ablation_20260509` | Mostra trade-off: blends e lag24 melhoram picos/cauda, mas o ganho global é pequeno e sensível a seed. |
| Atenção multi-head/gates/grupos/query por horizonte | runs de ablação do Seq2Seq attention | Não produziram ganho determinístico suficiente; usar como tentativa negativa/diagnóstico. |
| Luong dot/general/local e DA-RNN | runs de ablação do Seq2Seq attention | Úteis para dizer que mecanismos canônicos foram testados, mas não resolveram a irrelevância da atenção neste dataset. |
| Guided/supervised attention | runs de ablação do Seq2Seq attention | Forçar peso em recência/lag24/lag48 não trouxe salto determinístico; a informação funcionou melhor como feature/baseline/loss. |
| Scheduled sampling / teacher forcing | `teacher_forcing_paper_ablation` | Não trouxe ganho agregado; teacher forcing convencional e DTFP ficaram melhores que ITFP nesse protocolo. |
| Decoder com exógenas futuras causais | `seq2seq_improvement_suite_2026_04_21` | Foi um dos maiores ganhos em Cascata; usar como evidência de desenho do decoder, não como resultado Sapo. |
| `attention_conditioning=previous_state` | `seq2seq_improvement_suite_2026_04_21` | Pequeno ganho no regime forte com exógenas futuras completas. |
| `semi_direct_decoder` | `seq2seq_open_hypotheses_2026_04_21` | Trade-off: MAE muito próximo do controle, melhor estabilidade por horizonte e picos. |
| Recency-biased attention | `seq2seq_open_hypotheses_2026_04_21` | Melhorou em seed isolado, mas não sustentou vantagem clara em multi-seed. |
| Input feeding off | `seq2seq_open_hypotheses_2026_04_21` | Resultado negativo; piorou agregados e picos. |
| Decoder exog gate | `seq2seq_open_hypotheses_2026_04_21` | Melhorou alguns aspectos de pico/horizonte, mas pagou custo em MAE/RMSE. |
| Loss de picos | `itfp_peak_loss_ablation` e `seq2seq_open_hypotheses_2026_04_21` | Reduz erro em picos, mas piora MAE agregado. É trade-off de objetivo, não vitória geral. |
| Sampler por regime e aux event head | `event_window_ablation` e `aux_event_ablation` | Exploratórios; úteis para discussão de eventos raros, não para tabela principal. |

## 6. O Que Descartar do Núcleo Final

Remover ou rebaixar a histórico:

- Cascata/Piratininga como escopo principal.
- Ibirité como objeto central, salvo quando explicar histórico do projeto.
- Período 2015-2022.
- Horizonte de 12 horas como tarefa principal.
- Split por ano calendário `2016-2018 / 2019 / 2020` para o benchmark Sapo final.
- SAITS como método central.
- Narrativa M0-M4.
- Afirmação de que Attention + Scheduled Sampling venceu.
- Afirmação de que o XGBoost é o vencedor final atual. Ele venceu o benchmark fixo antigo, mas no estado mais recente o vencedor global é `lstm_direct_clean_pm10_hpo`.
- Afirmação de que o Seq2Seq attention "falhou" sem nuance. O correto é dizer que não venceu em MAE global, mas o `weighted_l1` melhorou picos/cauda e reduziu suavização.
- Afirmação de que o TCC propõe um modelo novo, se a contribuição real for protocolo experimental e comparação controlada.
- Resultados de notebooks antigos.
- Figuras placeholder.
- Conclusões probabilísticas sem calibração ou avaliação explícita de incerteza.
- `runtime/reports/ablation/tcc_ablation_20260320_152900.json` como cadeia sequencial final, porque o artefato executado tem erro de propagação de estado vencedor.

## 7. Comparabilidade: Regras Obrigatórias

### 7.1 Pode Comparar Diretamente

Pode comparar diretamente os modelos do relatório Sapo `clean_pm10_decoder_proxy` porque eles compartilham estação, split, tarefa, imputação, features e protocolo de avaliação:

- `lstm_recursive`;
- `lstm_direct`;
- `seq2seq_basic`;
- `seq2seq_attention`;
- XGB `multi_output_tree`, com ressalva metodológica abaixo.
- `weighted_l1_hpo_mae` pode ser comparado como variante do Seq2Seq attention, desde que o texto explicite que a função de perda foi alterada.

### 7.2 Pode Comparar com Ressalva

XGB pode ser comparado como baseline forte, mas o texto deve explicitar que o contrato de treino não é idêntico ao dos DL:

- XGB multi-output treina em janelas com horizonte completo observado;
- modelos DL usam máscara por ponto observado;
- a avaliação de teste é comparável, mas a exposição de treino não é perfeitamente simétrica.

Frase recomendada:

> O XGBoost multi-output foi tratado como baseline tabular forte sob contrato causal equivalente de entrada, embora seu treinamento multi-output exija janelas com horizonte completo observado.

Outra frase recomendada para métricas vs plots:

> O LSTM direto apresentou o melhor erro médio no holdout, enquanto variantes Seq2Seq com perda ponderada preservaram mais amplitude e reduziram parte do erro em regimes de maior concentração. Assim, a escolha do modelo depende de priorizar erro médio ou resposta a eventos altos.

### 7.3 Não Pode Comparar Diretamente

Não comparar diretamente, na mesma tabela principal:

- Sapo 70/15/15 com Cascata;
- Sapo 70/15/15 com Cascata/Piratininga;
- split 70/15/15 com split por ano calendário;
- runs com HPO contra runs sem HPO como se tivessem mesmo orçamento;
- loss de picos contra loss padrão sem discutir mudança de objetivo;
- modelos com horizonte 12h contra horizonte 24h como se fossem a mesma tarefa;
- dataset diário contra dataset horário como se a métrica respondesse à mesma pergunta;
- ensemble/blend contra modelo único sem explicitar que é uma combinação de predições;
- runtime ablation contra resultado de acurácia final;
- resultados do artefato sequencial de março como se a cadeia de vencedores fosse válida.

## 8. Pergunta, Objetivos e Contribuição

### Pergunta de Pesquisa

Formulação recomendada:

> Em uma tarefa horária de previsão de PM2.5 na estação Sapo, com entrada de 48 horas, horizonte de 24 horas e split temporal fixo, como diferentes escolhas de modelagem - arquiteturas sequenciais, baseline tabular, imputação, variáveis exógenas e estratégias de treinamento - afetam o desempenho preditivo e os erros por horizonte?

### Objetivo Geral

Avaliar, sob um protocolo experimental rastreável e comparável, o desempenho de modelos de aprendizado de máquina e deep learning para previsão horária multi-step de PM2.5 na estação Sapo, distinguindo erro médio global de comportamento em picos e cauda.

### Objetivos Específicos

- Construir uma base horária de PM2.5 e PM10 para a estação Sapo, com atributos temporais, flags de missingness e proxies causais.
- Definir um protocolo temporal `48 -> 24` com split cronológico `70/15/15`.
- Implementar pré-processamento com imputação, normalização e features causais sem vazamento de informação futura.
- Comparar LSTM direta, LSTM recursiva, Seq2Seq básico, Seq2Seq com atenção e XGBoost multi-output.
- Avaliar os modelos por métricas globais e por horizonte.
- Discutir ablações metodológicas relevantes, incluindo imputação, uso de PM10 causal, attention, estratégias de decoder, HPO e perdas voltadas a picos.
- Confrontar métricas agregadas com inspeção visual dos plots, especialmente suavização, viés à média e subestimação de eventos altos.
- Identificar limitações do protocolo e oportunidades de extensão para eventos extremos, múltiplas estações e modelos espaço-temporais.

### Contribuição Realista

Não vender o trabalho como criação de um novo modelo. A contribuição mais defensável é:

- um estudo comparável e rastreável em dados ambientais reais;
- uma análise honesta de modelos sequenciais e baseline tabular;
- documentação de trade-offs entre erro médio, horizonte de previsão, suavização visual e eventos de maior concentração;
- consolidação de uma pipeline que evita vazamento em imputação, normalização, janelamento e avaliação.

## 9. Estrutura Recomendada do Relatório

### Capítulo 1 - Introdução

Função: motivar o problema e declarar o escopo final.

Estrutura:

1. PM2.5 como problema ambiental e de saúde.
2. Necessidade de previsão horária de curto prazo.
3. Dificuldades: lacunas, sazonalidade, autocorrelação, picos raros, drift e risco de leakage.
4. Lacuna metodológica: comparações de modelos frequentemente confundem arquitetura, imputação, atributos, split e seleção.
5. Proposta: estudo comparável na estação Sapo, tarefa `48 -> 24`, com contrato `clean_pm10_decoder_proxy`.
6. Pergunta de pesquisa.
7. Objetivo geral e objetivos específicos.
8. Contribuições.
9. Organização do texto.

Cuidados:

- Declarar Sapo como escopo principal já na introdução.
- Não prometer que Seq2Seq attention vencerá.
- Não apresentar XGBoost como vencedor final se a tabela atual com HPO já mostra `lstm_direct_clean_pm10_hpo` à frente.
- Não prometer previsão operacional em produção.
- Não mencionar Cascata/Piratininga como se fossem o objeto final.

### Capítulo 2 - Fundamentação

Função: explicar apenas os conceitos usados depois.

Estrutura:

1. PM2.5 e monitoramento da qualidade do ar.
2. Séries temporais multivariadas.
3. Previsão multi-step: direta, recursiva e encoder-decoder.
4. Dados faltantes, imputação e vazamento temporal.
5. Janelas deslizantes, lags e variáveis exógenas disponíveis no momento da previsão.
6. LSTM.
7. Seq2Seq e atenção.
8. Teacher forcing e scheduled sampling.
9. Baselines tabulares e gradient boosting.
10. Métricas: MAE, RMSE, MAPE, R2, métricas por horizonte e viés.

Cuidados:

- Scheduled sampling deve ser descrito como técnica avaliada, não como solução vencedora.
- SAITS deve sair do centro.
- Previsão probabilística só deve ficar se a avaliação de incerteza for realmente apresentada.

### Capítulo 3 - Trabalhos Relacionados

Função: posicionar o trabalho na literatura.

Estrutura:

1. Previsão de PM2.5 com modelos estatísticos e aprendizado de máquina.
2. Deep learning para qualidade do ar.
3. LSTM, atenção e modelos encoder-decoder em séries ambientais.
4. Tratamento de dados faltantes em séries temporais ambientais.
5. Protocolos de avaliação temporal e problemas de comparabilidade.
6. Como este TCC se diferencia: escopo fixo, pipeline rastreável, ablações e baseline tabular.

Evitar uma lista de artigos. Cada trabalho citado deve sustentar uma decisão ou lacuna.

### Capítulo 4 - Metodologia

Função: permitir reprodução do experimento principal.

Estrutura:

1. Fonte de dados e estação Sapo.
2. Variável-alvo e variáveis explicativas.
3. Recorte temporal do artefato atual e justificativa do filtro aplicado.
4. Formulação da tarefa `48 -> 24`.
5. Split cronológico `70/15/15`.
6. Pré-processamento:
   - alinhamento horário;
   - tratamento de ausências;
   - imputação linear no contrato atual;
   - máscaras de alvo imputado;
   - normalização com estatísticas do treino.
7. Feature engineering:
   - atributos temporais;
   - Fourier;
   - PM2.5 e PM10 no encoder;
   - missingness;
   - `PM10_proxy_exante`;
   - `PM10_trend_exante`;
   - exclusão de variáveis muito esparsas, sem afirmar causalidade forte.
8. Modelos:
   - LSTM recursiva;
   - LSTM direta;
   - Seq2Seq básico;
   - Seq2Seq com atenção;
   - Seq2Seq attention com `weighted_l1` como variante;
   - XGBoost multi-output.
9. Treinamento:
   - HPO no resultado atual;
   - early stopping;
   - monitoramento por validação;
   - distinção entre benchmark fixo antigo e resultado atual com HPO.
10. Métricas.
11. Desenho das ablações auxiliares.
12. Ambiente computacional e reprodutibilidade.

Cuidados:

- Não escrever split por ano calendário para o benchmark Sapo.
- Não escrever Cascata/Piratininga na seção de dados principal.
- Não dizer que `fs_physics` mede impacto isolado de física.
- Explicar que XGB é baseline tabular forte com ressalva de contrato de treino.
- Explicar que o `weighted_l1` é uma função de perda ponderada, não regularização L1.

### Capítulo 5 - Resultados e Discussão

Função: apresentar evidência, não uma narrativa otimista.

Estrutura recomendada:

1. Caracterização breve do benchmark Sapo.
2. Resultado principal `clean_pm10_decoder_proxy` com HPO.
3. Métricas por horizonte.
4. Discussão do `lstm_direct_clean_pm10_hpo` como vencedor global por MAE/RMSE/R2.
5. Comparação entre modelos DL.
6. Discussão do XGBoost como baseline tabular forte.
7. Discussão do Seq2Seq attention:
   - attention HPO canônico ficou competitivo, mas não venceu;
   - `weighted_l1_hpo_mae` foi o melhor Seq2Seq attention individual;
   - variantes com lag24 e weighted L1 melhoraram picos/cauda;
   - atenção explícita continuou pouco interpretável/quase uniforme em vários testes.
8. Métricas vs plots:
   - LSTM direct e XGBoost acertam mais o erro médio por suavização;
   - Seq2Seq weighted L1 preserva mais amplitude;
   - discutir p99, `std_ratio`, `peak35_mae` e subestimação de picos junto com MAE.
9. Ablations metodológicas:
   - imputação;
   - features;
   - PM10 causal no decoder;
   - delta/residual/log/loss, apenas se houver evidência rastreável;
   - runtime apenas como custo, não como acurácia.
10. Ablations internas do Seq2Seq como estudos auxiliares:
   - scheduled sampling;
   - decoder com exógenas causais;
   - semi-direct;
   - attention recency;
   - Luong/local/DA-RNN/guided attention;
   - loss de picos;
   - sampler e aux event.
11. Ameaças à validade:
   - uma estação principal;
   - split único;
   - sensibilidade a seed em DL;
   - XGB com contrato de treino diferente;
   - picos raros;
   - generalização para outras estações.

Cuidados:

- Não escolher modelo por validação e depois trocar por teste sem explicar.
- Não esconder que `lstm_direct_clean_pm10_hpo` é melhor no erro médio atual.
- Não esconder que XGBoost e LSTM direct podem parecer mais suaves nos plots.
- Não transformar o bom comportamento visual do Seq2Seq em vitória global sem respaldo de MAE/RMSE/R2.
- Não misturar números de Cascata com Sapo.
- Resultados negativos devem ser tratados como achados metodológicos.

### Capítulo 6 - Conclusão

Função: responder à pergunta de pesquisa dentro dos limites do que foi medido.

Estrutura:

1. Retomar a pergunta.
2. Responder com base no benchmark Sapo.
3. Destacar principais achados:
   - LSTM direct foi o vencedor global atual por erro médio;
   - XGBoost permanece baseline tabular forte;
   - Seq2Seq attention não venceu globalmente, mas o `weighted_l1` o tornou competitivo;
   - Seq2Seq weighted L1 apresentou comportamento visual menos suavizado e melhor em parte dos picos;
   - escolhas de decoder e features importam;
   - picos exigem trade-off de objetivo.
4. Limitações.
5. Trabalhos futuros:
   - validação multi-seed e HPO mais amplo;
   - múltiplas estações;
   - modelos espaço-temporais;
   - avaliação focada em eventos extremos;
   - calibração probabilística, se saída probabilística for retomada;
   - implantação operacional.

## 10. Figuras e Tabelas Recomendadas

### Figuras

| Figura | Capítulo | Observação |
| --- | --- | --- |
| Diagrama da tarefa `48 -> 24` | 1 ou 4 | Criar figura simples e própria. |
| Linha temporal do split `70/15/15` | 4 | Deve mostrar proporção, não anos fixos. |
| Pipeline experimental | 4 | Dados, imputação, features, janelas, modelos, validação e teste. |
| Localização ou identificação da estação Sapo | 4 | Usar fonte confiável ou tabela se mapa não for necessário. |
| Ranking exploratório de estações | 4 | Fundamentar por que Sapo foi escolhida entre outras estações/usinas. |
| Cobertura mensal e lacunas de Sapo | 4 | Mostrar gaps, continuidade parcial e necessidade de máscaras de ausência. |
| Distribuição de PM2.5 por split | 4 ou 5 | Gerar especificamente para Sapo e discutir eventos raros. |
| Resultado principal dos modelos | 5 | Barras de MAE/RMSE ou tabela limpa. |
| Erro por horizonte | 5 | Usar h1, h6, h12, h24 ou todos os horizontes. |
| Predito vs observado | 5 | Obrigatório para comparar suavização de LSTM direct/XGBoost contra amplitude do Seq2Seq weighted L1. |
| Métrica vs comportamento visual | 5 | Painel ou sequência de plots mostrando MAE/RMSE junto de p99, `std_ratio` e erro em picos. |
| Erro por regime de concentração | 5 | Usar `peak35_mae`, viés em picos e taxa de subestimação quando disponíveis. |

### Tabelas

- Descrição da estação Sapo e período.
- Variáveis usadas.
- Missingness e cobertura temporal.
- Split `70/15/15`.
- Espaço de HPO e melhores hiperparâmetros por modelo.
- Resultado principal `clean_pm10_decoder_proxy` com HPO.
- Métricas por horizonte.
- Métricas de cauda/picos: `peak35_mae`, p99 previsto/observado, `std_ratio`, viés em picos.
- Tabela separada do benchmark fixo antigo, se for usado como histórico.
- Resumo das ablações auxiliares, claramente rotuladas como auxiliares.
- Ameaças à validade.

## 11. Bibliografia Mínima por Bloco

| Bloco | Referências-base esperadas |
| --- | --- |
| PM2.5 e saúde | WHO 2021; Pope e Dockery; Brook et al.; estudos epidemiológicos recentes. |
| Qualidade do ar no Brasil | Fonte oficial da rede de monitoramento e artigos brasileiros relevantes. |
| Séries temporais e avaliação temporal | Hyndman; Tashman; Bergmeir ou equivalentes. |
| Missing data | Rubin; KNN imputation; MICE; MissForest; SAITS apenas como relacionado se necessário. |
| LSTM e Seq2Seq | Hochreiter e Schmidhuber; Sutskever; Bahdanau. |
| Atenção em Seq2Seq | Bahdanau; Luong; DA-RNN se citado; supervised/guided attention se a ablação for discutida. |
| Scheduled sampling | Bengio et al. |
| Gradient boosting / XGBoost | Chen e Guestrin. |
| Métricas e avaliação | Referências de forecasting e avaliação de regressão. |
| PM2.5 com deep learning | Reviews e artigos recentes de previsão de qualidade do ar. |

Antes de escrever a fundamentação, limpar `referencias.bib` para conter entradas realmente usadas.

## 12. Artefatos Auxiliares a Criar

Antes de reescrever os capítulos finais, criar dois arquivos no relatório:

1. `MATRIZ_REFERENCIAS_TCC.md`
   - chave BibTeX;
   - tema;
   - seção onde será usada;
   - frase/ideia que sustenta;
   - status do PDF/link.

2. `MANIFESTO_EVIDENCIAS_TCC.md`
   - config;
   - comando;
   - data da execução;
   - commit do `TCC-wsl`;
   - dataset path/hash quando houver;
   - run ids;
   - CSV/MD oficial;
   - figuras exportadas.

Sem esse manifesto, o Capítulo 5 tende a voltar a misturar histórico com resultado final.

## 13. Checklist de Coerência

### Geral

- [x] O texto declara Sapo como estação principal.
- [x] O texto não trata Cascata/Piratininga como escopo final.
- [x] O período descrito bate com o artefato `clean_pm10_decoder_proxy` atual.
- [x] A tarefa é `48 -> 24`.
- [x] O split principal é `70/15/15`.
- [x] A tabela principal vem de `runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/`.
- [x] Resultados auxiliares estão rotulados como auxiliares.
- [x] XGB é apresentado com ressalva metodológica.
- [x] O resultado final é descrito como HPO em DL e XGBoost.
- [x] O benchmark fixo antigo sem HPO é rotulado como histórico.
- [x] O texto declara `lstm_direct_clean_pm10_hpo` como vencedor global atual por erro médio.
- [x] O texto declara `weighted_l1_hpo_mae` como melhor Seq2Seq attention individual.
- [x] O texto discute que LSTM direct/XGBoost são mais suaves nos plots e que Seq2Seq weighted L1 preserva mais amplitude.
- [x] O texto não afirma que scheduled sampling venceu.
- [x] O texto não transforma o bom plot do Seq2Seq em vitória global sem respaldo de métrica.

### Capítulo 1

- [x] Problema e relevância do PM2.5 atualizados.
- [x] Escopo Sapo declarado.
- [x] Pergunta de pesquisa alinhada ao estudo comparável.
- [x] Objetivos sem promessas inválidas.
- [x] Contribuição descrita como protocolo/análise, não como novo modelo.

### Capítulo 2

- [x] PM2.5 e previsão horária fundamentados.
- [x] Séries temporais multi-step explicadas.
- [x] Missing data e leakage discutidos.
- [x] LSTM, Seq2Seq, atenção e scheduled sampling descritos.
- [x] XGBoost incluído se continuar como baseline oficial.
- [x] SAITS removido do centro.

### Capítulo 3

- [x] Trabalhos relacionados organizados por eixo.
- [x] Estudos de PM2.5 recentes incluídos.
- [x] Protocolos de avaliação temporal discutidos.
- [x] Lacuna do TCC explicitada sem exagero.

### Capítulo 4

- [x] Dados, estação, período e split batem com configs oficiais.
- [x] EDA comparativa de outras estações fundamenta a escolha de Sapo.
- [x] EDA de Sapo mostra cobertura, lacunas e blocos observados contínuos.
- [x] Pré-processamento descrito sem leakage.
- [x] Alvo imputado fora de loss/métricas observadas está explicado.
- [x] Features descritas sem prometer causalidade meteorológica.
- [x] PM10 proxy/trend causal está explicado como known-future input.
- [x] Modelos e baseline descritos.
- [x] Seleção por validação explicada.
- [x] HPO do resultado atual explicitado.

### Capítulo 5

- [x] Resultados vêm de CSV/MD oficial.
- [x] Tabelas têm origem rastreável.
- [x] LSTM direct vencedor atual aparece honestamente.
- [x] XGBoost aparece como baseline forte, não vencedor final atual.
- [x] Melhor Seq2Seq attention (`weighted_l1_hpo_mae`) aparece separadamente.
- [x] Plots são discutidos junto de p99, `std_ratio` e erro em picos.
- [x] Métricas por horizonte são discutidas.
- [x] Ablations auxiliares não são misturadas com Sapo.
- [x] Resultados negativos são interpretados.

### Capítulo 6

- [x] Responde à pergunta de pesquisa.
- [x] Não contradiz os números.
- [x] Limitações são concretas.
- [x] Trabalhos futuros derivam das limitações reais.

## 14. Primeiro Movimento Recomendado

Ordem prática de trabalho:

- [x] Criar `MANIFESTO_EVIDENCIAS_TCC.md` com `clean_pm10_decoder_proxy` como fonte principal.
- [x] Criar `MATRIZ_REFERENCIAS_TCC.md`.
- [x] Reescrever Capítulo 1 para travar escopo Sapo.
- [x] Reescrever Capítulo 4 antes dos resultados, porque ele define o contrato experimental.
- [x] Reescrever Capítulo 5 com a tabela Sapo atual, a seção de plots vs métricas e uma seção separada de ablações auxiliares.
- [x] Reescrever Capítulos 2 e 3 com bibliografia ajustada ao método real.
- [x] Reescrever Capítulo 6.
- [x] Atualizar resumo, abstract, listas, figuras e referências.
- [x] Compilar o PDF e corrigir inconsistências.

Subtarefas já entregues da etapa de atualização final:

- [x] Título do trabalho atualizado para não prometer um modelo Attention-LSTM como contribuição central.
- [x] Resumo atualizado para Sapo, `48 -> 24`, `clean_pm10_decoder_proxy` e vencedor LSTM direct.
- [x] Abstract atualizado com a mesma conclusão do resumo.
- [x] Lista de abreviações atualizada, removendo SAITS do centro e incluindo HPO, PM10, R2 e XGBoost.
- [x] Entradas BibTeX pendentes adicionadas para XGBoost, Optuna, Huber, Luong, DA-RNN e estudos recentes de PM2.5.
- [x] Figuras finais revisadas/exportadas.
- [x] `referencias.bib` limpo e complementado com entradas pendentes da matriz.
- [x] Figura 5.2 reorganizada em painéis por modelo, com escala comum e quebras nos gaps.
- [x] EDA de Sapo inserida no Capítulo 4 com ranking, cobertura, lacunas, distribuição e picos.
- [x] Escolha de Sapo fundamentada com EDA de outras estações e estudos exploratórios auxiliares.
- [x] Referências a documentos internos removidas do corpo do TCC; evidências técnicas ficam fora da leitura principal.
- [x] Aliases internos de modelos substituídos por nomes acadêmicos legíveis nas tabelas e análises.
- [x] Justificativa de Sapo reforçada com o melhor MAE nos testes exploratórios contra Barra Longa/Centro, Aeroporto CMD e Ibirité/Cascata.

## 15. Reforço Acadêmico Solicitado

Subtarefas entregues na rodada de fortalecimento teórico:

- [x] Referências estruturantes de deep forecasting pesquisadas antes da escrita.
- [x] Surveys de deep learning para séries temporais adicionados à bibliografia.
- [x] Referências específicas para Seq2Seq/multi-horizon forecasting adicionadas.
- [x] Capítulo 2 expandido com formulação matemática da tarefa `48 -> 24`.
- [x] Equações da LSTM adicionadas.
- [x] Equações do Seq2Seq com atenção adicionadas.
- [x] Objetivo regularizado do XGBoost adicionado.
- [x] Fórmulas de Huber, loss mascarada e `weighted_l1` adicionadas.
- [x] Citações diretas curtas incluídas para sustentar deep forecasting, Seq2Seq, atenção e padronização experimental.
- [x] Citações indiretas ampliadas para PM2.5, protocolos temporais e arquiteturas multi-horizonte.
- [x] Diagramas próprios de LSTM, Seq2Seq com atenção e XGBoost multi-output gerados e citados.
- [x] Legendas dos diagramas deixam claro que as imagens são elaboração própria baseada nas referências, não figuras copiadas.
- [x] Diagramas próprios redesenhados com melhor organização visual, versões PDF vetoriais e script reprodutível.
- [x] Diagramas próprios reorganizados para reduzir sobreposição de vetores/setas e melhorar leitura.
- [x] Parêntese metodológico sobre Transformers e arquiteturas mais novas adicionado.
- [x] Pesos de atenção extraídos dos checkpoints finais.
- [x] Plots de perfil médio e heatmap de atenção inseridos no Capítulo 5.
- [x] Análise do impacto real da camada de atenção adicionada aos resultados.
- [x] Figuras 5.3 e 5.4 reconciliadas: escala do heatmap corrigida, média por posição adicionada e diferença numérica documentada.
- [x] Fundamentação de séries temporais expandida com componentes, decomposição aditiva e autocorrelação.
- [x] Figura de decomposição descritiva da série PM2.5 de Sapo adicionada ao Capítulo 2.
- [x] Figura de teacher forcing vs. scheduled sampling adicionada ao Capítulo 2.
- [x] Direção do scheduled sampling validada: \(p_{TF}\) decrescente segue o paper original; agenda crescente foi fundamentada por Teutsch e Mäder (Flipped Classroom/Increasing Teacher Forcing), mas permaneceu como ablação auxiliar e não eixo do resultado final.
- [x] Funcionamento do Optuna, TPE e poda por Hyperband descritos na fundamentação teórica.
- [x] Escolha do HyperbandPruner referenciada com documentação oficial do Optuna.
- [x] Espaço de busca de HPO por modelo adicionado ao Capítulo 4.
- [x] Hiperparâmetros vencedores por modelo adicionados ao Capítulo 4.

O erro que a reescrita precisa evitar é simples: o texto não pode parecer um TCC sobre Cascata/Piratininga com resultados novos de Sapo colados no final. O relatório deve nascer como um estudo de Sapo; todo o restante entra apenas como contexto técnico ou ablação auxiliar claramente identificada.
