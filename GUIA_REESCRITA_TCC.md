# Guia de reescrita do TCC-RELATORIO

Este guia substitui a versão anterior (que descrevia os resultados e o escopo de campanhas antigas; ela continua no histórico do git). Ele reúne o que a
orientadora pediu (`revisoes-orientadora/CRITICAS_E_PREFERENCIAS_ORIENTADORA.md`) e o estado científico atual do trabalho
(`../TCC-wsl/docs/PROTOCOLO_EXPERIMENTAL.md`, `../TCC-wsl/docs/PERGUNTAS_BANCA.md` e as tabelas em `../TCC-wsl/runtime/reports/thesis_protocol/tables/`).

## 0. Regras de trabalho

1. **Um capítulo por vez, fechando antes de avançar.** A orientadora só lê o próximo depois que o anterior estiver aprovado. Ordem: Capítulo 1, depois Resumo/Abstract,
   depois Capítulo 2, e assim por diante. Ao fechar um capítulo: compilar, gerar o PDF e enviá-lo por WhatsApp.
2. **Antes de escrever qualquer trecho, releia o checklist de `AGENTS.md`** (definir antes de usar; texto + figura + fórmula juntos; `equation` com `\label`; referência para o incomum;
   cada capítulo no seu papel; nada falso ou polêmico; enxugar).
3. **Números vêm das tabelas geradas** (`tex/tabelas/*.tex`, via `\inputtabela`), nunca digitados. Onde ainda houver `\aserpreenchido{...}`, escrever só depois de ler a tabela correspondente.
4. **Cada tabela e figura é chamada no texto antes de aparecer, dizendo o que observar** ("observe que o intervalo de confiança da diferença exclui zero...").

## 1. Estado científico (o que o texto pode afirmar)

- Protocolo único: estação Sapo, PM2,5 horário, 48 h de entrada para 24 h de saída, dados de 2017 a 2023; treino até 21/10/2019, validação até 27/05/2020, teste depois (teste histórico de junho a
  dezembro de 2020 e *holdout* de 2021 a 2023, sempre reportados separados). Todos os modelos com o mesmo treino, mesma busca de hiperparâmetros (24 tentativas, três dobras *walk-forward*) e quatro
  sementes (três nos fatores).
- Resultado principal (MAE, holdout): XGBoost por horizonte 2,77; Ridge 2,79; Seq2Seq com atenção 2,87 a 2,88; LSTM direta 2,98; melhor ingênuo (média móvel de 24 h) 3,07. **A LSTM direta não é a vencedora.**
  No teste histórico, XGBoost e os Seq2Seq com atenção empatam (a Ridge tem números próximos, mas não há teste pareado dela contra eles). O desenho "novo" do Seq2Seq empata com o canônico.
- Picos (≥ 35 µg/m³): nenhum modelo os prevê (subestimação em 95% a 100% dos pontos); a persistência tem erro por evento comparável.
- Atenção: o contexto é essencial (zerar custa mais de 1 µg/m³), a estrutura de faixas de defasagem importa, mas os pesos aprendidos valem no máximo ~0,03 sobre pesos uniformes entre faixas.
- Erro perto do piso de ruído da série (a interpolação com os dois vizinhos erra ~2,2; o melhor previsor de 1 h erra 2,3; o de 24 h, 2,9). Meteorologia da estação Aeroporto e PM dos vizinhos não melhoraram
  em teste exploratório (não citar os números daquele teste; refazer como ablação oficial se for usar).
- Limitações a declarar: estação única, teste histórico já consultado, meteorologia da própria estação indisponível, ausência de previsão probabilística.
- Metodologia dos alvos imputados: métricas só nos pontos observados (convenção do DCRNN, Li et al., 2018); não há artigo de PM2,5 sobre isso; declarar como decisão e mostrar a sensibilidade.

## 2. Capítulo 1: Introdução (prioridade; três rodadas de correção)

Estrutura pedida (detalhes e citações da orientadora em `CRITICAS_E_PREFERENCIAS_ORIENTADORA.md` §3):

1. **Parágrafo 1: o problema do PM2,5, detalhado.** O que é material particulado; por que "fino"; efeitos na saúde, internações e mortalidade, com referências (OMS 2021, Pope e Dockery 2006, Brook et al. 2010, Requia et al.);
   por que prever ajuda a prevenir. Sigla PM2,5 **depois** da explicação; PM10 idem. Absorver o conteúdo da atual seção 2.1 do Capítulo 2.
2. **Parágrafo 2: a dificuldade de prever a série.** Lacunas, ruído, mudanças de comportamento, picos raros, dependência de meteorologia, emissão, dispersão e outros poluentes que nem sempre estão
   disponíveis. Sem definir "série temporal" (Capítulo 2). Sem a frase cortada ("informação parcial e dados imperfeitos").
3. **Parágrafo 3: a lacuna.** A literatura já usa modelos de aprendizado profundo para PM2,5 e séries meteorológicas, com modelos diferentes e sem consenso nem comparativo. Referências. Nada de "a comparação entre
   trabalhos nem sempre é direta".
4. **Parágrafo 4: este trabalho.** "Estudo comparativo para previsão horária de curto prazo de PM2,5, utilizando diferentes modelos e arquiteturas (LSTM, Seq2Seq, XGBoost)"; buscar responder não só qual tem menor erro de
   predição, mas em que condições cada um é mais adequado; estudo de caso: série da estação Sapo, em Conceição do Mato Dentro (MG), dados da FEAM, **no fim do parágrafo**. Pode citar qual modelo se destacou, sem métricas.
   Sem janelamento, 48/24, recorte, "multissaída", "referência tabular".
5. **1.1 Motivação.** Por que fazer: série complexa (dados faltantes, dificuldades das séries meteorológicas), variedade crescente de arquiteturas na literatura, ausência de comparativo nesta série.
   **Remover** "Problema de Pesquisa" e "a pergunta que orienta este TCC".
6. **1.2 Objetivos.** Objetivo geral (sem "na estação Sapo"; horizonte de 24 horas explícito). Específicos: protocolo rastreável de previsão; comparar LSTM, Seq2Seq e XGBoost sob o mesmo protocolo; avaliar erro médio,
   erro por horizonte e picos; discutir em que condições cada um é adequado.
7. **1.3 Organização do trabalho.** Manter (aprovada), ajustando ao que mudar.

Depois de aprovado: Resumo e Abstract (sem "recorte CMD", "presença pareada", "mascaramento", "LSTM direta" sem explicação; "diferentes modelos"; "Porém, a previsão não é trivial"; aprendizado profundo como parte de aprendizado de máquina).

## 3. Capítulo 2: Fundamentação teórica (rodada 2; reordenar e completar)

Ordem sugerida, conforme ela indicou ("primeiro como os dados são estruturados"):

1. **Séries temporais** (título só isso): definição, univariada × multivariada, componentes, autocorrelação com símbolos definidos.
2. **Janelamento (aprendizado supervisionado em séries)**, com figura da janela deslizante: série contínua → pares entrada/saída; definir L, H, defasagens, variáveis exógenas, atributos de calendário e termos periódicos; por que não
   usar valores futuros observados.
3. **Previsão multi-horizonte:** estratégias recursiva, direta e codificador-decodificador, cada uma com **uma referência de aplicação** (candidatas: Taieb et al., 2012, para recursiva/direta; Sutskever et al., 2014, e Cho et al. para
   codificador-decodificador).
4. **Validação:** treino/validação/teste, validação cruzada temporal e *walk-forward*, com a Figura 2.1 conduzida pelo texto; o bloco final é o teste reservado desde o início.
5. **Dados faltantes, imputação e vazamento temporal** (três blocos: o que são; métodos clássicos; o que é vazamento e como evitar, com exemplos e normalização). Tratar a distinção observado × imputado como escolha apoiada em referência.
6. **Redes neurais, RNN, LSTM** (figura padrão com gates; estado interno; gradiente que some/explode antes; fórmulas ligadas à figura), **Seq2Seq e atenção** (figura padrão, maior; equações numeradas; **sem** aplicações em séries temporais,
   que vão ao Capítulo 3), **teacher forcing e scheduled sampling** (decodificador autorregressivo primeiro; figuras separadas; exemplo; Bernoulli, p_TF, b_{i,k}, currículo, free running, referência do Teutsch e Mäder).
7. **Impulsionamento por gradiente e XGBoost** (nome completo; XGBoost como caso; figura + texto + equação; sem "tabular × rede").
8. **Treinamento, perda e HPO** (hiperparâmetros, agenda de taxa de aprendizado, Huber, elementos das perdas J(θ), J_w(θ), por que automatizar, Optuna).
9. **Métricas** (definir todos os símbolos; conferir a fórmula do MAPE; não usar "acurácia"; mostrar como a análise por horizonte é feita; referência para calcular só nos pontos observados).
10. **Sem "Resumo do capítulo".** A seção 2.1 sai daqui (vai para o Capítulo 1).

## 4. Capítulo 3: Trabalhos relacionados (ainda não lido)

Recebe as aplicações que a orientadora mandou tirar do Capítulo 2 (Wen et al., 2017; DeepAR; Temporal Fusion Transformer; Seq2Seq em previsão multi-horizonte) e a discussão de PM2,5 com aprendizado profundo. Segue os mesmos princípios:
definir antes de usar, referência para cada afirmação, e uma frase de síntese que deixe a lacuna (falta de comparativo sob condições iguais) explícita, coerente com o parágrafo 3 da introdução.

## 5. Capítulo 4: Metodologia (já reescrito; falta adequá-lo ao que ela pede)

O texto atual foi escrito antes de ela ler o capítulo e usa muito jargão interno. Antes de enviar:
- Definir no primeiro uso: contrato de atributos, recorte/estação, faixas de defasagem, mascaramento, *holdout*, origem, semi-direto, sensibilidade.
- Colocar a justificativa da escolha da estação aqui (pedido explícito dela).
- Descrever o XGBoost por horizonte sem a dicotomia "tabular × redes"; o janelamento é o mesmo para todos.
- Conduzir cada figura e tabela pelo texto; equações em `equation` com `\label`; símbolos definidos.
- Apresentar métricas apenas em pontos observados como escolha apoiada em Li et al. (2018), com a sensibilidade.

## 6. Capítulo 5: Resultados (números novos; texto ainda não escrito)

Cada seção tem uma tabela gerada (`\inputtabela{...}`) e um `\aserpreenchido{...}` a substituir por texto que **conduza o leitor pela tabela**:

| Seção | Tabelas | O que dizer (e o que não dizer) |
|---|---|---|
| Comparação principal | `metricas_*`, `cauda_*`, `ensemble_holdout` | XGBoost/Ridge no topo; não afirmar superioridade do complexo |
| Significância | `pareado_*`, `matriz_*` | só "melhor" quando o IC exclui zero; senão "empate estatístico" |
| Erro por horizonte | `erro_por_horizonte_*` | o erro cresce pouco de H1 a H24 (2,3 → 2,9) |
| Picos e dinâmica | `eventos_*`, `dinamica_*` | ninguém prevê picos; correlação das variações baixa (0,13 a 0,17) |
| Fatores (perda, resíduo, evento) | `fatorial_perda_*`, `extras_*` | perda ponderada só ajuda o Seq2Seq novo; resíduo piora |
| Desenho do Seq2Seq | `ablacao_desenho_*` | peças quase não mudam o erro |
| PM10 | `ablacao_pm10_*` | ganho pequeno (~0,5%) no XGBoost |
| Atenção | `atencao_diagnostico_*`, `atencao_contrafactual_*` | contexto essencial; pesos aprendidos ≈ uniforme entre faixas |
| Janela | `janela_validacao` | julgada só na validação |
| Imputados | `sensibilidade_imputados_*` | a ordenação dos três primeiros não muda |
| Viés de reaproveitar HPO | `verificacao_hpo_*` | diferença dentro do ruído |
| Limite de previsibilidade (nova seção sugerida) | erro por horizonte, piso de ruído, convergência entre famílias | erro perto do piso; ganhos exigem informação nova |

## 7. Capítulo 6 e Resumo

Conclusão sem promessa de implantação; o mérito é o protocolo rastreável e a evidência de que, com estes dados, complexidade não compra desempenho. Resumo por último, em linguagem que o leitor entenda sem ter lido o texto.

## 8. Figuras a produzir ou substituir

- Janela deslizante (série → entrada/saída), com um exemplo numérico pequeno.
- LSTM padrão com gates, e Seq2Seq padrão da literatura (maior e legível); teacher forcing e agenda de p_TF em figuras separadas.
- Figura conduzida da validação *walk-forward* (com o bloco de teste reservado).
- XGBoost: figura de boosting alinhada às equações.
- Do protocolo atual: `erro_por_horizonte_*.pdf`, `janela_evento_*.pdf`, mapas de atenção do MLflow (executar `mlflow server` no banco oficial).

## 9. Referências pendentes pedidas por ela

- Uma aplicação para cada estratégia multi-horizonte (recursiva, direta, codificador-decodificador).
- Fonte para o trecho de Teutsch e Mäder (currículos e Increasing Teacher Forcing).
- Fonte que respalde avaliar somente nos pontos observados (ver §1).
- Conferir no `referencias.bib` as entradas novas (Cinar, Li DCRNN, Taieb, Che, Serrano, Wiegreffe, Cheng, Bergstra, Willmott, Chai, Little e Rubin, Montero-Manso), escritas de memória.

## 10. Fechamento de cada capítulo

- [ ] Checklist de `AGENTS.md` cumprido.
- [ ] Compila sem referência indefinida; todas as figuras/tabelas/equações referenciadas.
- [ ] PDF gerado e enviado por WhatsApp à orientadora.
- [ ] Aguardar o retorno antes de mexer no capítulo seguinte.
