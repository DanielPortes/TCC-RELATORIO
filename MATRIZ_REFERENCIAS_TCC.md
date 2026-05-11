# Matriz de Referencias do TCC

Esta matriz conecta cada referencia ao ponto do texto que ela sustenta. Ela e inicial: antes da versao final, `referencias.bib` deve ser limpo para manter apenas entradas citadas e receber as entradas pendentes marcadas abaixo.

## Checklist da Matriz

- [x] Blocos bibliograficos principais mapeados.
- [x] Referencias ja existentes em `referencias.bib` identificadas.
- [x] Lacunas bibliograficas criticas marcadas como pendentes.
- [x] Entradas BibTeX pendentes adicionadas.
- [x] Chaves nao usadas removidas ou rebaixadas.
- [x] Citacoes finais conferidas contra os capitulos.
- [x] Referencias estruturantes de deep forecasting pesquisadas e adicionadas.
- [x] Citacoes diretas curtas e citacoes indiretas distribuidas nos Caps. 2 e 3.
- [x] Referencias para diagramas proprios dos modelos vinculadas no texto.

## Matriz

| Chave BibTeX | Tema | Secao prevista | Ideia sustentada | Status do PDF/link |
| --- | --- | --- | --- | --- |
| `who2021air` | PM2.5 e saude | Cap. 1; Cap. 2 | PM2.5 e PM10 sao poluentes prioritarios e motivam monitoramento e previsao. | PDF salvo segundo `referencias_fundamentais`. |
| `pope2006health` | PM2.5 e saude | Cap. 1; Cap. 2 | Material particulado fino esta associado a efeitos respiratorios e cardiovasculares. | Metadado/link salvo. |
| `brook2010particulate` | PM2.5 e saude | Cap. 1; Cap. 2 | Evidencia cardiovascular para exposicao a particulados. | Metadado/link salvo. |
| `cohen2017estimates` | Carga global de doenca | Cap. 1 | Poluicao atmosferica por particulados tem impacto global relevante. | Metadado/link. |
| `requia2021health` | Brasil e queimadas | Cap. 1; Cap. 3 | Evidencia brasileira de impacto de poluicao relacionada a queimadas. | PDF salvo segundo curadoria. |
| `requia2022short` | Brasil e PM2.5 | Cap. 1; Cap. 3 | Exposicao de curto prazo a PM2.5 de queimadas aumenta riscos de mortalidade. | PDF salvo segundo curadoria. |
| `hyndman2021forecasting` | Forecasting | Cap. 2; Cap. 4 | Padroes de series temporais, decomposicao, autocorrelacao, avaliacao temporal, holdout e metricas de previsao. | Metadado/link salvo. |
| `tashman2000out` | Avaliacao fora da amostra | Cap. 2; Cap. 4 | Teste fora da amostra e separacao entre treino/validacao/teste. | Metadado/link. |
| `bergmeir2012crossvalidation` | Series temporais | Cap. 2; Cap. 4 | Cuidados com validacao cruzada e dependencia temporal. | Metadado/link. |
| `hewamalage2021rnn` | RNNs para forecasting | Cap. 2; Cap. 3 | Referencia transversal para uso de redes recorrentes em previsao de series temporais, com ressalva de que nao ha arquitetura universal. | Adicionada apos pesquisa bibliografica de reforco. |
| `benidis2022deep` | Deep forecasting | Cap. 2; Cap. 3 | Survey/tutorial amplo para justificar deep learning, janelas supervisionadas, covariaveis e comparacao de arquiteturas. | Adicionada apos pesquisa bibliografica de reforco. |
| `lim2021survey` | Deep forecasting multi-horizonte | Cap. 2; Cap. 3 | Survey sobre desenhos de encoder/decoder para previsao um-passo e multi-horizonte. | Adicionada apos pesquisa bibliografica de reforco. |
| `wen2017mqrnn` | Seq2Seq multi-horizonte | Cap. 2; Cap. 3 | Justifica Seq2Seq como formulacao natural para previsao multi-horizonte recorrente. | Adicionada apos pesquisa bibliografica de reforco. |
| `salinas2020deepar` | DeepAR | Cap. 2; Cap. 3 | Exemplo relevante de decoder recorrente/autoregressivo para forecasting probabilistico. | Adicionada apos pesquisa bibliografica de reforco. |
| `lim2021tft` | Temporal Fusion Transformer | Cap. 2; Cap. 3 | Exemplo moderno de previsao multi-horizonte com covariaveis futuras conhecidas e interpretabilidade. | Adicionada apos pesquisa bibliografica de reforco. |
| `zhou2021informer` | Transformer temporal | Cap. 3; Cap. 4 | Exemplo de Transformer eficiente para previsao de series temporais longas. | Adicionada na rodada de delimitacao sobre Transformers. |
| `wu2021autoformer` | Transformer temporal | Cap. 3; Cap. 4 | Exemplo de arquitetura Transformer com decomposicao e autocorrelacao para forecasting. | Adicionada na rodada de delimitacao sobre Transformers. |
| `nie2023patchtst` | Transformer temporal | Cap. 3; Cap. 4 | Exemplo recente de Transformer com patches para previsao de longo horizonte. | Adicionada na rodada de delimitacao sobre Transformers. |
| `zeng2023transformers` | Critica a Transformers em forecasting | Cap. 3; Cap. 4 | Fundamenta a cautela de que Transformers nao vencem automaticamente benchmarks de series temporais. | Adicionada na rodada de delimitacao sobre Transformers. |
| `rubin1976inference` | Dados faltantes | Cap. 2; Cap. 4 | Ausencia de dados e implicacoes inferenciais. | Metadado/link. |
| `vanbuuren2011mice` | Imputacao | Cap. 2; Cap. 4 | Imputacao multivariada como tecnica relacionada, mesmo que nao seja o contrato final. | PDF salvo segundo curadoria. |
| `stekhoven2012missforest` | Imputacao | Cap. 2; Cap. 4 | Imputacao nao parametrica como alternativa avaliada/relacionada. | Metadado/link. |
| `du2023saits` | Imputacao por deep learning | Cap. 2 ou Cap. 3 | SAITS pode aparecer como trabalho relacionado, nao como metodo central do TCC final. | Entrada existente; uso opcional. |
| `hochreiter1997long` | LSTM | Cap. 2; Cap. 4 | Base teorica das arquiteturas LSTM direta e recursiva. | Metadado/link. |
| `sutskever2014sequence` | Seq2Seq | Cap. 2; Cap. 4 | Formula encoder-decoder para sequencias. | PDF salvo segundo curadoria. |
| `bahdanau2014neural` | Atencao | Cap. 2; Cap. 4 | Atencao aditiva como mecanismo de alinhamento em Seq2Seq. | PDF salvo segundo curadoria. |
| `bengio2015scheduled` | Scheduled sampling | Cap. 2; Cap. 5 | Define scheduled sampling como transicao de teacher forcing para uso crescente das predicoes do modelo; tecnica avaliada em ablacões auxiliares, sem ser vencedora final. | PDF salvo segundo curadoria. |
| `teutsch2022flipped` | Increasing Teacher Forcing | Cap. 2; Cap. 4 | Fundamenta a ablação de agenda crescente de teacher forcing em series temporais; paper reporta ganhos em forecasting multi-step com curriculos do tipo Flipped Classroom. | Fonte primaria: TMLR/OpenReview e arXiv. |
| `kingma2014adam` | Otimizacao | Cap. 2; Cap. 4 | Otimizacao com Adam/AdamW nos modelos neurais. | PDF salvo segundo curadoria. |
| `goodfellow2016deep` | Deep learning | Cap. 2 | Conceitos gerais de redes neurais profundas. | Removida da bibliografia final por nao ser mais citada. |
| `yang2023attention` | PM2.5 com attention-LSTM | Cap. 3 | Exemplo de uso de atencao/LSTM em previsao horaria de PM2.5. | Entrada existente. |
| `zhao2021pm2` | PM2.5 com LSTM | Cap. 3 | Exemplo de modelo hibrido/recorrente para PM2.5. | Entrada existente. |
| `zhang2021deep` | PM2.5 com deep learning | Cap. 3 | Exemplo de deep learning aplicado a PM2.5. | Entrada existente. |
| `song2018arima` | Baselines classicos | Cap. 3 | Exemplo de combinacao estatistica/ML para PM2.5. | Entrada existente; uso opcional. |
| `guo2019pm2` | Baseline tabular | Cap. 3 | Random forest e variaveis meteorologicas para PM2.5. | Entrada existente; uso opcional. |
| `chen2016xgboost` | XGBoost | Cap. 2; Cap. 4; Cap. 5 | Fundamenta o baseline tabular XGBoost multi-output. | Adicionado em `referencias.bib`. |
| `akiba2019optuna` | HPO | Cap. 4 | Fundamenta a busca de hiperparametros via Optuna. | Adicionado em `referencias.bib`; PDF salvo segundo curadoria. |
| `huber1964robust` | Funcao Huber | Cap. 2; Cap. 4 | Justifica uso de Huber loss em modelos principais. | Adicionado em `referencias.bib`. |
| `luong2015effective` | Atencao Luong | Cap. 2; Cap. 5 | Necessaria se as ablacões Luong dot/general/local forem discutidas. | Adicionado em `referencias.bib`. |
| `jain2019attention` | Interpretabilidade de atencao | Cap. 5 | Sustenta a cautela de que pesos de atencao nao sao explicacao causal completa do modelo. | Adicionada na rodada de analise dos pesos de atencao. |
| `qin2017darnn` | DA-RNN | Cap. 3; Cap. 5 | Necessaria se DA-RNN for citado nas ablacões internas do Seq2Seq. | Adicionado em `referencias.bib`. |
| `pm25_review_2024` | Revisao PM2.5 deep learning | Cap. 3 | Revisao recente para posicionar o trabalho. | Adicionado em `referencias.bib`; PDF salvo segundo curadoria. |
| `zanobini2024curitiba` | PM2.5 no Brasil | Cap. 3 | Trabalho brasileiro recente de previsao de PM2.5 com ML. | Adicionado em `referencias.bib`; PDF salvo segundo curadoria. |
| `tran2023optimized_lstm` | PM2.5 horario com LSTM | Cap. 3 | LSTM otimizado em previsao horaria de PM2.5. | Adicionado em `referencias.bib`; corrige a chave provisoria `rahu2023optimized_lstm` da curadoria. |
| `li2020urban` | PM2.5 com CNN-LSTM e atencao | Cap. 3 | Exemplo de arquitetura hibrida com atencao para PM2.5 urbano. | Adicionado em `referencias.bib`. |
| `ayturan2020short` | PM2.5 curto prazo | Cap. 3 | Mostra uso de RNN/LSTM/GRU em previsao de curto prazo e ajuda a discutir sensibilidade ao horizonte. | Adicionado em `referencias.bib`. |
| `su2023cnn_lstm_pm25` | PM2.5 com CNN-LSTM e variaveis ricas | Cap. 3 | Exemplo com multiplas cidades, copoluentes, meteorologia ERA5 e PWV; sustenta cautela de comparabilidade. | Adicionado em `referencias.bib`. |
| `hu2024high_dim_pm25` | PM2.5 high-dimensional time series | Cap. 3 | Exemplo de DL para series multivariadas de alta dimensao. | Adicionado em `referencias.bib`. |
| `zhang2025gnss_pwv_rf_lstm` | PM2.5 com GNSS-PWV e RF-LSTM | Cap. 3 | Exemplo de previsao com variaveis meteorologicas/atmosfericas ricas e horizonte curto. | Adicionado em `referencias.bib`. |
| `zeng2026diverse_horizons` | PM2.5 em horizontes diversos | Cap. 3 | Mostra que meteorologia melhora mais que copoluentes e que horizonte/completude sazonal afetam desempenho. | Adicionado em `referencias.bib`. |
| `qamar2025cleaner_air` | PM2.5 com DL e series tradicionais | Cap. 3 | Exemplo recente de comparacao entre modelos DL e abordagens tradicionais. | Adicionado em `referencias.bib`. |
| `li2020hybrid_cnn_lstm_access` | PM2.5 CNN-LSTM 24h | Cap. 3 | Exemplo de modelo CNN-LSTM para proxima janela de 24h com entradas multivariadas. | Adicionado em `referencias.bib`. |
| `liu2025pso_transformer_lstm` | PM2.5 Transformer-LSTM com PSO | Cap. 3 | Exemplo de arquitetura hibrida otimizada, com ressalva de que arquitetura depende do contrato de dados. | Adicionado em `referencias.bib`. |
| `he2024comparative_pm25` | PM2.5 mensal | Cap. 3 | Exemplo de resultado com agregacao mensal, nao diretamente comparavel ao protocolo horario 48->24. | Adicionado em `referencias.bib`. |
| `bai2024cnn_lstm_pm25` | PM2.5 CNN-LSTM com fatores meteorologicos | Cap. 3 | Exemplo de R2 alto em tarefa com dados diarios, meteorologia e componente espacial. | Adicionado em `referencias.bib`. |
| `chen2024lstcn_pm25` | PM2.5 horario espaco-temporal | Cap. 3 | Exemplo de modelo com informacao espacial/multiplas estacoes e PCA. | Adicionado em `referencias.bib`. |
| `feng2024hybrid_spatiotemporal_pm25` | PM2.5 ST-GCN/high resolution | Cap. 3 | Exemplo de desempenho alto com informacao espacial de alta resolucao; sustenta a nao comparabilidade com Sapo uniestacao. | Adicionado em `referencias.bib`. |
| `balaraman2022lstm_pm25` | PM2.5 LSTM urbano | Cap. 3 | Exemplo de LSTM com dados de 15 minutos e R2 alto, mas em contrato diferente. | Adicionado em `referencias.bib`. |

## Decisoes de Uso

- `SAITS` deve sair do centro do texto; usar `du2023saits` apenas como relacionado de imputacao se a narrativa exigir.
- Referencias de blogs ou paginas didaticas (`olah2015understanding`, `alammar2018visualizing`, `aprilliant2021walkforward`) foram removidas da bibliografia final porque as figuras antigas deixaram de ser usadas.
- As entradas pendentes de XGBoost, Optuna, Huber e trabalhos recentes de PM2.5 foram adicionadas em `referencias.bib`; falta apenas conferir citacoes finais e remover chaves nao usadas.
- A defesa do Seq2Seq foi reforcada com surveys e trabalhos de multi-horizon forecasting, mas o texto evita afirmar SOTA universal; a formulacao correta e que Seq2Seq e uma familia bem fundamentada e competitiva para tarefas sequencia-para-sequencia/multi-horizonte.
- As figuras conceituais de LSTM, Seq2Seq com atencao e XGBoost foram geradas como elaboracao propria; as citacoes nas legendas indicam a base teorica, nao reaproveitamento de figuras externas.
- Transformers foram reconhecidos como linha moderna relevante, mas ficaram fora do escopo experimental final por exigirem HPO proprio, validacao comparavel e nova bateria multi-seed.
- Os pesos de atencao foram analisados como diagnostico interpretativo limitado; o texto evita tratar atencao como explicacao causal completa.
