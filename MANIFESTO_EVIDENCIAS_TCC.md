# Manifesto de Evidencias do TCC

Este manifesto registra quais artefatos podem sustentar a escrita final do TCC. A regra de uso e: os resultados principais devem vir da suite final de 2026-05-22, sob o contrato `clean_pm10_decoder_proxy`, tarefa 48 -> 24 e mesmas sementes; resultados antigos entram apenas como historico ou estudo auxiliar.

## Checklist do Manifesto

- [x] Contrato experimental principal identificado.
- [x] Dataset final, periodo, linhas e hash registrados.
- [x] Tabela principal com HPO registrada.
- [x] Tabelas do novo Seq2Seq attention registradas.
- [x] Comandos exatos de reproducao revisados em texto final.
- [x] Figuras finais exportadas e vinculadas aos Capitulos 4 e 5.
- [x] EDA comparativa de estacoes e EDA especifica de Sapo registradas no Capitulo 4.
- [x] Diagramas teoricos proprios de LSTM, Seq2Seq com atencao e XGBoost gerados e citados no Capitulo 2.
- [x] Diagramas proprios revisados para reduzir sobreposicao de setas e melhorar a leitura.
- [x] Pesos de atencao dos checkpoints finais extraidos e analisados no Capitulo 5.
- [x] Experimentos diagnosticos `oracle future aux` e Seq2Seq multi-alvo adicionados como limite informacional.
- [x] PDF compilado depois da revisao final.

## Estado do Repositorio Tecnico

| Item | Valor |
| --- | --- |
| Repositorio tecnico | `../TCC-wsl` |
| Commit lido | `8d0458353c50b583735724587a896f8520307937` |
| Estado local | Arvore com modificacoes e arquivos nao rastreados em `TCC-wsl` no momento da leitura. |
| Data de consolidacao dos artefatos principais | `2026-05-22` |
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
| `../TCC-wsl/scripts/analysis/run_sapo_final_new_seq2seq_suite.py` | Suite final comparavel com novo Seq2Seq attention, seis modelos e quatro sementes | `python scripts/analysis/run_sapo_final_new_seq2seq_suite.py --run-all --max-parallel 2`; executa `seq2seq_*` de forma exclusiva na GPU e consolida `final_model_*`. |
| `../TCC-wsl/scripts/analysis/run_sapo_window_seq2seq_ablation.py` | Ablacao de janela de entrada e comparacao do novo Seq2Seq contra `weighted_l1` antigo | Usado para justificar manter 48h e substituir o Seq2Seq antigo. |
| `../TCC-wsl/scripts/analysis/run_sapo_clean_pm10_hpo_all_models.py` | Bateria de 2026-05-09 com HPO simples; manter como histórico comparável | `python scripts/analysis/run_sapo_clean_pm10_hpo_all_models.py` com defaults do script. |
| `../TCC-wsl/scripts/analysis/run_seq2seq_weighted_l1_hpo.py` | HPO especifico do Seq2Seq attention com `weighted_l1` | `python scripts/analysis/run_seq2seq_weighted_l1_hpo.py` com defaults: `WEIGHTED_L1_HPO_TRIALS=18`, `WEIGHTED_L1_HPO_MAX_EPOCHS=14`, `WEIGHTED_L1_FINAL_MAX_EPOCHS=48`. |
| `../TCC-wsl/scripts/analysis/run_seq2seq_weighted_l1_final_ablation.py` | Ablacao final de seeds, lags e blends do `weighted_l1` | `python scripts/analysis/run_seq2seq_weighted_l1_final_ablation.py` com defaults: `FINAL_MAX_EPOCHS=48`, `REFINED_HPO_TRIALS=14`, `REFINED_HPO_MAX_EPOCHS=16`. |
| `../TCC-wsl/scripts/analysis/run_station_lstm_seq2seq_feature_transfer.py` | Diagnosticos auxiliares por dataset/estacao, incluindo `oracle future aux` e Seq2Seq multi-alvo em Sapo. | Usado como estudo auxiliar; nao substitui a suite principal `clean_pm10_decoder_proxy`. |
| `../TCC-wsl/configs/data_source/cmd_sapo.yaml` | Fonte de dados e estacao principal | Sapo/CMD. |
| `../TCC-wsl/configs/experiment/seq_len_48x24_cmd_sapo_70_15_15.yaml` | Formula a tarefa | entrada 48h e saida 24h. |
| `../TCC-wsl/configs/period/cmd_sapo_2016_2020_ratio_70_15_15.yaml` | Periodo do benchmark fixo inicial | Usar como historico; conferir sempre contra o artefato final filtrado. |

## Artefatos Oficiais

| Artefato | Uso no TCC |
| --- | --- |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/cv_hpo_summary.csv` | Tabela principal do Capitulo 5 após HPO walk-forward. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/multi_seed_aggregate.csv` | Estabilidade multi-seed dos modelos selecionados. |
| `../TCC-wsl/runtime/reports/sapo_final_new_seq2seq_suite_20260522/final_model_seed42_ranking.csv` | Tabela principal atualizada com novo Seq2Seq e seis modelos preenchidos. |
| `../TCC-wsl/runtime/reports/sapo_final_new_seq2seq_suite_20260522/final_model_aggregate.csv` | Estabilidade multi-seed atualizada com novo Seq2Seq. |
| `../TCC-wsl/runtime/reports/sapo_final_new_seq2seq_suite_20260522/event_level_model_summary.csv` | Analise event-level atualizada; novo Seq2Seq vence eventos altos. |
| `artefatos/resultados_sapo_final_novo_seq2seq.md` | Resumo textual dos resultados finais de 2026-05-22 para apoio ao Capitulo 5 e Conclusao. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/naive_baselines.csv` | Baselines ingênuos e skill score. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/pm10_causal_ablation.csv` | Ablação de PM10 causal. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/mask_imputation_ablation.csv` | Ablação de máscara/imputação. |
| `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/event_level_model_summary.csv` | Análise event-level de picos. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_hpo_vs_reference.csv` | Tabela historica de 2026-05-09; nao usar como resultado final se conflitar com a suite 2026-05-10. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_hpo_vs_reference.json` | Versao estruturada da tabela historica de 2026-05-09. |
| `../TCC-wsl/runtime/reports/sapo_clean_pm10_hpo_all_models_20260509/sapo_clean_pm10_dataset_summary.json` | Periodo, linhas, colunas e missingness do dataset. |
| `../TCC-wsl/runtime/reports/seq2seq_weighted_l1_hpo_20260509/seq2seq_weighted_l1_hpo_summary.csv` | Melhor Seq2Seq attention individual com `weighted_l1`. |
| `../TCC-wsl/runtime/reports/seq2seq_weighted_l1_final_ablation_20260509/seq2seq_weighted_l1_final_ablation_summary.csv` | Seeds, lag24/lag48, blends e HPO refinado para cauda/picos. |
| `../TCC-wsl/runtime/reports/station_lstm_seq2seq_feature_transfer_20260510/cmd_sapo_hourly_pm10_seq2seq_winner_oracle_future_mon_rmse_48x24/summary.json` | Diagnostico oracle com PM10 futuro real em Sapo. |
| `../TCC-wsl/runtime/reports/station_lstm_seq2seq_feature_transfer_20260510/cmd_sapo_hourly_all_context_seq2seq_winner_oracle_future_mon_rmse_48x24/summary.json` | Diagnostico oracle com PM10 + PTS futuros reais em Sapo. |
| `../TCC-wsl/runtime/reports/station_lstm_seq2seq_feature_transfer_20260510/cmd_sapo_hourly_all_context_seq2seq_winner_multitarget_aux128_mon_rmse_48x24/summary.json` | Melhor diagnostico Seq2Seq multi-alvo com PM10 e PTS como tarefas auxiliares. |
| `../TCC-wsl/docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv` | Ranking exploratorio usado para fundamentar a escolha da estacao Sapo. |
| `artefatos/eda_sapo_split_summary_tcc.csv` e `artefatos/eda_sapo_summary_tcc.json` | Cobertura, missingness, distribuicao e picos do artefato final Sapo por split. |
| `artefatos/eda_sapo_pm25_gaps_tcc.csv` | Maiores lacunas originais de PM2.5 no artefato Sapo. |
| `artefatos/eda_sapo_pm25_continuous_runs_tcc.csv` | Maiores blocos continuos observados de PM2.5 no artefato Sapo. |
| `artefatos/analise_janela_entrada_sapo.md` e `../TCC-wsl/runtime/reports/sapo_input_window_analysis_20260522/` | Analise auxiliar de persistencia e tamanho de janela para justificar o protocolo 48 -> 24. |
| `artefatos/attention_summary_tcc.csv` e `artefatos/attention_summary_tcc.json` | Diagnosticos agregados dos pesos de atencao extraidos dos checkpoints finais. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.csv` | Benchmark fixo inicial sem HPO; usar apenas como historico. |
| `../TCC-wsl/results/reports/sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828.md` | Resumo legivel do benchmark fixo inicial; usar apenas como historico. |

## Resultado Principal Atual

| Modelo | Run ID | MAE | RMSE | MAPE | R2 | H1 MAE | H24 MAE | Peak35 MAE | p99 previsto | Leitura |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `lstm_direct_clean_pm10_final_seed_42` | ver `final_model_seed42_ranking.csv` | 2.7713 | 3.8346 | 23.01 | 0.5154 | 2.6725 | 2.8670 | 13.6112 | 28.57 | Vencedor por MAE no seed canonico. |
| `seq2seq_attention_new_clean_pm10_final_seed_42` | ver `final_model_seed42_ranking.csv` | 2.8132 | 3.8799 | 23.23 | 0.5039 | 2.6222 | 2.9138 | 11.0815 | 32.50 | Melhor compromisso para picos; substitui `weighted_l1` antigo. |
| `xgboost_clean_pm10_final_seed_42` | ver `final_model_seed42_ranking.csv` | 2.8786 | 3.9793 | 23.80 | 0.4781 | 2.5618 | 3.0273 | 12.2583 | 30.73 | Referência baseada em árvores; melhor H1. |
| `seq2seq_attention_canonical_clean_pm10_final_seed_42` | ver `final_model_seed42_ranking.csv` | 2.8811 | 3.9859 | 23.79 | 0.4764 | 2.7155 | 2.9743 | 14.7027 | 29.13 | Referencia Seq2Seq attention canônica. |
| `lstm_recursive_clean_pm10_final_seed_42` | ver `final_model_seed42_ranking.csv` | 2.8876 | 3.8380 | 24.39 | 0.5146 | 2.7380 | 3.1492 | 12.0392 | 30.49 | Melhor RMSE/R2 medio multi-seed, mas MAE e vies piores. |
| `seq2seq_basic_clean_pm10_final_seed_42` | ver `final_model_seed42_ranking.csv` | 2.9553 | 4.0967 | 23.99 | 0.4469 | 2.6519 | 3.1514 | 12.9806 | 30.65 | Linha de base encoder-decoder sem atencao. |

## Novo Seq2Seq Attention

| Variante | Run ID | MAE | RMSE | R2 | Peak35 MAE | p99 previsto | Leitura |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| `seq2seq_attention_new_clean_pm10_final_seed_42` | ver `final_model_seed42_ranking.csv` | 2.8132 | 3.8799 | 0.5039 | 11.0815 | 32.50 | Melhor Seq2Seq individual; melhora MAE e picos contra `weighted_l1` antigo. |
| `seq2seq_attention_new_clean_pm10_final` media multi-seed | ver `final_model_aggregate.csv` | 2.8218 | 3.8989 | 0.4989 | 11.5855 | 31.90 | Segundo melhor MAE medio e melhor comportamento de picos. |

## Diagnosticos de Limite Informacional

| Experimento auxiliar | MAE | RMSE | R2 | Peak35 MAE | Leitura |
| --- | ---: | ---: | ---: | ---: | --- |
| PM10 causal Seq2Seq | 2.7777 | 3.9131 | 0.4954 | 10.2406 | Controle causal PM10-only no diagnostico. |
| PM10 + PTS causal Seq2Seq | 2.8758 | 3.9949 | 0.4741 | 10.5980 | Controle all-context util em Sapo; meteo/gases muito esparsos ficaram fora. |
| PM10 futuro real (`oracle`) | 2.4201 | 3.2659 | 0.6485 | 7.9835 | Mostra que PM10 futuro carrega informacao relevante, mas usa vazamento controlado. |
| PM10 + PTS futuro real (`oracle`) | 2.4223 | 3.2654 | 0.6486 | 7.1718 | Melhor pico no oracle; ainda distante de R2 proximo de 1. |
| Melhor Seq2Seq multi-alvo PM10+PTS | 2.7689 | 3.9373 | 0.4891 | 11.3975 | Aprendizagem auxiliar melhora MAE/R2 contra all-context causal, mas nao reproduz o ganho oracle. |

## Figuras Exportadas

| Figura | Fonte | Uso no TCC |
| --- | --- | --- |
| `figuras/tarefa_48_24_sapo.png` | Gerada a partir da definicao do protocolo `48 -> 24`. | Capitulo 4, formulacao da tarefa. |
| `figuras/split_70_15_15_sapo.png` | Gerada a partir dos limites do artefato `clean_pm10_decoder_proxy`. | Capitulo 4, split cronologico. |
| `figuras/eda_ranking_estacoes_pm25_pm10.pdf` / `.png` | `../TCC-wsl/docs/generated/eda_outras_usinas/metricas/usina_pm25_resumo_ranking.csv`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, fundamentacao da escolha de Sapo. |
| `figuras/eda_sapo_cobertura_lacunas.pdf` / `.png` | Artefato `clean_pm10_decoder_proxy`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, cobertura mensal e maiores lacunas de PM2.5. |
| `figuras/eda_sapo_distribuicao_pm25.pdf` / `.png` | Artefato `clean_pm10_decoder_proxy`; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 4, distribuicao observada e eventos altos por split. |
| `figuras/erro_por_horizonte_sapo.png` / `.pdf` | `per_horizon_metrics.csv` dos modelos da suite final 2026-05-22; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 5, MAE por horizonte. |
| `figuras/predito_observado_pico_sapo.png` / `.pdf` | `test_predictions_timeline.csv` dos modelos seed 42 da suite final 2026-05-22; fonte em `scripts/gerar_figuras_eda_sapo.py`. | Capitulo 5, suavizacao e evento alto em paineis por modelo. |
| `figuras/artificial_neuron_model_chrislb_wikimedia.png` | Imagem do modelo de neurônio artificial de Chrislb no Wikimedia Commons, citada em `referencias.bib`. | Capitulo 2, analogia entre neuronio biologico e artificial. |
| `figuras/lstm_fdeloche_wikimedia.png` | Imagem da celula LSTM de fdeloche no Wikimedia Commons, citada em `referencias.bib`. | Capitulo 2, celula LSTM e portoes. |
| `figuras/diagrama_seq2seq_attention_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base em Seq2Seq e mecanismos de atencao; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, encoder-decoder com atencao para tarefa 48 -> 24. |
| `figuras/teacher_forcing_regimes.pdf` / `.png` | Elaboracao propria gerada por `scripts/gerar_figuras_fundamentacao.py`, com base em Bengio et al. (2015). | Capitulo 2, regimes de realimentacao no decodificador. |
| `figuras/teacher_forcing_agendas.pdf` / `.png` | Elaboracao propria gerada por `scripts/gerar_figuras_fundamentacao.py`, com base em Bengio et al. (2015) e Teutsch e Mäder (2022). | Capitulo 2, direcoes esquematicas de agenda de teacher forcing; nao representa hiperparametros ou resultados do experimento. |
| `figuras/diagrama_xgboost_multioutput_proprio.pdf` / `.png` | Elaboracao propria redesenhada com base no XGBoost multi-output; fonte em `scripts/gerar_diagramas_modelos.py`. | Capitulo 2, conversao de janela temporal para vetor de atributos. |
| `figuras/perfil_medio_atencao_seq2seq.pdf` / `.png` | Pesos de atencao extraidos dos checkpoints anteriores; fonte em `scripts/gerar_figuras_atencao.py`. | Figura auxiliar historica; nao sustenta a conclusao final do novo Seq2Seq. |
| `figuras/heatmap_medio_atencao_weighted_l1.pdf` / `.png` | Pesos de atencao extraidos do checkpoint `weighted_l1_hpo_mae`; fonte em `scripts/gerar_figuras_atencao.py`. | Figura auxiliar historica; removida da narrativa principal atualizada. |
| `figuras/diagnosticos_atencao_seq2seq.pdf` / `.png` | Diagnosticos agregados dos pesos de atencao; fonte em `scripts/gerar_figuras_atencao.py`. | Figura auxiliar; a conclusao final usa metricas de erro, cauda e eventos. |

## Regras de Uso na Escrita

- A tabela principal do TCC deve usar `runtime/reports/sapo_final_new_seq2seq_suite_20260522/final_model_seed42_ranking.csv`.
- A tabela multi-seed deve usar `runtime/reports/sapo_final_new_seq2seq_suite_20260522/final_model_aggregate.csv`.
- O benchmark `sapo_70_15_15_4dl_xgb_multi_resume_20260507_215828` deve ser rotulado como historico, sem HPO e sem declarar vencedor final.
- O XGBoost pode ser comparado como referência baseada em árvores, com a ressalva de que o treinamento multi-output exige janelas com horizonte completo observado.
- `weighted_l1` deve ser descrito como funcao de perda ponderada por regime/erro, nao como regularizacao L1; no texto final, ela entra dentro da nova variante Seq2Seq, nao como modelo final separado.
- Blends devem ser apresentados como combinacoes de predicoes, nao como modelos individuais.
- Figuras finais foram selecionadas/exportadas e registradas neste manifesto.
