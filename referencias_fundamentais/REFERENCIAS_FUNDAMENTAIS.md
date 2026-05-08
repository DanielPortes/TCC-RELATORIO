# Referencias Fundamentais do TCC

Curadoria feita para o TCC real do repositorio: previsao de PM2.5 com estudo de ablacao envolvendo representacao em delta vs absoluto, imputacao, conjuntos de atributos, arquiteturas recorrentes/seq2seq com atencao e praticas de treinamento/otimizacao.

Pasta base:
- `/home/portes/TCC/TCC-RELATORIO/referencias_fundamentais`

Convencao desta lista:
- `PDF salvo` = arquivo baixado localmente.
- `Metadado/link` = DOI ou pagina oficial relevante; nao houve PDF aberto baixado via shell.
- `Preprint salvo` = PDF salvo do arXiv/preprint, com DOI/link oficial do trabalho principal.

## 2.1 PM2.5, qualidade do ar e impactos em saude

- WHO. *WHO global air quality guidelines: particulate matter (PM2.5 and PM10), ozone, nitrogen dioxide, sulfur dioxide and carbon monoxide* (2021).
  Link oficial: https://www.who.int/publications/i/item/9789240034228/
  Status local: PDF salvo em `pdfs/pm25_saude/WHO_Global_Air_Quality_Guidelines_2021.pdf`

- WHO. *WHO global air quality guidelines: executive summary* (2021).
  Link oficial: https://www.who.int/publications/i/item/9789240034433/
  Status local: PDF salvo em `pdfs/pm25_saude/WHO_Air_Quality_Guidelines_Executive_Summary_2021.pdf`

- Pope, C. A. III; Dockery, D. W. *Health Effects of Fine Particulate Air Pollution: Lines that Connect* (2006).
  DOI: https://doi.org/10.1080/10473289.2006.10464485
  Apoio oficial: https://pubmed.ncbi.nlm.nih.gov/16805397/
  Status local: Metadado HTML salvo em `metadata/Pope_Dockery_2006_PubMed.html`

- Brook, R. D. et al. *Particulate Matter Air Pollution and Cardiovascular Disease: An Update to the Scientific Statement From the American Heart Association* (2010).
  DOI: https://doi.org/10.1161/CIR.0b013e3181dbece1
  Apoio oficial: https://stacks.cdc.gov/view/cdc/214655
  Status local: Metadado HTML salvo em `metadata/Brook_2010_CDC_stacks.html`

- Di, Q. et al. *Air Pollution and Mortality in the Medicare Population* (2017).
  DOI: https://doi.org/10.1056/NEJMoa1702747
  Apoio oficial: https://pmc.ncbi.nlm.nih.gov/articles/PMC5766848/
  Status local: Metadado/link

- Cohen, A. J. et al. *Estimates and 25-year trends of the global burden of disease attributable to ambient air pollution: an analysis of data from the Global Burden of Diseases Study 2015* (2017).
  DOI: https://doi.org/10.1016/S0140-6736(17)30505-6
  Status local: Metadado/link

- Requia, W. J. et al. *Health impacts of wildfire-related air pollution in Brazil* (2021).
  DOI: https://doi.org/10.1038/s41467-021-26822-7
  Status local: PDF salvo em `pdfs/pm25_saude/Requia_2021_Health_Impacts_Wildfire_Brazil.pdf`

- Requia, W. J. et al. *Short-term exposure to wildfire-related PM2.5 increases mortality risks and burdens in Brazil* (2022).
  DOI: https://doi.org/10.1038/s41467-022-35326-x
  Status local: PDF salvo em `pdfs/pm25_saude/Requia_2022_Wildfire_PM25_Mortality_Brazil.pdf`

## 2.2 Previsao em series temporais e avaliacao experimental

- Hyndman, R. J.; Athanasopoulos, G. *Forecasting: Principles and Practice*.
  Link oficial: https://otexts.com/fpp3/
  Status local: Metadado HTML salvo em `metadata/Hyndman_FPP3_home.html`

- Tashman, L. J. *Out-of-sample tests of forecasting accuracy: an analysis and review* (2000).
  DOI: https://doi.org/10.1016/S0169-2070(00)00065-0
  Status local: Metadado/link

- Bergmeir, C.; Benitez, J. M. *On the use of cross-validation for time series predictor evaluation* (2012).
  DOI: https://doi.org/10.1016/j.ins.2011.12.028
  Status local: Metadado/link

## 2.3 Modelos sequenciais: RNN, LSTM, Seq2Seq, atencao

- Hochreiter, S.; Schmidhuber, J. *Long Short-Term Memory* (1997).
  DOI: https://doi.org/10.1162/neco.1997.9.8.1735
  Status local: Metadado/link

- Sutskever, I.; Vinyals, O.; Le, Q. V. *Sequence to Sequence Learning with Neural Networks* (2014).
  DOI: https://doi.org/10.48550/arXiv.1409.3215
  Status local: PDF salvo em `pdfs/modelos_seq/Sutskever_2014_Seq2Seq.pdf`

- Bahdanau, D.; Cho, K.; Bengio, Y. *Neural Machine Translation by Jointly Learning to Align and Translate* (2014).
  DOI: https://doi.org/10.48550/arXiv.1409.0473
  Status local: PDF salvo em `pdfs/modelos_seq/Bahdanau_2014_Attention_NMT.pdf`

- Williams, R. J.; Zipser, D. *A Learning Algorithm for Continually Running Fully Recurrent Neural Networks* (1989).
  DOI: https://doi.org/10.1162/NECO.1989.1.2.270
  Status local: Metadado/link

- Bengio, S. et al. *Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks* (2015).
  DOI: https://doi.org/10.48550/arXiv.1506.03099
  Status local: PDF salvo em `pdfs/modelos_seq/Bengio_2015_Scheduled_Sampling.pdf`

## 2.4 Dados faltantes e imputacao

- Rubin, D. B. *Inference and Missing Data* (1976).
  DOI: https://doi.org/10.1093/biomet/63.3.581
  Status local: Metadado/link

- van Buuren, S.; Groothuis-Oudshoorn, K. *mice: Multivariate Imputation by Chained Equations in R* (2011).
  DOI: https://doi.org/10.18637/jss.v045.i03
  Status local: PDF salvo em `pdfs/imputacao/van_Buuren_2011_MICE_JSS.pdf`

- Troyanskaya, O. et al. *Missing value estimation methods for DNA microarrays* (2001).
  DOI: https://doi.org/10.1093/bioinformatics/17.6.520
  Status local: Metadado/link

- Stekhoven, D. J.; Buhlmann, P. *MissForest: non-parametric missing value imputation for mixed-type data* (2012).
  DOI: https://doi.org/10.1093/bioinformatics/btr597
  Status local: Metadado/link

## 2.5 Treinamento, perdas e otimizacao

- Huber, P. J. *Robust Estimation of a Location Parameter* (1964).
  DOI: https://doi.org/10.1214/aoms/1177703732
  Status local: Metadado/link

- Koenker, R.; Bassett, G. *Regression Quantiles* (1978).
  DOI: https://doi.org/10.2307/1913643
  Apoio oficial: https://www.econometricsociety.org/publications/econometrica/browse/supplemental-materials/1978/01/01/regression-quantiles
  Status local: Metadado/link

- Kingma, D. P.; Ba, J. *Adam: A Method for Stochastic Optimization* (2014).
  DOI: https://doi.org/10.48550/arXiv.1412.6980
  Status local: PDF salvo em `pdfs/otimizacao_treino/Kingma_Ba_2014_Adam.pdf`

- Loshchilov, I.; Hutter, F. *Decoupled Weight Decay Regularization* (2017).
  DOI: https://doi.org/10.48550/arXiv.1711.05101
  Status local: PDF salvo em `pdfs/otimizacao_treino/Loshchilov_Hutter_2017_AdamW.pdf`

- Akiba, T. et al. *Optuna: A Next-generation Hyperparameter Optimization Framework* (2019).
  DOI oficial: https://doi.org/10.1145/3292500.3330701
  Preprint salvo: https://doi.org/10.48550/arXiv.1907.10902
  Status local: PDF salvo em `pdfs/otimizacao_treino/Akiba_2019_Optuna.pdf`

- Prechelt, L. *Early Stopping - But When?* (1998).
  DOI: https://doi.org/10.1007/3-540-49430-8_3
  Status local: Metadado HTML salvo em `metadata/Prechelt_1998_Early_Stopping.springer.html`

## 2.6 Trabalhos relacionados diretamente conectados ao tema

- *Deep-learning architecture for PM2.5 concentration prediction: A review* (2024).
  DOI: https://doi.org/10.1016/j.ese.2024.100400
  Apoio oficial: https://www.sciencedirect.com/science/article/pii/S2666498424000140
  Status local: PDF salvo em `pdfs/aplicacoes_pm25/PM25_Review_2024_Deep_Learning_Architecture.pdf`

- Zanobini, M. et al. *Prediction and forecasting of PM2.5 in Curitiba with machine learning* (2024).
  DOI: https://doi.org/10.3389/fdata.2024.1412837
  Status local: PDF salvo em `pdfs/aplicacoes_pm25/Zanobini_2024_PM25_Curitiba_Machine_Learning.pdf`

- Li, T. et al. *Urban PM2.5 Concentration Prediction via Attention-Based CNN-LSTM* (2020).
  DOI: https://doi.org/10.3390/app10061953
  Apoio oficial: https://www.mdpi.com/2076-3417/10/6/1953
  Status local: Metadado/link

- Rahu, A.; Lee, H.; Shin, D. *Forecasting hourly PM2.5 concentration with an optimized LSTM model* (2023).
  DOI: https://doi.org/10.1016/j.atmosenv.2023.120161
  Apoio oficial: https://www.sciencedirect.com/science/article/pii/S1352231023005873
  Status local: Metadado/link

## Observacoes praticas para a escrita

- Nucleo minimo da fundamentacao teorica:
  PM2.5/saude (WHO, Pope & Dockery, Brook, Di, Cohen), avaliacao temporal (Hyndman, Tashman, Bergmeir), modelos (LSTM, Seq2Seq, atencao), imputacao (Rubin, MICE, KNN/Troyanskaya, missForest), treinamento/otimizacao (Williams & Zipser, Scheduled Sampling, Huber, AdamW, Optuna, Early Stopping).

- Nucleo minimo de trabalhos relacionados:
  review de PM2.5 2024, Curitiba 2024, attention-based CNN-LSTM 2020, LSTM otimizado 2023.

- Arquivos locais validos baixados nesta curadoria:
  13 PDFs + 4 HTMLs de metadado.
