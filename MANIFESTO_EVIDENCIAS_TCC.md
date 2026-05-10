# Manifesto de Evidencias do TCC

Este manifesto registra quais artefatos podem sustentar a escrita final do TCC. A regra de uso e: os resultados principais devem vir dos artefatos recentes e rastreaveis de 2026-05-10, sob o contrato `clean_pm10_decoder_proxy` com HPO walk-forward; resultados antigos entram apenas como historico ou estudo auxiliar.

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
| Data de consolidacao dos artefatos principais | `2026-05-10` |
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
| Dataset | `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/datasets/clean_pm10_decoder_proxy.parquet` |
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
| `../TCC-wsl/scripts/analysis/run_sapo_final_pre_delivery_suite.py` | Bateria principal final com HPO walk-forward, multi-seed, baselines e ablações | `CV_HPO_XGB_TRIALS=4 python scripts/analysis/run_sapo_final_pre_delivery_suite.py`; defaults principais: `CV_HPO_DL_TRIALS=24`, `CV_HPO_MAX_EPOCHS=18`, `CV_N_SPLITS=3`, `FINAL_SUITE_SEEDS=7,21,123`. |
| `../TCC-wsl/scripts/analysis/run_sapo_clean_pm10_hpo_all_models.py` | Bateria de 2026-05-09 com HPO simples; manter como histórico comparável | `python scripts/analysis/run_sapo_clean_pm10_hpo_all_models.py` com defaults do script. |
| `../TCC-wsl/scripts/analysis/run_seq2seq_weighted_l1_hpo.py` | HPO especifico do Seq2Seq attention com `weighted_l1` | `python scripts/analysis/run_seq2seq_weighted_l1_hpo.py` com defaults: `WEIGHTED_L1_HPO_TRIALS=18`, `WEIGHTED_L1_HPO_MAX_EPOCHS=14`, `WEIGHTED_L1_FINAL_MAX_EPOCHS=48`. |
| `../TCC-wsl/scripts/analysis/run_seq2seq_weighted_l1_final_ablation.py` | Ablacao final de seeds, lags e blends do `weighted_l1` | `python scripts/analysis/run_seq2seq_weighted_l1_final_ablation.py` com defaults: `FINAL_MAX_EPOCHS=48`, `REFINED_HPO_TRIALS=14`, `REFINED_HPO_MAX_EPOCHS=16`. |
| `../TCC-wsl/configs/data_source/cmd_sapo.yaml` | Fonte de dados e estacao principal | Sapo/CMD. |
| `../TCC-wsl/configs/experiment/seq_len_48x24_cmd_sapo_70_15_15.yaml` | Formula a tarefa | entrada 48h e saida 24h. |
| `../TCC-wsl/configs/period/cmd_sapo_2016_2020_ratio_70_15_15.yaml` | Periodo do benchmark fixo inicial | Usar como historico; conferir sempre contra o artefato final filtrado. |

## Artefatos Oficiais

| Artefato | Uso no TCC |
| --- | --- |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/cv_hpo_summary.csv` | Tabela principal do Capitulo 5 após HPO walk-forward. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/multi_seed_aggregate.csv` | Estabilidade multi-seed dos modelos selecionados. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/naive_baselines.csv` | Baselines ingênuos e skill score. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/pm10_causal_ablation.csv` | Ablação de PM10 causal. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/mask_imputation_ablation.csv` | Ablação de máscara/imputação. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/event_level_model_summary.csv` | Análise event-level de picos. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_hpo_vs_reference.csv` | Tabela historica de 2026-05-09; nao usar como resultado final se conflitar com a suite 2026-05-10. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_hpo_vs_reference.json` | Versao estruturada da tabela historica de 2026-05-09. |
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
| `cv_hpo_lstm_direct_clean_pm10` | ver `cv_hpo_summary.csv` | 2.7713 | 3.8346 | 23.01 | 0.5154 | 2.6725 | 2.8670 | 13.6112 | 28.57 | Vencedor por MAE no seed canonico. |
| `cv_hpo_weighted_l1_clean_pm10` | ver `cv_hpo_summary.csv` | 2.8658 | 3.9641 | 23.90 | 0.4821 | 2.7631 | 2.9695 | 12.3697 | 31.57 | Seq2Seq attention final; melhor amplitude que LSTM direct, sem vencer MAE. |
| `cv_hpo_xgboost_clean_pm10` | ver `cv_hpo_summary.csv` | 2.8786 | 3.9793 | 23.80 | 0.4781 | 2.5618 | 3.0273 | 12.2583 | 30.73 | Baseline tabular forte; melhor H1. |
| `cv_hpo_lstm_recursive_clean_pm10` | ver `cv_hpo_summary.csv` | 2.8876 | 3.8380 | 24.39 | 0.5146 | 2.7380 | 3.1492 | 12.0392 | 30.49 | Melhor RMSE/R2 medio multi-seed, mas MAE e vies piores. |

## Seq2Seq Attention com Weighted L1

| Variante | Run ID | MAE | RMSE | R2 | Peak35 MAE | p99 previsto | Leitura |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `cv_hpo_weighted_l1_clean_pm10` seed 42 | ver `cv_hpo_summary.csv` | 2.8658 | 3.9641 | 0.4821 | 12.3697 | 31.57 | Resultado final selecionado por walk-forward. |
| `cv_hpo_weighted_l1_clean_pm10` media multi-seed | ver `multi_seed_aggregate.csv` | 2.8646 | 3.9617 | 0.4827 | 13.1103 | 30.49 | Competitivo, mas abaixo da LSTM direct em MAE. |

## Figuras Exportadas

| Figura | Fonte | Uso no TCC |
| --- | --- | --- |
| `figuras/tarefa_48_24_sapo.png` | Gerada a partir da definicao do protocolo `48 -> 24`. | Capitulo 4, formulacao da tarefa. |
| `figuras/split_70_15_15_sapo.png` | Gerada a partir dos limites do artefato `clean_pm10_decoder_proxy`. | Capitulo 4, split cronologico. |
| `figuras/eda_ranking_estacoes_pm25_pm10.pdf` / `.png` | `../TCC-wsl/docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, fundamentacao da escolha de Sapo. |
| `figuras/eda_sapo_cobertura_lacunas.pdf` / `.png` | Artefato `clean_pm10_decoder_proxy`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, cobertura mensal e maiores lacunas de PM2.5. |
| `figuras/eda_sapo_distribuicao_pm25.pdf` / `.png` | Artefato `clean_pm10_decoder_proxy`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, distribuicao observada e eventos altos por split. |
| `figuras/erro_por_horizonte_sapo.png` | `per_horizon_metrics.csv` dos modelos da suite final 2026-05-10. | Capitulo 5, MAE por horizonte. |
| `figuras/predito_observado_pico_sapo.png` / `.pdf` | `test_predictions_timeline.csv` de LSTM direct, XGBoost e `cv_hpo_weighted_l1_clean_pm10`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 5, suavizacao e evento alto em paineis por modelo. |
| `figuras/diagrama_lstm_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base na formulacao da LSTM; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, celula LSTM e portoes. |
| `figuras/diagrama_seq2seq_attention_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base em Seq2Seq e mecanismos de atencao; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, encoder-decoder com atencao para tarefa 48 -> 24. |
| `figuras/diagrama_xgboost_multioutput_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base no baseline XGBoost multi-output; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, conversao de janela temporal para matriz tabular. |
| `figuras/perfil_medio_atencao_seq2seq.pdf` / `.png` | Pesos de atencao extraidos dos checkpoints finais; fonte em `scripts/gerar_figuras_atencao.py`. | Capitulo 5, perfil medio de atencao no encoder. |
| `figuras/heatmap_medio_atencao_weighted_l1.pdf` / `.png` | Pesos de atencao extraidos do checkpoint `weighted_l1_hpo_mae`; fonte em `scripts/gerar_figuras_atencao.py`. | Capitulo 5, heatmap medio por horizonte. |
| `figuras/diagnosticos_atencao_seq2seq.pdf` / `.png` | Diagnosticos agregados dos pesos de atencao; fonte em `scripts/gerar_figuras_atencao.py`. | Figura auxiliar; valores consolidados usados em tabela no Capitulo 5. |

## Regras de Uso na Escrita

- A tabela principal do TCC deve usar `runtime/reports/sapo_final_pre_delivery_suite_20260510/cv_hpo_summary.csv`.
- O benchmark `sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828` deve ser rotulado como historico, sem HPO e sem declarar vencedor final.
- O XGBoost pode ser comparado como baseline tabular forte, com a ressalva de que o treinamento multi-output exige janelas com horizonte completo observado.
- `weighted_l1` deve ser descrito como funcao de perda ponderada por regime/erro, nao como regularizacao L1.
- Blends devem ser apresentados como combinacoes de predicoes, nao como modelos individuais.
- Figuras finais foram selecionadas/exportadas e registradas neste manifesto.
