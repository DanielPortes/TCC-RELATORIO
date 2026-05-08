# Guia de Reescrita do TCC-RELATORIO

Este guia define como reescrever o `TCC-RELATORIO` a partir do estado atual do projeto técnico em `../TCC-wsl`.

A regra principal é: `TCC-wsl` é a fonte técnica atual; `TCC-RELATORIO` ainda contém texto de fases anteriores. A reescrita deve preservar a motivação do problema de previsão de PM2.5, mas reconstruir escopo, método, resultados e conclusão a partir dos artefatos atuais e comparáveis.

## 1. Escopo Atual do Projeto

O TCC final deve ser apresentado como um estudo experimental de previsão horária de PM2.5 para a estação `Sapo`, no conjunto CMD, com protocolo comparável de modelos e ablações controladas.

Escopo oficial:

| Item | Definição final |
| --- | --- |
| Poluente-alvo | `PM2.5` horário |
| Estação principal | `Sapo` / CMD |
| Período | `2016-01-01 00:00:00` a `2020-12-31 23:00:00` |
| Tarefa | usar 48 horas passadas para prever as próximas 24 horas (`48 -> 24`) |
| Split | cronológico por proporção `70/15/15` |
| Treino | primeiros 70% do período filtrado |
| Validação | 15% seguintes |
| Teste | 15% finais |
| Imputação do benchmark principal | `knn` |
| Feature set principal | `lag_cmd_sapo_ratio_70_15_15` |
| Modelos DL principais | `lstm_recursive`, `lstm_direct`, `seq2seq_basic`, `seq2seq_attention` |
| Baseline tabular | XGBoost `multi_output_tree` |
| Busca de hiperparâmetros no benchmark principal | desativada (`optimization.n_trials=0`) |
| Seleção de checkpoint | validação, principalmente `val/selection_score` |
| Avaliação final | métricas no holdout de teste |

O escopo principal **não é mais Cascata/Piratininga**. Essas estações aparecem apenas em experimentos históricos ou auxiliares de desenvolvimento do Seq2Seq. Elas não devem ser descritas como o objeto central do TCC final.

## 2. Diagnóstico do Relatório Atual

A reescrita ainda deve ser grande.

O texto atual mistura várias fases do projeto: Ibirité/Cascata/Piratininga, horizonte de 12 horas, narrativa M0-M4, SAITS, notebooks antigos, scheduled sampling como conclusão central e resultados que não pertencem ao benchmark Sapo 70/15/15.

Esses elementos devem ser removidos do núcleo do relatório ou rebaixados a histórico, quando forem úteis para explicar a evolução do projeto. O relatório final precisa contar uma história única:

1. existe um problema de previsão horária de PM2.5 em dados ambientais reais;
2. o trabalho fixa um protocolo temporal comparável para a estação Sapo;
3. diferentes famílias de modelos são avaliadas sob o mesmo contrato de dados;
4. ablações metodológicas explicam decisões de imputação, features, treino e desenho do Seq2Seq;
5. os resultados são discutidos com honestidade, inclusive quando modelos neurais não vencem o baseline tabular.

## 3. Fontes de Verdade

Use estes arquivos antes de escrever qualquer capítulo técnico:

| Fonte | Uso |
| --- | --- |
| `../TCC-wsl/configs/ablation_new/step3_architectures_sapo_70_15_15.yaml` | Configuração central do benchmark Sapo 70/15/15, 4 DL + XGB. |
| `../TCC-wsl/configs/data_source/cmd_sapo.yaml` | Fonte de dados e estação Sapo. |
| `../TCC-wsl/configs/period/cmd_sapo_2016_2020_ratio_70_15_15.yaml` | Período oficial do benchmark Sapo. |
| `../TCC-wsl/configs/experiment/seq_len_48x24_cmd_sapo_70_15_15.yaml` | Formulação `48 -> 24`. |
| `../TCC-wsl/configs/feature_set/lag_cmd_sapo_ratio_70_15_15.yaml` | Features usadas no benchmark principal. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.csv` | Tabela principal de resultados atuais. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.md` | Resumo legível do benchmark principal. |
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

Não use valores de notebooks antigos, prints soltos ou runs sem config rastreável como resultado final.

## 4. Resultado Principal Atual

A tabela principal do TCC deve partir do benchmark Sapo 70/15/15:

| Modelo | MAE | RMSE | MAPE | R2 | H1 MAE | H24 MAE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| XGB `multi_output_tree` | 2.9481 | 4.0654 | 24.45 | 0.4555 | 2.4844 | 3.1551 |
| `lstm_recursive` | 3.0423 | 4.0989 | 25.45 | 0.4465 | 2.7913 | 3.2607 |
| `seq2seq_attention` | 3.0655 | 4.3341 | 25.71 | 0.3811 | 2.4811 | 3.3650 |
| `lstm_direct` | 3.1790 | 4.2441 | 27.32 | 0.4065 | 3.0173 | 3.2618 |
| `seq2seq_basic` | 3.2586 | 4.6867 | 26.83 | 0.2763 | 2.5780 | 3.5036 |

Esses valores devem ser conferidos diretamente no CSV oficial no momento da escrita final. A interpretação esperada é:

- o XGBoost multi-output é o melhor em MAE no benchmark atual;
- os modelos DL ficam próximos, especialmente `lstm_recursive` e `seq2seq_attention`;
- `seq2seq_attention` não deve ser apresentado como vencedor global se os números finais permanecerem assim;
- `seq2seq_basic` funciona como baseline encoder-decoder simples, mas não é o melhor;
- a comparação é válida como benchmark de configuração fixa, não como competição com HPO igual para todos.

## 5. Eixos Experimentais do TCC

O relatório deve separar claramente três níveis de evidência.

### 5.1 Núcleo Principal

Este é o eixo obrigatório do TCC:

1. estação Sapo;
2. período 2016-2020;
3. tarefa `48 -> 24`;
4. split cronológico `70/15/15`;
5. imputação `knn`;
6. features `lag_cmd_sapo_ratio_70_15_15`;
7. comparação `4DL + XGB`;
8. avaliação por MAE, RMSE, MAPE, R2 e métricas por horizonte.

Esse eixo deve ocupar o Capítulo 4 e a parte principal do Capítulo 5.

### 5.2 Ablations Metodológicas

Estas ablações explicam decisões de projeto, mas nem todas são resultado final direto em Sapo:

| Eixo | Como tratar |
| --- | --- |
| Imputação | Discutir `linear`, `knn`, `iterative_rf`; no benchmark principal Sapo, o contrato atual usa `knn`. |
| Delta/residual learning | Pode entrar como decisão metodológica se houver artefato oficial comparável. |
| Feature set / physics | Não chamar de impacto isolado de física se o conjunto altera também lags, tempo, proxies e colunas. |
| Log target / loss | Tratar como ablação de função objetivo e transformação do alvo, com cuidado para não selecionar por teste. |
| Stride / orçamento de treino | Discutir como engenharia experimental se for usado para justificar custo e redundância de janelas. |

Se uma ablação não foi rerodada no escopo Sapo 70/15/15, ela deve ser escrita como estudo auxiliar, não como conclusão final do benchmark.

### 5.3 Ablations Internas do Seq2Seq

Estas ablações são importantes para explicar o desenvolvimento do modelo, mas foram executadas em escopos auxiliares, principalmente Cascata ou Cascata/Piratininga. Elas não podem ser misturadas numericamente com a tabela Sapo.

| Tema | Evidência atual | Interpretação correta |
| --- | --- | --- |
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
- Afirmação de que o TCC propõe um modelo novo, se a contribuição real for protocolo experimental e comparação controlada.
- Resultados de notebooks antigos.
- Figuras placeholder.
- Conclusões probabilísticas sem calibração ou avaliação explícita de incerteza.
- `runtime/reports/ablation/tcc_ablation_20260320_152900.json` como cadeia sequencial final, porque o artefato executado tem erro de propagação de estado vencedor.

## 7. Comparabilidade: Regras Obrigatórias

### 7.1 Pode Comparar Diretamente

Pode comparar diretamente os modelos do relatório Sapo 70/15/15 porque eles compartilham estação, período, split, tarefa, imputação, features e stride:

- `lstm_recursive`;
- `lstm_direct`;
- `seq2seq_basic`;
- `seq2seq_attention`;
- XGB `multi_output_tree`, com ressalva metodológica abaixo.

### 7.2 Pode Comparar com Ressalva

XGB pode ser comparado como baseline forte, mas o texto deve explicitar que o contrato de treino não é idêntico ao dos DL:

- XGB multi-output treina em janelas com horizonte completo observado;
- modelos DL usam máscara por ponto observado;
- a avaliação de teste é comparável, mas a exposição de treino não é perfeitamente simétrica.

Frase recomendada:

> O XGBoost multi-output foi tratado como baseline tabular forte sob contrato causal equivalente de entrada, embora seu treinamento multi-output exija janelas com horizonte completo observado.

### 7.3 Não Pode Comparar Diretamente

Não comparar diretamente, na mesma tabela principal:

- Sapo 70/15/15 com Cascata;
- Sapo 70/15/15 com Cascata/Piratininga;
- split 70/15/15 com split por ano calendário;
- runs com HPO contra runs sem HPO como se tivessem mesmo orçamento;
- loss de picos contra loss padrão sem discutir mudança de objetivo;
- runtime ablation contra resultado de acurácia final;
- resultados do artefato sequencial de março como se a cadeia de vencedores fosse válida.

## 8. Pergunta, Objetivos e Contribuição

### Pergunta de Pesquisa

Formulação recomendada:

> Em uma tarefa horária de previsão de PM2.5 na estação Sapo, com entrada de 48 horas, horizonte de 24 horas e split temporal fixo, como diferentes escolhas de modelagem - arquiteturas sequenciais, baseline tabular, imputação, variáveis exógenas e estratégias de treinamento - afetam o desempenho preditivo e os erros por horizonte?

### Objetivo Geral

Avaliar, sob um protocolo experimental rastreável e comparável, o desempenho de modelos de aprendizado de máquina e deep learning para previsão horária multi-step de PM2.5 na estação Sapo.

### Objetivos Específicos

- Construir uma base horária de PM2.5 e variáveis meteorológicas para a estação Sapo no período 2016-2020.
- Definir um protocolo temporal `48 -> 24` com split cronológico `70/15/15`.
- Implementar pré-processamento com imputação, normalização e features causais sem vazamento de informação futura.
- Comparar LSTM direta, LSTM recursiva, Seq2Seq básico, Seq2Seq com atenção e XGBoost multi-output.
- Avaliar os modelos por métricas globais e por horizonte.
- Discutir ablações metodológicas relevantes, incluindo imputação, uso de variáveis exógenas, scheduled sampling, estratégias de decoder e perdas voltadas a picos.
- Identificar limitações do protocolo e oportunidades de extensão para eventos extremos, múltiplas estações e modelos espaço-temporais.

### Contribuição Realista

Não vender o trabalho como criação de um novo modelo. A contribuição mais defensável é:

- um estudo comparável e rastreável em dados ambientais reais;
- uma análise honesta de modelos sequenciais e baseline tabular;
- documentação de trade-offs entre erro médio, horizonte de previsão e eventos de maior concentração;
- consolidação de uma pipeline que evita vazamento em imputação, normalização, janelamento e avaliação.

## 9. Estrutura Recomendada do Relatório

### Capítulo 1 - Introdução

Função: motivar o problema e declarar o escopo final.

Estrutura:

1. PM2.5 como problema ambiental e de saúde.
2. Necessidade de previsão horária de curto prazo.
3. Dificuldades: lacunas, sazonalidade, autocorrelação, picos raros, drift e risco de leakage.
4. Lacuna metodológica: comparações de modelos frequentemente confundem arquitetura, imputação, atributos, split e seleção.
5. Proposta: estudo comparável na estação Sapo, 2016-2020, tarefa `48 -> 24`.
6. Pergunta de pesquisa.
7. Objetivo geral e objetivos específicos.
8. Contribuições.
9. Organização do texto.

Cuidados:

- Declarar Sapo como escopo principal já na introdução.
- Não prometer que Seq2Seq attention vencerá.
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
3. Recorte temporal 2016-2020.
4. Formulação da tarefa `48 -> 24`.
5. Split cronológico `70/15/15`.
6. Pré-processamento:
   - alinhamento horário;
   - tratamento de ausências;
   - imputação fitada no treino;
   - máscaras de alvo imputado;
   - normalização com estatísticas do treino.
7. Feature engineering:
   - atributos temporais;
   - Fourier;
   - lag de PM2.5;
   - missingness;
   - proxies meteorológicos ex-ante;
   - atributos físicos, sem afirmar causalidade.
8. Modelos:
   - LSTM recursiva;
   - LSTM direta;
   - Seq2Seq básico;
   - Seq2Seq com atenção;
   - XGBoost multi-output.
9. Treinamento:
   - orçamento fixo;
   - early stopping;
   - monitoramento por validação;
   - ausência de HPO no benchmark principal.
10. Métricas.
11. Desenho das ablações auxiliares.
12. Ambiente computacional e reprodutibilidade.

Cuidados:

- Não escrever split por ano calendário para o benchmark Sapo.
- Não escrever Cascata/Piratininga na seção de dados principal.
- Não dizer que `fs_physics` mede impacto isolado de física.
- Explicar que XGB é baseline tabular forte com ressalva de contrato de treino.

### Capítulo 5 - Resultados e Discussão

Função: apresentar evidência, não uma narrativa otimista.

Estrutura recomendada:

1. Caracterização breve do benchmark Sapo.
2. Resultado principal 4DL + XGB.
3. Métricas por horizonte.
4. Discussão do XGB como baseline vencedor atual.
5. Comparação entre modelos DL.
6. Discussão do Seq2Seq attention: desempenho próximo, mas não vencedor global.
7. Ablations metodológicas:
   - imputação;
   - features;
   - delta/residual/log/loss, apenas se houver evidência rastreável;
   - runtime apenas como custo, não como acurácia.
8. Ablations internas do Seq2Seq como estudos auxiliares:
   - scheduled sampling;
   - decoder com exógenas causais;
   - semi-direct;
   - attention recency;
   - loss de picos;
   - sampler e aux event.
9. Ameaças à validade:
   - uma estação principal;
   - split único;
   - ausência de HPO no benchmark principal;
   - XGB com contrato de treino diferente;
   - picos raros;
   - generalização para outras estações.

Cuidados:

- Não escolher modelo por validação e depois trocar por teste sem explicar.
- Não esconder que XGB é melhor no resultado atual.
- Não misturar números de Cascata com Sapo.
- Resultados negativos devem ser tratados como achados metodológicos.

### Capítulo 6 - Conclusão

Função: responder à pergunta de pesquisa dentro dos limites do que foi medido.

Estrutura:

1. Retomar a pergunta.
2. Responder com base no benchmark Sapo.
3. Destacar principais achados:
   - XGB forte no erro global;
   - LSTM/Seq2Seq competitivos;
   - Seq2Seq attention não necessariamente vencedor;
   - escolhas de decoder e features importam;
   - picos exigem trade-off de objetivo.
4. Limitações.
5. Trabalhos futuros:
   - rerodagem com HPO igual;
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
| Distribuição de PM2.5 por split | 4 ou 5 | Gerar especificamente para Sapo se ainda não existir. |
| Resultado principal dos modelos | 5 | Barras de MAE/RMSE ou tabela limpa. |
| Erro por horizonte | 5 | Usar h1, h6, h12, h24 ou todos os horizontes. |
| Predito vs observado | 5 | Se houver artefato final confiável. |
| Erro por regime de concentração | 5 | Só se calculado no benchmark Sapo. |

### Tabelas

- Descrição da estação Sapo e período.
- Variáveis usadas.
- Missingness e cobertura temporal.
- Split `70/15/15`.
- Hiperparâmetros fixos do benchmark.
- Resultado 4DL + XGB.
- Métricas por horizonte.
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

- [ ] O texto declara Sapo como estação principal.
- [ ] O texto não trata Cascata/Piratininga como escopo final.
- [ ] O período é 2016-2020.
- [ ] A tarefa é `48 -> 24`.
- [ ] O split principal é `70/15/15`.
- [ ] A tabela principal vem do relatório Sapo 70/15/15.
- [ ] Resultados auxiliares estão rotulados como auxiliares.
- [ ] XGB é apresentado com ressalva metodológica.
- [ ] O benchmark principal é descrito como configuração fixa, sem HPO.
- [ ] O texto não afirma que scheduled sampling venceu.
- [ ] O texto não afirma que Seq2Seq attention venceu se o CSV atual continuar mostrando XGB/lstm_recursive à frente.

### Capítulo 1

- [ ] Problema e relevância do PM2.5 atualizados.
- [ ] Escopo Sapo declarado.
- [ ] Pergunta de pesquisa alinhada ao estudo comparável.
- [ ] Objetivos sem promessas inválidas.
- [ ] Contribuição descrita como protocolo/análise, não como novo modelo.

### Capítulo 2

- [ ] PM2.5 e previsão horária fundamentados.
- [ ] Séries temporais multi-step explicadas.
- [ ] Missing data e leakage discutidos.
- [ ] LSTM, Seq2Seq, atenção e scheduled sampling descritos.
- [ ] XGBoost incluído se continuar como baseline oficial.
- [ ] SAITS removido do centro.

### Capítulo 3

- [ ] Trabalhos relacionados organizados por eixo.
- [ ] Estudos de PM2.5 recentes incluídos.
- [ ] Protocolos de avaliação temporal discutidos.
- [ ] Lacuna do TCC explicitada sem exagero.

### Capítulo 4

- [ ] Dados, estação, período e split batem com configs oficiais.
- [ ] Pré-processamento descrito sem leakage.
- [ ] Features descritas sem prometer causalidade meteorológica.
- [ ] Modelos e baseline descritos.
- [ ] Seleção por validação explicada.
- [ ] Ausência de HPO no benchmark principal explicitada.

### Capítulo 5

- [ ] Resultados vêm de CSV/MD oficial.
- [ ] Tabelas têm origem rastreável.
- [ ] XGB vencedor atual aparece honestamente.
- [ ] Métricas por horizonte são discutidas.
- [ ] Ablations auxiliares não são misturadas com Sapo.
- [ ] Resultados negativos são interpretados.

### Capítulo 6

- [ ] Responde à pergunta de pesquisa.
- [ ] Não contradiz os números.
- [ ] Limitações são concretas.
- [ ] Trabalhos futuros derivam das limitações reais.

## 14. Primeiro Movimento Recomendado

Ordem prática de trabalho:

1. Criar `MANIFESTO_EVIDENCIAS_TCC.md` com o benchmark Sapo como fonte principal.
2. Criar `MATRIZ_REFERENCIAS_TCC.md`.
3. Reescrever Capítulo 1 para travar escopo Sapo.
4. Reescrever Capítulo 4 antes dos resultados, porque ele define o contrato experimental.
5. Reescrever Capítulo 5 com a tabela Sapo e uma seção separada de ablações auxiliares.
6. Reescrever Capítulos 2 e 3 com bibliografia ajustada ao método real.
7. Reescrever Capítulo 6.
8. Atualizar resumo, abstract, listas, figuras e referências.
9. Compilar o PDF e corrigir inconsistências.

O erro que a reescrita precisa evitar é simples: o texto não pode parecer um TCC sobre Cascata/Piratininga com resultados novos de Sapo colados no final. O relatório deve nascer como um estudo de Sapo; todo o restante entra apenas como contexto técnico ou ablação auxiliar claramente identificada.
