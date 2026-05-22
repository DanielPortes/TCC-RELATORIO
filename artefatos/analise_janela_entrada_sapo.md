# Analise da janela de entrada em Sapo

Artefato tecnico: `../TCC-wsl/runtime/reports/sapo_input_window_analysis_20260522/`

Dataset usado: `../TCC-wsl/runtime/reports/sapo_final_pre_delivery_suite_20260510/datasets/clean_pm10_decoder_proxy.parquet`

## Resultado sintetico

A serie de PM2,5 da estacao Sapo apresenta persistencia de curto prazo e repeticao diaria clara. A autocorrelacao observada foi:

| Defasagem | Autocorrelacao PM2,5 |
| --- | ---: |
| 1h | 0,813 |
| 24h | 0,681 |
| 48h | 0,598 |
| 168h | 0,461 |

Na comparacao comum de janelas que permite ate 168h de historico, a melhor linha de base simples foi a media movel de 24h, com MAE 3,0306 no teste. A media movel de 48h piorou para MAE 3,1157, e a media movel de 168h piorou para MAE 3,3714.

Nos modelos lineares diagnosticos, avaliados apenas para estudar o efeito do tamanho do historico, o resultado tambem nao indicou ganho por ampliar a entrada alem do ciclo diario:

| Diagnostico | 24h | 48h | 168h |
| --- | ---: | ---: | ---: |
| Ridge PM2,5 + tempo | 2,7635 | 2,7672 | 2,8239 |
| Ridge com PM10 causal do contrato | 2,7657 | 2,7851 | 2,8413 |

Esses numeros nao substituem a comparacao principal com HPO e modelos finais, porque usam um modelo linear leve e um subconjunto comum de janelas com suporte a 168h. A leitura metodologica e que 24h ja capturam a maior parte do sinal diario, enquanto 48h continuam defensaveis por preservar dois ciclos diarios e permitir usar defasagens de 24 e 48 horas sob o mesmo protocolo. Nao houve evidencia simples de que uma entrada semanal de 168h seja necessaria como configuracao principal.

## Texto curto reaproveitavel

A escolha de 48 horas de entrada nao foi tratada apenas como convencao arbitraria. A analise de persistencia no artefato final de Sapo mostrou autocorrelacao elevada em uma hora e repeticao diaria relevante em 24 horas, enquanto modelos diagnosticos leves nao apresentaram ganho consistente ao ampliar a entrada para 168 horas. Uma janela de 24 horas ja captura a maior parte do padrao diario; a janela de 48 horas foi mantida por preservar dois ciclos completos, permitir defasagens de 24 e 48 horas no mesmo protocolo e manter custo computacional controlado. Assim, o desenho 48 -> 24 funciona como compromisso metodologico para a comparacao principal, nao como prova de otimalidade universal da janela.
