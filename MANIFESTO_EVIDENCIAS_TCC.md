# Manifesto de Evidencias do TCC

Este manifesto registra quais artefatos podem sustentar a escrita final do TCC. A regra de uso e: os resultados principais devem vir dos artefatos recentes e rastreaveis de 2026-05-09, sob o contrato `clean_pm10_decoder_proxy`; resultados antigos entram apenas como historico ou estudo auxiliar.

## Checklist do Manifesto

- [x] Contrato experimental principal identificado.
- [x] Dataset final, periodo, linhas e hash registrados.
- [x] Tabela principal com HPO registrada.
- [x] Tabelas do Seq2Seq `weighted_l1` registradas.
- [x] Comandos exatos de reproducao revisados em texto final.
- [x] Figuras finais exportadas e vinculadas aos Capitulos 4 e 5.
- [x] EDA comparativa de estacoes e EDA especifica de Sapo registradas no Capitulo 4.
- [x] Diagramas teoricos proprios de LSTM, Seq2Seq com atencao e XGBoost gerados e citados no Capitulo 2.
- [x] Diagramas proprios revisados para reduzir sobreposicao de setas e melhorar a leitura.
- [x] Pesos de atencao dos checkpoints finais extraidos e analisados no Capitulo 5.
- [x] PDF compilado depois da revisao final.

## Estado do Repositorio Tecnico

| Item | Valor |
| --- | --- |
| Repositorio tecnico | `../TCC-wsl` |
| Commit lido | `8d0458353c50b583735724587a896f8520307937` |
| Estado local | Arvore com modificacoes e arquivos nao rastreados em `TCC-wsl` no momento da leitura. |
| Data de consolidacao dos artefatos principais | `2026-05-09` |
| Observacao | O commit deve ser citado junto da ressalva de arvore suja se a versao final nao for congelada em novo commit. |

## Contrato Principal

| Campo | Valor |
| --- | --- |
| Nome do contrato | `clean_pm10_decoder_proxy` |
| Estacao | `Sapo` / CMD |
| Poluente-alvo | `PM2.5` horario |
| Tarefa | `48 -> 24` |
| Split | cronologico `70/15/15` |
| Imputacao | linear no dataset limpo atual |
| Mascara do alvo | alvo imputado fora de loss e metricas observadas quando a mascara esta disponivel |
| Dataset | `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/datasets/sapo_clean_pm10_decoder_proxy.parquet` |
| SHA-256 do dataset | `3f2f16c4d10420d9b534e722405180f61e86991dc6e888c14dffafbb85c32d17` |
| Periodo do artefato | `2017-01-04 00:30:00` a `2020-12-31 22:30:00` |
| Linhas | `34.991` |
| Colunas numericas | `29` |
| Missing PM2.5 | `19,264953845274498%` |
| Missing PM10 | `19,57646251893344%` |
| Variaveis centrais | `PM2.5`, `PM10`, `PM2.5__miss`, `PM10__miss`, tempo/Fourier, `PM10_proxy_exante`, `PM10_trend_exante` |

## Scripts e Configuracoes

| Evidencia | Papel | Comando/entrada registrada |
| --- | --- | --- |
| `../TCC-wsl/scripts/analysis/run_sapo_clean_pm10_hpo_all_models.py` | Bateria principal com HPO para 4 DL + XGBoost | `python scripts/analysis/run_sapo_clean_pm10_hpo_all_models.py` com defaults do script: `DL_HPO_TRIALS=10`, `XGB_HPO_TRIALS=12`, `HPO_MAX_EPOCHS=12`, `FINAL_MAX_EPOCHS=36`. |
| `../TCC-wsl/scripts/analysis/run_seq2seq_weighted_l1_hpo.py` | HPO especifico do Seq2Seq attention com `weighted_l1` | `python scripts/analysis/run_seq2seq_weighted_l1_hpo.py` com defaults: `WEIGHTED_L1_HPO_TRIALS=18`, `WEIGHTED_L1_HPO_MAX_EPOCHS=14`, `WEIGHTED_L1_FINAL_MAX_EPOCHS=48`. |
| `../TCC-wsl/scripts/analysis/run_seq2seq_weighted_l1_final_ablation.py` | Ablacao final de seeds, lags e blends do `weighted_l1` | `python scripts/analysis/run_seq2seq_weighted_l1_final_ablation.py` com defaults: `FINAL_MAX_EPOCHS=48`, `REFINED_HPO_TRIALS=14`, `REFINED_HPO_MAX_EPOCHS=16`. |
| `../TCC-wsl/configs/data_source/cmd_sapo.yaml` | Fonte de dados e estacao principal | Sapo/CMD. |
| `../TCC-wsl/configs/experiment/seq_len_48x24_cmd_sapo_70_15_15.yaml` | Formula a tarefa | entrada 48h e saida 24h. |
| `../TCC-wsl/configs/period/cmd_sapo_2016_2020_ratio_70_15_15.yaml` | Periodo do benchmark fixo inicial | Usar como historico; conferir sempre contra o artefato final filtrado. |

## Artefatos Oficiais

| Artefato | Uso no TCC |
| --- | --- |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_hpo_vs_reference.csv` | Tabela principal do Capitulo 5. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_hpo_vs_reference.json` | Versao estruturada da tabela principal. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_dataset_summary.json` | Periodo, linhas, colunas e missingness do dataset. |
| `../TCC-wsl/runtime/reports/seq2seq_weighted_l1_hpo_20260509/seq2seq_weighted_l1_hpo_summary.csv` | Melhor Seq2Seq attention individual com `weighted_l1`. |
| `../TCC-wsl/runtime/reports/seq2seq_weighted_l1_final_ablation_20260509/seq2seq_weighted_l1_final_ablation_summary.csv` | Seeds, lag24/lag48, blends e HPO refinado para cauda/picos. |
| `../TCC-wsl/docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv` | Ranking exploratorio usado para fundamentar a escolha da estacao Sapo. |
| `artefatos/eda_sapo_split_summary_tcc.csv` e `artefatos/eda_sapo_summary_tcc.json` | Cobertura, missingness, distribuicao e picos do artefato final Sapo por split. |
| `artefatos/eda_sapo_pm25_gaps_tcc.csv` | Maiores lacunas originais de PM2.5 no artefato Sapo. |
| `artefatos/eda_sapo_pm25_continuous_runs_tcc.csv` | Maiores blocos continuos observados de PM2.5 no artefato Sapo. |
| `artefatos/attention_summary_tcc.csv` e `artefatos/attention_summary_tcc.json` | Diagnosticos agregados dos pesos de atencao extraidos dos checkpoints finais. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.csv` | Benchmark fixo inicial sem HPO; usar apenas como historico. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.md` | Resumo legivel do benchmark fixo inicial; usar apenas como historico. |

## Resultado Principal Atual

| Modelo | Run ID | MAE | RMSE | MAPE | R2 | H1 MAE | H24 MAE | Peak35 MAE | p99 previsto | Leitura |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `lstm_direct_clean_pm10_hpo` | `b159712f4f544901970eedfc02cb3c08` | 2.7807 | 3.8861 | 22.84 | 0.5023 | 2.6605 | 2.8906 | 13.6841 | 28.92 | Vencedor global atual por MAE/RMSE/R2. |
| `xgboost_clean_pm10_hpo` | `bb27821ba0b74357af18c67782088888` | 2.8655 | 3.9340 | 23.88 | 0.4900 | 2.4486 | 3.0129 | 13.0208 | 29.97 | Baseline tabular forte; nao e mais vencedor global. |
| `seq2seq_attention_clean_pm10_hpo` | `166e7cd1d95e4503bbf2cf44182174f2` | 2.8811 | 3.9859 | 23.79 | 0.4764 | 2.7155 | 2.9743 | 14.7027 | 29.13 | Attention canonico com HPO ficou competitivo, mas abaixo do LSTM direct. |
| `seq2seq_basic_clean_pm10_hpo` | `75ac9e207c1546eda37059eabdc79386` | 2.9553 | 4.0967 | 23.99 | 0.4469 | 2.6519 | 3.1514 | 12.9806 | 30.65 | Baseline encoder-decoder simples, inferior ao attention e ao XGBoost. |
| `lstm_recursive_clean_pm10_hpo` | `2f7ab74071a64991bed1fc08665cc236` | 2.9818 | 3.9363 | 25.45 | 0.4894 | 2.7567 | 3.2312 | 10.9772 | 31.94 | Melhor comportamento em picos, mas pior MAE e vies positivo. |

## Seq2Seq Attention com Weighted L1

| Variante | Run ID | MAE | RMSE | R2 | Peak35 MAE | p99 previsto | Leitura |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `weighted_l1_hpo_mae` | `eb94b33d27484a20ad509492ebeb6b5d` | 2.8358 | 3.9026 | 0.4981 | 12.4871 | 30.60 | Melhor Seq2Seq attention individual; supera XGBoost em MAE, mas nao LSTM direct. |
| `weighted_l1_lag24_only` | `62a53474214e4fa4bf849c9403b56664` | 2.8579 | 3.9341 | 0.4899 | 11.9571 | 31.48 | Melhor trade-off de cauda/picos com perda pequena de MAE global. |
| `weighted_l1_seed_21` | `0c0a9f9fa3a94b35985abbd02ae06b57` | 2.8428 | 3.9413 | 0.4881 | 12.6911 | 30.70 | Evidencia de robustez parcial. |
| `weighted_l1_seed_123` | `6097a133fab64b6da4db88b80799a946` | 2.8392 | 3.9141 | 0.4951 | 12.8550 | 30.16 | Evidencia de robustez parcial. |
| `weighted_l1_seed_7` | `fcd0ad2d021146d8a6e2bc04be1d4f97` | 2.8958 | 3.9690 | 0.4808 | 12.9048 | 30.61 | Mostra sensibilidade a seed. |
| `blend_hpo70_tiny30` | combinacao de predicoes | 2.8311 | 3.9071 | 0.4969 | 12.3516 | 30.90 | Melhor combinacao Seq2Seq por predicao; relatar como ensemble, nao como modelo unico. |

## Figuras Exportadas

| Figura | Fonte | Uso no TCC |
| --- | --- | --- |
| `figuras/tarefa_48_24_sapo.png` | Gerada a partir da definicao do protocolo `48 -> 24`. | Capitulo 4, formulacao da tarefa. |
| `figuras/split_70_15_15_sapo.png` | Gerada a partir dos limites do artefato `clean_pm10_decoder_proxy`. | Capitulo 4, split cronologico. |
| `figuras/eda_ranking_estacoes_pm25_pm10.pdf` / `.png` | `../TCC-wsl/docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, fundamentacao da escolha de Sapo. |
| `figuras/eda_sapo_cobertura_lacunas.pdf` / `.png` | Artefato `clean_pm10_decoder_proxy`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, cobertura mensal e maiores lacunas de PM2.5. |
| `figuras/eda_sapo_distribuicao_pm25.pdf` / `.png` | Artefato `clean_pm10_decoder_proxy`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, distribuicao observada e eventos altos por split. |
| `figuras/erro_por_horizonte_sapo.png` | `per_horizon_metrics.csv` dos cinco modelos da bateria principal. | Capitulo 5, MAE por horizonte. |
| `figuras/predito_observado_pico_sapo.png` / `.pdf` | `test_predictions_timeline.csv` de LSTM direct, XGBoost e `weighted_l1_hpo_mae`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 5, suavizacao e evento alto em paineis por modelo. |
| `figuras/diagrama_lstm_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base na formulacao da LSTM; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, celula LSTM e portoes. |
| `figuras/diagrama_seq2seq_attention_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base em Seq2Seq e mecanismos de atencao; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, encoder-decoder com atencao para tarefa 48 -> 24. |
| `figuras/diagrama_xgboost_multioutput_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base no baseline XGBoost multi-output; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, conversao de janela temporal para matriz tabular. |
| `figuras/perfil_medio_atencao_seq2seq.pdf` / `.png` | Pesos de atencao extraidos dos checkpoints finais; fonte em `scripts/gerar_figuras_atencao.py`. | Capitulo 5, perfil medio de atencao no encoder. |
| `figuras/heatmap_medio_atencao_weighted_l1.pdf` / `.png` | Pesos de atencao extraidos do checkpoint `weighted_l1_hpo_mae`; fonte em `scripts/gerar_figuras_atencao.py`. | Capitulo 5, heatmap medio por horizonte. |
| `figuras/diagnosticos_atencao_seq2seq.pdf` / `.png` | Diagnosticos agregados dos pesos de atencao; fonte em `scripts/gerar_figuras_atencao.py`. | Figura auxiliar; valores consolidados usados em tabela no Capitulo 5. |

## Regras de Uso na Escrita

- A tabela principal do TCC deve usar `sapo_clean_pm10_hpo_vs_reference.csv`.
- O benchmark `sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828` deve ser rotulado como historico, sem HPO e sem declarar vencedor final.
- O XGBoost pode ser comparado como baseline tabular forte, com a ressalva de que o treinamento multi-output exige janelas com horizonte completo observado.
- `weighted_l1` deve ser descrito como funcao de perda ponderada por regime/erro, nao como regularizacao L1.
- Blends devem ser apresentados como combinacoes de predicoes, nao como modelos individuais.
- Figuras finais foram selecionadas/exportadas e registradas neste manifesto.
