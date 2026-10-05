# Manifesto de Evidencias do TCC

Este manifesto registra quais artefatos podem sustentar a escrita final do TCC. Regra: **todos os resultados numericos do Capitulo 5 vem do protocolo unificado** (`../TCC-wsl/scripts/thesis/`), executado uma unica vez sobre um commit congelado e tabulado por `scripts/thesis/analyze.py`. Resultados de campanhas anteriores sao historicos e nao sustentam nenhuma conclusao.

## Checklist do Manifesto

- [ ] Commit do repositorio tecnico congelado, com arvore limpa, e citado abaixo.
- [ ] Protocolo executado por completo (`plan` conferido; `datasets`, `hpo`, `final` e `baselines` para todos os grupos).
- [ ] Tabelas e figuras geradas por `python -m scripts.thesis.analyze --latex-dir ../TCC-RELATORIO/tex/tabelas`.
- [ ] Contraprova de atencao executada (`python -m scripts.thesis.attention_counterfactual`).
- [ ] Nenhum `\aserpreenchido` restante no PDF (`grep PREENCHER` no texto extraido deve retornar vazio).
- [ ] Hash do CSV bruto e do dataset conferidos com `runtime/reports/thesis_protocol/datasets/*.json`.
- [ ] PDF compilado depois da revisao final.

## Estado do Repositorio Tecnico

| Item | Valor |
| --- | --- |
| Repositorio tecnico | `../TCC-wsl` |
| Commit executado | _preencher com `git rev-parse HEAD` (tambem gravado em `runtime/reports/thesis_protocol/manifest.json`)_ |
| Arvore limpa | _preencher (`git.dirty` no `manifest.json` deve ser `false`)_ |
| Ambiente | versoes registradas em `manifest.json` (`environment`) |

## Contrato Principal

| Campo | Valor |
| --- | --- |
| Nome do contrato | `clean_pm10_decoder_proxy` |
| Estacao | `Sapo` / CMD |
| Poluente-alvo | `PM2.5` horario |
| Tarefa | `48 -> 24` |
| Split | por datas: treino ate 2019-10-21 14:30; validacao ate 2020-05-27 06:30; teste historico 2020-05-27..2020-12-31; holdout 2021-01-01..2023-12-31 |
| Imputacao | linear no treino, propagacao apos o corte; refeita por dobra na HPO |
| Mascara do alvo | alvo imputado fora de perda e metricas |
| Dataset | `../TCC-wsl/runtime/reports/thesis_protocol/datasets/clean_pm10_decoder_proxy.parquet` |
| Periodo do dataset | `2017-01-04 00:30:00` a `2023-12-31 22:30:00`; 61.271 linhas (as 34.991 primeiras coincidem com o conjunto das campanhas anteriores) |
| SHA-256 do dataset e do CSV bruto | _preencher com `datasets/clean_pm10_decoder_proxy.json`_ |
| Variaveis centrais | `PM2.5`, `PM10`, `PM2.5__miss`, `PM10__miss`, tempo/Fourier, `PM10_proxy_exante`, `PM10_trend_exante` |

## Scripts e Configuracoes

| Evidencia | Papel | Comando/entrada |
| --- | --- | --- |
| `../TCC-wsl/configs/thesis_protocol.yaml` | Protocolo de treino unico para todos os modelos | verificado por `tests/test_thesis_protocol.py` |
| `../TCC-wsl/scripts/thesis/protocol.py` | Casos experimentais e espacos de busca; tabela "igual x diferente" | `python -m scripts.thesis.run_protocol plan` |
| `../TCC-wsl/scripts/thesis/run_protocol.py` | Datasets, HPO walk-forward, treino final (4 sementes na comparação principal, 3 nos fatores), baselines | `python -m scripts.thesis.run_protocol all --group primary loss extras design_ablation pm10_ablation` |
| `../TCC-wsl/scripts/thesis/analyze.py` | Metricas, bootstrap em blocos, Diebold-Mariano, eventos, dinamica, ensemble, vitorias, fatorial, ablacoes, LaTeX | `python -m scripts.thesis.analyze --latex-dir ../TCC-RELATORIO/tex/tabelas` |
| `../TCC-wsl/scripts/thesis/attention_counterfactual.py` | Contraprova da atencao aprendida | `python -m scripts.thesis.attention_counterfactual --case seq2seq_attention_new__huber` |
| `../TCC-wsl/src/data/thesis_dataset.py` | Construcao do dataset a partir do CSV bruto com corte explicito | testes em `tests/test_thesis_dataset.py` |
| `../TCC-wsl/src/evaluation/` | Metricas (WAPE, sMAPE, cauda) e estatistica | testes em `tests/test_evaluation_*.py` |
| `../TCC-wsl/docs/PROTOCOLO_EXPERIMENTAL.md` | Descricao completa do protocolo | — |

## Artefatos Oficiais (gerados pelo protocolo)

| Artefato | Uso no TCC |
| --- | --- |
| `runtime/reports/thesis_protocol/manifest.json` | Commit, ambiente, casos e configuracao efetivamente usados. |
| `runtime/reports/thesis_protocol/hpo/*.json` | Hiperparametros selecionados e orcamento de cada HPO. |
| `runtime/reports/thesis_protocol/runs/<caso>/seed_<n>/summary.json` | Metricas, hiperparametros, epoca do melhor ponto de controle, hash do dataset. |
| `runtime/reports/thesis_protocol/runs/<caso>/seed_<n>/test_predictions_window_level.csv` | Previsoes por janela e horizonte (base de todas as tabelas). |
| `runtime/reports/thesis_protocol/tables/*.csv` e `*.tex` | Tabelas do Capitulo 5 (copiadas para `tex/tabelas/`). |
| `runtime/reports/thesis_protocol/tables/summary.md` | Resumo legivel de todas as tabelas. |

## Artefatos Historicos (nao sustentam conclusoes)

| Artefato | Observacao |
| --- | --- |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/` e `sapo_final_new_seq2seq_suite_20260522/` | Campanha anterior: protocolos de treino diferentes entre modelos e variante do Seq2Seq escolhida olhando o teste historico. Produzidas pelos scripts em `../TCC-wsl/scripts/legacy/`. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/`, `seq2seq_weighted_l1_*` | Rodadas exploratorias de HPO e ablacoes. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.*` | Benchmark fixo inicial sem HPO. |
| `../TCC-wsl/runtime/reports/station_lstm_seq2seq_feature_transfer_20260510/` | Diagnosticos `oracle future aux` e Seq2Seq multialvo (Secao "Diagnosticos com Variaveis Futuras"); nao reexecutados no protocolo unificado. |
| `artefatos/attention_*_tcc.*`, `figuras/perfil_medio_atencao_seq2seq.*`, `figuras/heatmap_medio_atencao_weighted_l1.*`, `figuras/diagnosticos_atencao_seq2seq.*` | Pesos de atencao de checkpoints antigos; nao usados na narrativa. |

## Artefatos de Apoio Ainda Validos (EDA)

| Artefato | Uso no TCC |
| --- | --- |
| `../TCC-wsl/docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv` | Ranking exploratorio usado para justificar a escolha da estacao Sapo. |
| `artefatos/eda_sapo_*` | Cobertura, lacunas e distribuicao do recorte de desenvolvimento (2017-2020). |
| `artefatos/analise_janela_entrada_sapo.md` | Justificativa da janela de 48 h. |
| `figuras/eda_*.pdf`, `figuras/serie_temporal_componentes_sapo.pdf` | Figuras do Capitulo 4 (recorte 2017-2020). |
| `figuras/tarefa_48_24_sapo.png` | Formulacao da tarefa. |

## Figuras dos Capitulos 2 e 4 (elaboracao propria)

Diagramas de neuronio, LSTM, Seq2Seq com atencao, XGBoost por horizonte, *teacher forcing* e validacao *walk-forward* sao figuras conceituais geradas por `scripts/gerar_*.py`; a divisao cronologica do Capitulo 4 agora e um desenho TikZ no proprio `.tex`.

## Regras de Uso na Escrita

- Nenhum numero do Capitulo 5 e digitado a mao: vem de `\inputtabela`/`\figuragerada`; a prosa cita as tabelas.
- Resultado do teste historico e do holdout sao sempre reportados separadamente; so o holdout e confirmatorio.
- O XGBoost e a Ridge sao treinados por horizonte (estrategia direta), cada um com todas as janelas cujo alvo naquele horizonte foi observado, a mesma regra de mascara das redes; usam objetivo de erro absoluto e parada antecipada nativa. A versao multi-saida anterior descartava ~70% das janelas de treino e foi abandonada.
- `weighted_l1` e uma funcao de perda absoluta ponderada por regime (decisao de projeto), nao regularizacao L1; e um fator aplicado a todas as arquiteturas neurais.
- Afirmacoes de diferenca entre modelos exigem o veredito do bootstrap em blocos; diferencas cujo intervalo contem zero sao descritas como empate estatistico.
- Nao afirmar que um modelo "entende a dinamica" sem suporte nas medidas de dinamica horaria (correlacao das diferencas, acerto de direcao).
