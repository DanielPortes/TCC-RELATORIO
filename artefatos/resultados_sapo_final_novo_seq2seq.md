# Resultados finais Sapo com novo Seq2Seq

Fonte: `../TCC-wsl/runtime/reports/sapo_final_new_seq2seq_suite_20260522/`.

Protocolo: estação Sapo, contrato `clean_pm10_decoder_proxy`, entrada de 48 horas, horizonte de 24 horas, divisão cronológica 70/15/15, imputação linear e máscara de alvo observado em perda e métricas. As runs finais usam as sementes 42, 7, 21 e 123.

## Resultado seed 42

| Modelo | MAE | RMSE | R2 | H1 MAE | H24 MAE | Peak35 MAE | p99 previsto |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| LSTM direta | 2,7713 | 3,8346 | 0,5154 | 2,6725 | 2,8670 | 13,6112 | 28,57 |
| Seq2Seq atenção novo | 2,8132 | 3,8799 | 0,5039 | 2,6222 | 2,9138 | 11,0815 | 32,50 |
| XGBoost multissaída | 2,8786 | 3,9793 | 0,4781 | 2,5618 | 3,0273 | 12,2583 | 30,73 |
| Seq2Seq atenção canônica | 2,8811 | 3,9859 | 0,4764 | 2,7155 | 2,9743 | 14,7027 | 29,13 |
| LSTM recursiva | 2,8876 | 3,8380 | 0,5146 | 2,7380 | 3,1492 | 12,0392 | 30,49 |
| Seq2Seq básico | 2,9553 | 4,0967 | 0,4469 | 2,6519 | 3,1514 | 12,9806 | 30,65 |

## Média multi-seed

| Modelo | MAE médio | Desvio MAE | RMSE médio | R2 médio | Peak35 MAE médio | p99 previsto médio |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| LSTM direta | 2,8055 | 0,0540 | 3,8611 | 0,5086 | 14,1071 | 28,03 |
| Seq2Seq atenção novo | 2,8218 | 0,0220 | 3,8989 | 0,4989 | 11,5855 | 31,90 |
| LSTM recursiva | 2,8425 | 0,0426 | 3,8006 | 0,5239 | 12,1494 | 30,78 |
| Seq2Seq atenção canônica | 2,8727 | 0,0175 | 3,9592 | 0,4834 | 13,7824 | 29,71 |
| XGBoost multissaída | 2,8852 | 0,0077 | 3,9895 | 0,4755 | 12,5280 | 30,40 |
| Seq2Seq básico | 2,9444 | 0,0113 | 4,0778 | 0,4520 | 12,7627 | 30,85 |

## Eventos de pico

Na análise por 21 eventos contínuos com PM2,5 observado maior ou igual a 35, o novo Seq2Seq atenção teve o menor MAE médio por evento: 12,4138. A LSTM direta, embora vencedora por MAE global, teve MAE de evento 15,4683 e p99 previsto mais baixo.

## Leitura para o texto

A LSTM direta continua sendo a conclusão principal para erro médio. O novo Seq2Seq atenção substitui a variante antiga com `weighted_l1` como principal resultado Seq2Seq porque melhora MAE, amplitude e picos. A frase central do capítulo de resultados deve ser: LSTM direta vence por MAE; novo Seq2Seq atenção é o melhor compromisso para eventos de maior concentração.
