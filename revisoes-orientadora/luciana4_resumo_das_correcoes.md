# Correções da Luciana: reunião 4 (cap. 1 a 4.2)

Documento único desta revisão. Ele reúne os pedidos dela e o veredito de cada um, conferido nos dados e no código.

## Como ler

**Fontes:**
1. As anotações manuscritas no PDF (`luciana4_pdf_anotado.pdf`), lidas página a página.
2. O áudio (`luciana4_transcricao.md`).
3. `luciana4_texto_xgboost.docx`.
4. O código do protocolo, com o CSV bruto e as tabelas geradas (caminhos no Anexo).

**Convenções:**
- `impr. m` é a página impressa. `PDF n` é a página do arquivo (n = m + 13).
- `[hh:mm]` é o tempo no áudio.
- Aspas curtas trazem a anotação dela com a minha leitura da letra; `[?]` marca trecho ilegível.
- As marcas vão do Resumo (PDF 6) até a **impr. 37 (PDF 50)**. Ela parou no "quadro" da 4.2.1, e não há marcas depois.

**Veredito de cada ponto:**
- **[procede]**: ela tem razão, é só fazer.
- **[em parte]**: o problema de texto existe, mas a afirmação técnica dela não está certa.
- **[não procede]**: o PDF ou o código estão corretos. Reescreva para tirar a dúvida, sem tornar o texto tecnicamente errado.
- **[verificado]**: fato conferido nos dados ou no código.

**Estação:** Sapo, que aparece como "CMD / Sapo" (Conceição do Mato Dentro). A 1ª colocada no ranking é Rio Doce / Estação Principal.

---

## 1. Conclusões gerais

### 1.1 Precisa retreinar? Não.
Não encontrei erro que invalide os resultados. Conferi:
- **Imputação:** é causal. É linear só até o fim do treino; depois do corte, só propaga o último valor medido. Na busca de hiperparâmetros, é refeita em cada dobra.
- **Normalização:** usa apenas o treino, tanto nas redes (`compute_station_stats(df_train)`) quanto na Ridge (`StandardScaler().fit(Xtr)`).
- **Escolhas de hiperparâmetros:** o α da Ridge, a busca das redes e a do XGBoost usam só a validação.
- **Covariáveis futuras:** são causais. `PM10_proxy_exante` = PM10(t−24), conhecido em t para h ≤ 24. Os termos seno e cosseno são determinísticos.
- **Alvos imputados:** ficam fora da perda e das métricas.
- **Números do PDF:** batem com o CSV bruto. Recalculei autocorrelações, correlações, cobertura e os tamanhos dos blocos.

O que precisa ser refeito é **figura e texto**, sem treino:
- Fig. 4.3: o script usa valores imputados e plota o teste de 2020 (ver 4.1.3).
- Fig. 2.1: a legenda está sobreposta.
- Fig. 4.2: deve mostrar também 2021–2023.

Uma ressalva que só você pode confirmar: que nenhuma decisão de projeto olhou 2021–2023 antes da execução final.

### 1.2 Se já há validação cruzada, por que há um holdout?
Os dois têm funções diferentes:
- **Validação cruzada (walk-forward, 3 dobras sobre 2017 a mai./2020):** serve para **escolher**, com 24 tentativas de hiperparâmetros por arquitetura. O erro de validação cruzada da configuração vencedora é **otimista**, porque ela foi escolhida justamente por ter o menor erro entre muitas. É o viés de seleção (Cawley e Talbot, 2010).
- **Holdout (2021–2023):** serve para **medir**. São dados que não participaram de nenhuma escolha, então dão a estimativa honesta.

É exatamente a sua Fig. 2.2: as partições com treino e validação, mais o "bloco final" verde reservado para o teste. No cap. 4, os blocos 1 a 4 correspondem a 2017 até mai./2020, e o bloco final a 2021–2023.

O "teste histórico" (jun. a dez./2020) foi consultado nos estudos preliminares. Por isso ele não serve como teste independente, e foi isso que motivou o holdout.

**Sugestão para simplificar o cap. 4:** apresente só dois períodos, desenvolvimento (2017–2020) e teste (2021–2023), e mande os resultados de 2020 para o apêndice (`ap_a_teste_historico` já existe). Isso elimina o termo "teste histórico", que ela rejeitou, e quase toda a confusão da 4.2.1. Não exige retreino.

Explique também as duas etapas:
- Na busca, há 3 dobras walk-forward.
- No treino final, há a divisão fixa treino/validação (parada antecipada).

### 1.3 Quantos modelos foram usados?
- **Quatro famílias:** LSTM, Seq2Seq, XGBoost e regressão linear (Ridge). É a contagem de "quatro modelos" que ela fez no áudio.
- **Sete modelos treinados:**
  - LSTM direta;
  - LSTM recursiva;
  - Seq2Seq básico;
  - Seq2Seq com atenção padrão;
  - Seq2Seq com atenção adaptado;
  - XGBoost;
  - Ridge.
- **Cinco referências ingênuas**, sem treinamento: persistência y(t), sazonal y(t−24), sazonal y(t−48), média móvel de 6 h e média móvel de 24 h. Ela insiste que também são modelos. Chame de "modelos de referência ingênuos" e diga que não são treinados.
- **Ablações e fatores** (perda ponderada, aprendizado residual, janelas 24/72/96, contratos de atributos) são **variações** dos modelos, não modelos novos.

**Recomendação:** ponha uma tabela no início do cap. 4 com as colunas família / modelo / estratégia multi-horizonte / treinado?. Use os mesmos números no resumo, no cap. 1 e no cap. 5.

### 1.4 Diagnóstico geral do texto
Ela tem razão no essencial: há termos usados antes de explicados, referências para frente e trechos que se contradizem. O parágrafo da escolha da estação é o caso mais claro (ver 4.1.1). A regra prática dela vale para o texto todo:
- referenciar só para trás;
- explicar cada termo antes de usá-lo;
- na fundamentação, trazer só o que o trabalho usa, ligando texto, figura e equação.

---

## 2. O que você disse no áudio e os dados contradizem
Corrija isto antes de reescrever o cap. 4.

| Você disse no áudio | O que os dados e o código mostram |
|---|---|
| "Tenho quase certeza que não existe essa coluna" de partículas totais [00:50] | **[verificado] Existe.** A coluna `PTS` tem **86,06 %** de cobertura (2017–2023). O PDF estava certo. |
| "2021 a 23 eu não usei… descartei" e "22 e 23 joguei fora" [00:54, 01:10] | **[verificado] Falso.** 2021–2023 é o holdout (`protocol.holdout_start`, Tabela 4.3, `metricas_holdout.tex`), e o cap. 5 inteiro usa esse período. Quem usou só 2017–2020 foram as campanhas antigas (70/15/15). |
| "Por que não usou a série toda? Porque piorava" [00:55] | O protocolo final usa a série toda: 2017–2020 no desenvolvimento e 2021–2023 no teste. |
| "2017–2020 vai ser o treinamento" [01:17] | O treino vai só até **21/10/2019**. 2017–2020 é treino, validação e teste de 2020. |
| Escolha da estação: "procurei menos picos" [01:05] | É o contrário. O PDF prefere Sapo por ter **mais** picos (1,16 % contra 0,19 % das horas). |
| Orçamento do Hyperband = "tempo computacional" [00:36] | Quase. No código, o recurso é a **época** (`pruner_min_resource: 4`). Orçamento = quantas épocas cada tentativa pode treinar antes de ser podada. |
| L = 48: "acho que eu não coloquei no texto" [01:25] | Está na Seção 5.9.1 (janelas 24/48/72/96). O problema é só a referência para frente. |

---

## 3. Decisões estruturais (valem para o texto todo)
1. **Referenciar só para trás.** Nada de "veja adiante". O que está na frente e é usado antes deve subir. [01:26; impr. 36 "isso é p/ trás, não p/ frente"] **[procede]**
2. **Explicar o termo antes de usar:** variável exógena, defasagem, L, h₀, "estatísticas de normalização", "gargalo". [00:12] **[procede]**
3. **Fundamentação sem elaboração própria.** Use figuras e definições da literatura, ligando texto, figura e equação. Não descreva "o seu trabalho" no cap. 2. [00:28, 00:37] **[procede]**
4. **Equações:** depois de cada uma, escreva "**onde** …" em vez de "Na Equação X, …". Ela marcou isso nas impr. 6, 7, 8, 11 e 13. [00:11] **[procede]**
5. **Numeração do cap. 2:**
   - **2.1 Séries temporais:** 2.1.1 Janelas e exógenas; 2.1.2 Validação temporal; 2.1.3 Dados faltantes, com 2.1.3.1 Dados faltantes, 2.1.3.2 Imputação e 2.1.3.3 Vazamento.
   - **2.2 Redes neurais:** 2.2.1 RNN/LSTM; 2.2.2 Seq2Seq.
   - **2.3** XGBoost; **2.4** Treinamento; **2.5** Métricas, com 2.5.1 Comparação estatística.
   - A seção só se quebra quando muda o assunto. [00:11] **[procede]**
6. **Padronizar termos:**
   - "neurônio", não "unidade da rede";
   - "variável exógena", não "auxiliar";
   - "pico", não "evento de alta concentração";
   - "conjunto de dados", não "artefato";
   - "estudos preliminares", não "etapas exploratórias anteriores".

   [00:35, 00:51, 01:04, 01:12] **[procede]**
7. **Resultados (cap. 5):** 98 páginas é demais. Tabelas para o apêndice; no texto, só o que importa e quem ganhou. [01:28] **[procede]**
8. **Fluxo de trabalho:** ela lê os caps. 4, 5 e 6 enquanto você corrige os anteriores. Arrume o cap. 4 e envie primeiro. [01:29]

---

## 4. Página a página

### Resumo (PDF 6)
- "*P*articulate *M*atter" com maiúsculas, tanto aqui quanto na impr. 2. [00:00]
- "além de previsores simples e de uma regressão linear como referências" → "…XGBoost **e da** regressão linear".
- Riscado: "confirmados em um período de 2021 a 2023 não consultado durante o desenvolvimento".
  - **[em parte]** O fato é verdadeiro e é um ponto forte. Ela riscou pela mesma confusão do cap. 4. Depois que o cap. 4 estiver claro, vale reintroduzi-lo em meia frase.
- Riscado: "sem diferença estatística entre eles, e que as redes neurais tiveram erro até cerca de 8 % maior".
  - **[verificado]** As duas afirmações estão corretas: XGBoost tem MAE 2,767 e Ridge 2,794, com IC da diferença de −0,074 a 0,007; a pior rede, a LSTM direta, tem 2,979, ou seja, +7,7 %. Tirar ou não é escolha de redação.
- Inserido "**porém,** todos os modelos subestimaram os picos". [00:01]
- Ondulado em todo o final, de "Conclui-se que…" até "situações ambientalmente relevantes". Ela disse que não gostou, mas não pediu para tirar.

### Cap. 1: Introdução

**impr. 3 (PDF 16): 1.1 Motivação e 1.2 Objetivos**
- Na lista "…LSTM, Seq2Seq e XGBoost", ela escreveu "**regressão linear?**". Inclua a regressão linear e corrija a pontuação (o "e" antes de XGBoost). [00:02] **[procede]**
- "Ele usa como caso principal…" foi riscado. Troque por "**O estudo de caso consiste em…**". [00:03]
- Na Seção 1.1: "**tirar uma seção e deixar o texto corrido**". [00:03] **[procede]**
- Objetivo geral: há ondulado em "com horizonte de 24 horas, avaliando desempenho médio…". Fica: "comparar diferentes modelos para previsão horária de curto prazo de PM2,5". [00:03]
  - **[em parte]** A frase dela de que "regressão linear não é ML" é discutível: a Ridge é aprendizado supervisionado. Mas trocar por "modelos" não custa nada. Só não escreva essa afirmação no texto.

**impr. 4 (PDF 17)**
- Objetivos específicos riscados com X: "**Tá muito ruim isso. Fala só as etapas da sua metodologia.**" Ou seja, preparação da série, imputação, modelos e avaliação. [00:03] **[procede]**
- No item 3 ("mesmo conjunto de teste…"): "**isso é óbvio em comparação… não tem que chamar atenção!**" **[procede]**
- 1.3 Cronograma riscado: "**Não tem cronograma em monografia.**" Isso vale também para a Tabela 1.1 (impr. 5). [00:06] **[procede]**
- 1.4: "o contexto, ~~a motivação~~, ~~os~~ objetivo~~s~~ e ~~o cronograma~~" → "o contexto **e o objetivo**". Há um objetivo só. [00:07]

### Cap. 2: Fundamentação teórica

**impr. 6 (PDF 19)**
- A introdução do capítulo ficou reduzida a "apresenta os conceitos necessários para compreender o trabalho". [00:07]
- Sobre "Quando várias grandezas… como PM2,5, PM10 e a hora do dia, a série é chamada de multivariada", ela escreveu: "**hora do dia é o próprio t, isso não é outra variável. Chama de multivariado quando tenho 2 variáveis A e B previstas ao mesmo tempo e A afeta B e B afeta A. Via de mão dupla.**" [00:07–00:10]
  - **[em parte]** Ela acerta em dois pontos: a hora do dia não é uma grandeza medida, e como só o PM2,5 é previsto, o PM10 é exógena. Então abandone "multivariado".
  - Ela erra em "hora do dia = t": a hora do dia é t mod 24, um atributo legítimo, a "entrada futura conhecida" de Lim et al. (2021). **[verificado]** Todos os seus modelos usam `hour`, `day_of_week`, `month` e 20 termos seno/cosseno (períodos 6, 12, 24, 168 e 8760 h, 2 harmônicos). Se você tirar o tema do texto, ele fica incoerente com o que foi feito. Ver impr. 8.
- "…o histórico das demais": "como mostra a equação?". Ligue o texto à equação.
- Eq. 2.1: "**fazer itemize para os itens**" (tendência, sazonalidade, resíduo) e "onde".

**impr. 7 (PDF 20): 2.2 → 2.1.1**
- Eq. 2.2: "onde".
- "…cada um formado por uma entrada e pela saída que se espera obter dela" → "por um **vetor de** entrada…", riscando "dela".
- "(de t+1 a t+H)": "a ordem que representa".
- **Riscado:** "Como as janelas se sobrepõem, o mesmo valor aparece em vários exemplos, ora como entrada, ora como saída." Ela trocou por "**E segue até percorrer toda a série.**"
- "Alguns atributos… são conhecidos de antemão…, como a hora do dia": "**Não entendi nada disso… mas hora do dia não é atributo!**" [00:11] **[em parte]**, ver impr. 6 e 8.

**impr. 8 (PDF 21)**
- **A legenda da Fig. 2.1 está circulada.** O quadrado laranja cobre o texto "valores)" da entrada. É um bug real de TikZ. **[procede]**
- Na Fig. 2.1: "numerar", ou seja, numerar o eixo do tempo.
- "**Tem que explicar o que é variável exógena! Falar antes de usar na fórmula!**". Na Eq. 2.3, sobre z: "**pode chamar isso de variável exógena!**" e "conhecidos como variável exógena". [00:12] **[procede]**
- No parágrafo "Algumas definições…": "**isso é defasagem, então deixa junto**", com uma seta mandando **subir** a definição de defasagem e de exógena para antes da Eq. 2.3.
- "Atributos de calendário… hora do dia, dia da semana e mês" está ondulado (remover). [00:25–00:28] **[em parte]**
  - Os atributos são usados, então não os apague. Reescreva como parágrafo próprio, com referência (Lim et al., 2021; Hyndman e Athanasopoulos, 2021, termos de Fourier) e com exemplo numérico, como ela pediu.
  - "Seno e cosseno são filtros suavizadores" (áudio) não se aplica: aqui eles são codificação cíclica do tempo.
- Eq. 2.4: "onde" e "**dê um exemplo numérico para deixar + claro**" **[procede]**. Exemplo pronto:
  - h = 23 → (sin, cos) = (−0,259; 0,966);
  - h = 0 → (0; 1);
  - h = 12 → (0; −1).
  - A distância entre 23 h e 0 h é 0,26; entre 0 h e 12 h é 2.

**impr. 9 (PDF 22): 2.3 Previsão multi-horizonte**
- O parágrafo "Uma variável só pode servir de atributo para um instante futuro…" está riscado: "**tirar!**". [00:11]
- As três estratégias estão riscadas: "**Não achei relevante. Você já mostrou na eq. 2.3… Só importaria uma seção se tivesse comparado as 3 formas!**" [00:13–00:17] **[não procede]**
  - **[verificado]** As 3 formas foram comparadas: LSTM recursiva, LSTM direta e Seq2Seq. XGBoost e Ridge também são diretos, com um modelo por horizonte. Pelo próprio critério dela, a seção fica, reescrita e ligada à Eq. 2.3.
  - "Recursivo é janela deslizante" está errado. A janela deslizante é como se formam os exemplos; recursivo e direto são como se produzem os H passos (Taieb et al., 2012).
  - A sugestão dela ("recursiva quando H = 1, direta quando H > 1") também está errada. As duas produzem H > 1 passos: a recursiva treina para 1 passo e reaplica o modelo; a direta produz os H passos de uma vez.

**impr. 10 (PDF 23): 2.4 → 2.1.2 Validação temporal**
- Depois de "dados novos": "**, e o que chamamos de capacidade de generalização**". Ela gostou do texto. [00:17]

**impr. 11 (PDF 24): 2.5 → 2.1.3**
- Eq. 2.5: "**e o que é o L?**" Defina L (perda/erro) e use "onde". [00:17] **[procede]**
- Subseções 2.1.3.1, 2.1.3.2 e 2.1.3.3.
- Sobre o indicador de ausência: "**Se o seu modelo não faz isso, retire esse texto, senão vai criar perguntas!**" [00:17–00:25]
  - **[verificado]** O modelo faz isso, de duas formas que você deve explicar separadamente:
    1. `PM2.5__miss` e `PM10__miss` (0/1) **entram como atributos** em todos os modelos: redes, XGBoost e Ridge.
    2. As horas com **alvo imputado ficam fora da perda e das métricas** (`ignore_imputed_target_for_loss/metrics: true`).
  - Não chame isso de "peso", como ela sugeriu no áudio.
  - Ela pediu exemplo numérico e referências: Che et al. (2018) para o indicador como entrada; Li et al. (2018) para excluir o alvo imputado do erro.

**impr. 12 (PDF 25): 2.1.3.3 Vazamento temporal**
- "Variáveis futuras… como o calendário": "**Não tem isso de calendário… pode gerar polêmicas, retirar.**" [00:25]
  - **[em parte]** Tire a frase daqui, mas o conceito precisa aparecer no parágrafo de calendário (impr. 8).
  - Explique nesta seção como o seu pipeline evita vazamento. A imputação é linear só no treino e só propaga depois do corte, refeita em cada dobra; isso responde à preocupação que você mesmo levantou [00:22]. A normalização usa só o treino.
- 2.6 → 2.2.

**impr. 13 (PDF 26)**
- "onde" nas Eqs. 2.6 e 2.7.
- Riscados "e permite" e "representar relações que não são retas", com "neural" inserido. Fica: "**que introduz não linearidade à rede neural**".

**impr. 14 (PDF 27): 2.7 → 2.2.1**
- Eq. 2.8: "**o que acontece p/ t=1?**" Explique h₀ (normalmente zero). **[procede]**
- Fig. 2.4: "**Não seria 3 camadas da LSTM?**" [00:28] **[não procede]**
  - É uma única RNN desdobrada no tempo, com os mesmos pesos em t−1, t e t+1 (Goodfellow et al., 2016, Fig. 10.3). O texto atual está certo.
- No rodapé: "**Ao invés de fazer elaboração própria, pega a imagem padrão da LSTM e a explica com equações.**" **[procede]**
  - Use a figura padrão e escreva explicitamente "desdobramento no tempo ≠ camadas empilhadas".

**impr. 15 (PDF 28)**
- "**Para falar do gradiente, mostra a equação do gradiente e um texto padrão da literatura, não o que você acha que é!**" **[procede]**
- "No primeiro caso (desaparecimento)…": "**assim parece que só o 1º tem problema**". Explique também a explosão.
- Sobre os portões: "**Só unir esses 2 textos, explique o que cada portão faz direcionando o leitor para a figura e as equações. Faça um texto + didático.**" [00:28] **[procede]**

**impr. 16 (PDF 29): 2.8 → 2.2.2**
- Fig. 2.5: "**aumentar figura**".
- Eq. 2.9: "**ligar isso com o texto da figura!**".
- "Eles têm duas partes" → "**Esse modelo é composto por**"; "que"; "o vetor de".

**impr. 17 (PDF 30)**
- "Gera a saída um elemento por vez": "**o que significa isso?**", "figura?" e "apresenta como cada estado hⱼ é calculado".
- "A janela de entrada é a sequência de entrada…": "**não entendi nada**" e "cadê a figura mostrando isso?". [00:29–00:31] **[procede]**
- "Entrada do passo j": "o vetor de" e "não entendi".
- "Esse vetor único é um gargalo": "**por quê?**". [00:32] **[procede]**
  - Você não soube responder no áudio. A resposta: o vetor de tamanho fixo precisa resumir toda a janela, e o desempenho cai com sequências longas (Cho et al., 2014; Bahdanau et al., 2014).
- "Os pesos indicam quais instantes…": "**não entendi**".
- Fig. 2.6 "adaptada": "**mostra a original ao invés de adaptado**". [00:33]

**impr. 18 (PDF 31)**
- "**Na fundamentação teórica acho importante você pegar a definição da literatura e colocar de forma didática no seu texto. Eu acho que ainda está confuso entender esse modelo!**" [00:33] **[procede]**

**impr. 19 (PDF 32): 2.9 Teacher forcing**
- No título: "**não sei onde se encaixa, se é subseção da anterior**".
- Na margem: "**Esse texto está ótimo. A figura conversa com o texto, deveria [ter] isso na seção anterior.**" Use esse estilo na 2.8. [00:33]
- No rodapé: "**+ só pode ser usado no treinamento, isso não foi falado no texto. Explique melhor!**" **[em parte]**
  - O texto já diz isso ("Durante o uso real… Durante o treinamento, porém…"). Deixe mais explícito.

**impr. 20 (PDF 33)**
- No topo: "**O que eu quero entender é por que e quando usar o teacher forcing?**" **[procede]**
  - Ele acelera e estabiliza o treino, mas cria um descompasso entre treino e uso (Bengio et al., 2015). No seu trabalho, ele só se aplica ao Seq2Seq básico.
- "Existem ainda decodificadores que dispensam a realimentação…": "**mas aí não é seu modelo**". [00:34] **[não procede]**
  - **[verificado]** É o seu modelo. As duas versões do Seq2Seq com atenção usam `decoder_strategy: semi_direct` e não realimentam previsões. Isso é o que torna o teacher forcing irrelevante para elas.
  - Explique isso aqui sem citar a Seção 4.5 para frente.
- 2.10 → 2.3 (XGBoost):
  - "por quê?" (por que uma única árvore é limitada);
  - "**cadê a figura disso?**";
  - "**como? Não entendi como funciona**";
  - "**o que significa isso?**" (regularização e recursos).
  - O ondulado em "Assim, o XGBoost é um tipo de impulsionamento… e não uma técnica distinta" significa remover a frase. [00:35]

**impr. 21 (PDF 34)**
- Na Fig. 2.8: "**i = iteração! Não significa que vou ter em i=K, K árvores; significa que a árvore da iteração K evoluiu, não é? Tenho + dúvidas disso.**" No áudio: "soma… faz a média". [00:35] **[não procede]**
  - O boosting mantém as K árvores e soma as saídas delas. Não há árvore que evolui, nem média; média é coisa de bagging e floresta aleatória. A Eq. 2.13 é a Eq. 1 de Chen e Guestrin (2016).
  - O próprio docx dela confirma: F₃ = F₀ + η·h₁ + η·h₂ + η·h₃.
  - **Ajuste que concilia as duas visões:** escreva ŷ = F₀ + η Σₖ fₖ(u), explicando F₀ e η, e use o exemplo do docx.
- Eq. 2.14: "**isso é o que o XGBoost faz?**" **[verificado]** Sim. É a função objetivo do artigo, e `reg_lambda` e `gamma` estão no espaço de busca.
- "**Usar o texto que vou te passar de XGBoost**" → `luciana4_texto_xgboost.docx`. É texto gerado por IA; revise antes de usar:
  - **Use o 2º exemplo** (calorias × idade, η = 0,5). A aritmética confere.
  - No 1º exemplo, a coluna "Erro Médio" (3,000 / 2,800 / …) está errada: é o maior resíduo, não a média. O MAE inicial é (3+1+1+3)/4 = **2,0**. Além disso, com η = 0,1 o exemplo termina longe dos valores reais.
  - "Constrói árvores em paralelo" é falso. As árvores são sequenciais; o que se paraleliza é a busca de divisões (Chen e Guestrin, 2016, Seção 4).
  - A folha "média dos resíduos" ignora λ. No XGBoost, w = −G/(H+λ).
  - Os exemplos usam perda quadrática, mas o seu XGBoost usa `reg:absoluteerror`. Diga que o exemplo é didático.
  - Cite Chen e Guestrin (2016) e Friedman (2001), não o docx.
- 2.11 → 2.4:
  - "dos parâmetros de modelo/neural", "na fase de treinamento do modelo".
  - Sobre o dropout: "**o que significa isso? o que é isso?**". Use "neurônios". [00:35]
  - Na margem: "**Seu texto não tem contexto. Várias informações jogadas.**" [00:36] **[procede]**

**impr. 22 (PDF 35)**
- "O tamanho de cada atualização": "**tamanho do que?**"
- Perda de Huber: "**Você está usando isso? É o otimizador dos hiperparâmetros que usa?**" **[verificado]**
  - Huber é a **perda do treino das redes**: δ = 1,0 por padrão, com δ ∈ {0,5; 1; 1,5; 2} na busca.
  - Os pesos são otimizados com AdamW.
  - A busca de hiperparâmetros (Optuna, TPE com Hyperband) minimiza o MAE de validação.
  - O XGBoost usa erro absoluto.
  - Ligue a fundamentação a esse uso.

**impr. 23 (PDF 36)**
- "o orçamento de treinamento" e "busca com orçamento limitado": "**o que é isso?**" nos dois. O orçamento são as épocas por tentativa (ver Seção 2). [00:36]
- 2.12 → 2.5. Riscado: "Como a previsão de PM2,5 é uma tarefa de regressão, a qualidade da previsão é medida por meio de erros."

**impr. 24 (PDF 37)**
- RMSE: "**isso é o MSE, não o RMSE… Mas tira a raiz. Tem erros na sua definição. Quais?**" [00:37] **[não procede]**
  - A frase está correta: o RMSE eleva ao quadrado antes da média e depois tira a raiz, e por isso dá mais peso aos erros grandes. A Eq. 2.19 está certa.
  - Deixe as duas etapas explícitas: quadrado, média, raiz, que volta à unidade µg/m³.
- "O MAE e o RMSE respondem a perguntas diferentes": "**quais?**". Diga quando usar cada um. **[procede]**
- MBE e habilidade: "**Você usa isso?**" [00:38] Sim; ver a tabela abaixo.

**impr. 25 (PDF 38)**
- MAE por horizonte: "**para quê? qual motivo?**" e "**Você usa isso?**". Sim. [00:39]
- 2.13 → 2.5.1. Bootstrap em blocos: "**isso pode ser usado em séries temporais? Como é feito? Quero figura e exemplo.**" e "mas não falou se você usa isso". [00:39]
  - **[em parte]** O método é o padrão para dados dependentes (Künsch, 1989; Politis e Romano, 1992). Dentro de cada bloco a ordem é preservada, então não perde a sequência.
  - Você usa blocos circulares de **168 h**, com 2000 réplicas.
  - Os pedidos de figura, exemplo e de dizer que usa procedem.

**Métricas: "Você usa isso?" (tudo [verificado] em `analyze.py` e `metricas_holdout.tex`)**

| Métrica | Onde aparece | O que falta dizer no cap. 2 |
|---|---|---|
| MBE (viés médio) | coluna MBE; viés nos eventos | sinal do erro: os modelos subestimam os picos |
| Habilidade vs. MM 24 h | coluna "Habilidade" | ganho relativo sobre a melhor referência ingênua |
| MAE por horizonte | MAE H1/H24; Fig. 5.1 | como o erro cresce de 1 h a 24 h |
| Bootstrap em blocos | IC das diferenças | se a diferença entre modelos é real |
| Diebold-Mariano | coluna p (DM) | teste complementar ao bootstrap |

### Cap. 3: Trabalhos relacionados

**impr. 27 (PDF 40)**
- "Referencial unificado e padronizado": "**Não entendi isso! O que significa?**" Tire, ou diga só o que a revisão concluiu. [00:40]
- "LSTM otimizada": "**o que é isso?**". "Decomposição por modos empíricos": "**isso é um modelo?**". "PM2,5 urbano": "**o que é isso?**". Ela também inseriu "previsão de". [00:41–00:42]
- "Modelos que incorporam informação espacial": "**isso como atributo?**" e "**que modelos?**". [00:43]

**impr. 28 (PDF 41)**
- Navegação por satélite: "**atributo?**". Camada limite planetária: "**Vc não tem esse atributo né?**" Avise que nem toda estação tem essa variável. [00:43]
- Riscado: "Alguns trabalhos comparam vários modelos na mesma tarefa, como o presente estudo."
- Seção 3.2: "**Não precisa separar em seções**". O parágrafo "Esses estudos usam configurações distintas" e a Tabela 3.1 estão riscados com X: "**Não é relevante fazer esse texto dessa forma!**". [00:43]

**impr. 29 (PDF 42)**
- 3.3 → 3.2. No áudio, ela pediu ordem **cronológica**.

**impr. 30 (PDF 43)**
- Título: riscados "Referências Simples," e "e Avaliação"; fica "Dados Faltantes". "Referências simples": "**o que é isso?**". [00:45]
- O 1º parágrafo (Makridakis/M3) está riscado em diagonal: "**tirar isso**", "não acho confiável" (séries e casos diferentes), "só para comparação" (previsão ingênua). [00:45]
- Valores ausentes (Che et al.): "**explique melhor**" e "quero trabalhos relacionados disso". Riscado: "Não encontramos trabalho de previsão de PM2,5 que discuta explicitamente essa escolha." [00:45]
- Gneiting/Diebold-Mariano: "**Não entendi nada, melhor tirar.**"
- 3.5 riscada com X: "**+ isso não é um diferencial; todo trabalho que compara faz isso.**" [00:46]

**impr. 31 (PDF 44): página escrita à mão**
> **Cap. 3 tem que ter 2 seções:**
> **3.1 Trabalhos relacionados sobre previsão de PM2,5:** trazer o que foi feito, quais modelos foram usados, variáveis usadas, horizontes e locais, e dizer qual modelo foi melhor.
> **3.2 Trabalhos relacionados à imputação de dados ausentes em séries temporais:** para dizer quais métodos são **mais** empregados (só vi uns 2 de relevante).

### Cap. 4: Materiais e métodos

**impr. 32 (PDF 45): 4.1 Dados**
- Na introdução do capítulo: "**Tudo bem deixar isso claro aqui, mas isso não é um diferencial do seu trabalho. Todos fazem assim.**"
- "Estação Sapo": "**por que foi escolhida essa estação?**". Suba a escolha da estação para antes. [00:49]
- No áudio, ela pediu ainda a tabela `df.info()` e o gráfico da série completa. [01:00, 01:11]
- Partículas totais (86 % de cobertura): "**Não entendi.**" **[verificado]**
  - A coluna `PTS` existe, com 86 % de cobertura.
  - Correlações: PTS × PM10 = **0,90**; PTS × PM2,5 = **0,43**; PM10 × PM2,5 = 0,60.
  - Em 30 % das horas PTS < PM10. Isso é fisicamente inconsistente, porque as partículas totais contêm o PM10.
  - Ou escreva uma frase ("não usada por ser quase redundante com o PM10, com correlação de 0,90, e menos associada ao PM2,5"), ou remova, como ela mandou. Se remover, a menção na Seção 4.4 também sai.
- "Os primeiros 34.992 registros… etapas exploratórias… 2021 a 2023 não foram usados…": "**Não entendi nada!**". [00:51]
  - Escreva "estudos preliminares" e reescreva com a estrutura da Seção 1.2.

**impr. 33 (PDF 46): 4.1.1 Escolha da estação**
- Marcas:
  - "cobertura do alvo": "**que alvo?**";
  - "eventos de alta concentração": "**não entendi**";
  - "volume suficiente" e "variável auxiliar útil": "**o que é isso?**".

  [01:03–01:05]
- Na margem: "**Faça pergunta lá em cima, direcionando a explicação para uma seção!**"
- Sobre o parágrafo e o gráfico: "**Não entendi nada, precisa melhorar seu texto. Pense que vai dar uma aula sobre isso.**" [01:06–01:09] **[procede]**
- **Por que o parágrafo é contraditório:**
  - O gráfico é uma "pontuação de previsibilidade" que **premia poucos picos e baixa variabilidade**: as colunas `score_menos_picos` e `score_baixa_variabilidade` do ranking.
  - O texto diz que não quer "a estação mais previsível".
  - Depois o texto descarta a 1ª colocada justamente por ter poucos picos.
  - Ou seja, o critério do gráfico e o critério do texto se opõem.
- **Atenção:** o critério que ela sugeriu (mais dados preenchidos e, no empate, menor dispersão) **escolheria Rio Doce**. **[verificado]**

| | Rio Doce | Sapo |
|---|---|---|
| Período com dados | 2020–2023 (4 anos) | 2017–2023 (7 anos) |
| Horas de PM2,5 medidas | 29.965 | **51.205** |
| Cobertura de PM2,5 | 85,5 % | 83,5 % |
| Desvio-padrão (µg/m³) | 5,41 | 7,22 |
| Horas > 35 µg/m³ | 0,19 % | 1,16 % |
| Correlação PM2,5–PM10 | 0,52 | 0,58 |

- **Texto sugerido:**

  > A estação foi escolhida entre as 38 estações da FEAM com medições de PM2,5, por três critérios: (i) volume de horas com PM2,5 medido; (ii) PM10 medido no mesmo horário, para uso como variável exógena; (iii) presença de picos em número suficiente para avaliar os modelos nesses momentos. A Tabela X compara as duas estações com maior cobertura. Rio Doce tem cobertura percentual ligeiramente maior (85,5 % contra 83,5 %), mas só possui dados a partir de 2020. Sapo tem sete anos de série (2017–2023), com 51.205 horas medidas contra 29.965, mais horas acima de 35 µg/m³ (1,16 % contra 0,19 %) e PM10 mais correlacionado ao PM2,5 (0,58 contra 0,52). Por isso, Sapo foi escolhida.

- Tire o gráfico de pontuação, ou mande-o para o apêndice. Tire também "não pertence ao mesmo município", que não é critério.

**impr. 34 (PDF 47): 4.1.2 Cobertura e lacunas**
- Ela trocou "sobretudo na validação" por "**ao longo da série**".
- "48,25 dias" e "8,5 dias": "**dia quebrado?**" Escreva "1.158 horas (cerca de 48 dias)". [01:12]
- Fig. 4.2: "**para mostrar treino, validação e teste, primeiro tem que falar disso**". Suba a divisão dos dados. "**O que é artefato final?**": troque por "conjunto de dados". [01:11–01:12]
  - **[verificado]** As cores estão corretas para o treino final. Inclua 2021–2023 na figura e explique a validação cruzada da busca (Seção 1.2).
- "A Tabela 4.1 resume cada bloco cronológico": "**Passe isso p/ frente**". "Teste histórico": ela não aceita o termo. [01:13]
- Coluna "Entrada propagada": "**explicar melhor, o que é isso?**" É a repetição do último valor depois do corte (imputação causal). [01:14]
- "Eventos de concentração alta": use "picos". [01:14]
- "…não são tratadas como ciclo regular, pois o conjunto cobre apenas sete anos": "**Não entendi.**" Diga que não foi detectada sazonalidade anual em 7 anos (autocorrelação anual de 0,04) e descreva os padrões diário e mensal. [01:15–01:16]

**impr. 35 (PDF 48): 4.1.3 Padrões temporais**
- "Período de desenvolvimento": "**desenvolvimento do quê?**" [01:17]
- Fig. 4.3: "**praticamente a mesma série. Verifique se não tem erro nessa decomposição.**" [01:17] **[em parte]**
  - **[verificado]** Não há erro de cálculo. O script (`TCC-RELATORIO/scripts/gerar_figuras_fundamentacao.py:108`) faz a decomposição clássica: a tendência é uma média móvel centrada de 7 dias, e o padrão horário é a média por hora.
  - O ciclo diário explica só cerca de **4 %** da variância, a tendência cerca de 57 % e o resíduo cerca de 35 %. Por isso o resíduo "parece" a série. Isso é um resultado e precisa ser explicado no texto.
  - Há dois problemas reais, que se resolvem regenerando a figura, sem treino:
    1. O texto diz "apenas pontos medidos", mas o código usa a série **com valores imputados**.
    2. O trecho plotado (ago.–nov./2020) é o teste de 2020, não o treino.
- Autocorrelações: "**explica melhor como isso foi calculado**" e "**para que foi feito isso? No que te ajudou?**" [01:18–01:22]
  - **[verificado]** Os valores da Tabela 4.2 estão corretos: 0,813 (1 h), 0,681 (24 h), 0,598 (48 h) e 0,461 (168 h), recalculados do CSV. No áudio ela leu 0,83 e 0,61.
  - Para que servem: justificam L = 48 (dois ciclos diários, com ρ = 0,60 em 48 h), as referências ingênuas t−24 e t−48 e o PM10 como exógena.
  - Pode ir para o apêndice.

**impr. 36 (PDF 49): 4.2**
- PM10 (correlação 0,597): "**explique que por isso vai ser usado como var. exógena!**"
- Autocorrelação anual de 0,04: "**o que isso quer dizer? o que ajuda na previsão?**" Que repetir o mesmo dia do ano anterior não ajuda.
- Título: "**que tarefa? Horizonte de previsão**" e "**Não, melhorar isso!**"
- Sobre "Resolução nº 491/2018 (CONAMA)": "**o que é isso?**". [01:24] **[procede]** Tire a resolução deste ponto.
  - **[verificado]** A resolução não trata de previsão. Ela define **padrões de concentração** de poluentes, cada um ligado a um **período de exposição** (média de 24 h, média anual).
    - Nem a 491/2018 nem a 506/2024 têm artigo sobre previsão ou horizonte de previsão.
    - O "24 horas" da resolução é a **média diária** que se compara com o limite. O seu modelo prevê **24 valores horários**, não a média do dia. Então "corresponde à escala do padrão de 24 h" não justifica a escolha. Você mesmo disse no áudio que não foi por isso.
  - **[verificado]** A Resolução CONAMA nº 506, de 5/7/2024, art. 11, I, **revogou os arts. 1º a 8º, 12 a 14 e o Anexo I** da 491/2018. O Anexo I era a tabela de padrões, inclusive o valor de 37 µg/m³ citado na Seção 4.7.
    - O texto cita como vigente uma tabela já revogada.
    - O `.bib` diz "Revogada", mas a revogação foi **parcial**.
  - **Justificativa honesta para H = 24:**
    1. Previsão para o dia seguinte, uma escala usual de alerta e planejamento.
    2. Estudos preliminares: a escolha L = 48 → H = 24 fica no apêndice ou na 5.9.1, citada para trás.

    Não use a resolução para isso.
  - **Seção 4.7, limiar de 35 µg/m³:**
    - Ou cite a **506/2024**, conferindo o valor no Anexo I dela.
    - Ou, mais simples, use a **meta intermediária 3 da OMS para 24 h, 37,5 µg/m³** (World Health Organization, 2021, já citada no trabalho).
  - **O que existe dos estudos de janela:**
    - **Entrada.** A Seção 5.9.1, no protocolo final, compara 24, 48, 72 e 96 h na validação.
      - LSTM direta: 2,842 / **2,808** / 2,832 / 2,829.
      - XGBoost: 2,845 / 2,804 / 2,787 / 2,772.
      - O estudo preliminar está em `TCC-RELATORIO/artefatos/analise_janela_entrada_sapo.md` (Ridge 24/48/168 h: 2,764 / 2,767 / 2,824).
    - **Horizonte (saída).** Não achei comparação utilizável. Só há estudos antigos de 12 h e 72 h na estação Cascata (Optuna), de outro escopo. Então não diga que o horizonte de 24 h foi otimizado; ele é uma decisão de projeto.
- Sobre "L = 48… referências simples (Seção 4.5.2)" e "Seção 5.9.1": "**Não entendi nada!**", "**isso é p/ trás, não p/ frente. Não pode fazer fora da ordem**". [00:58–01:26]
  - Escreva que, em estudos preliminares, a janela de 48 h de entrada para 24 h de saída foi a melhor. O detalhe vai para o apêndice ou para a 5.9.1, referenciado para trás.

**impr. 37 (PDF 50): 4.2.1**
- "As estatísticas de normalização": "**o que é isso?**" Diga que são a média e o desvio-padrão do treino. [01:25] **[verificado]** É assim que o código faz.
- "Limites de etapas exploratórias anteriores (70 % e 15 %)": "**o que é isso?**" **[verificado]** 24.495 h e 5.248 h de 34.992 h.
- "Teste histórico": "**o que é isso?**". "Evidência confirmatória… holdout": "**não entendi nada**". [01:26]
  - Resolva com a simplificação da Seção 1.2.

---

## 5. Ordem sugerida
1. **Cap. 4**, como ela pediu:
   1. Dados: `df.info()` e a série completa.
   2. Escolha da estação, com a tabela.
   3. Divisão temporal: uma figura de 2017 a 2023, mais o parágrafo sobre validação cruzada da busca × treino final.
   4. Lacunas.
   5. Padrões temporais, dizendo para que serve cada um.
   6. Horizonte de previsão.
   7. Tabela dos modelos (Seção 1.3).
2. **Cap. 2:** renumerar, cortar o que foi riscado, manter a 2.3 e reescrever calendário/seno-cosseno, LSTM, Seq2Seq e XGBoost com figuras padrão.
3. **Cap. 3:** duas seções.
4. **Cap. 1 e resumo** por último.
5. **Figuras sem retreino:** 2.1 (legenda), 4.2 (incluir 2021–2023) e 4.3 (só pontos medidos e trecho do treino).

## Anexo: onde conferi
- Protocolo: `TCC-wsl/scripts/thesis/` (branch `revisao-luciana4`) (`protocol.py`, `baselines.py`, `xgb_runner.py`, `analyze.py`) e `configs/thesis_protocol.yaml`.
- Dataset: `TCC-wsl/src/data/thesis_dataset.py`, `src/data/processing.py` (`compute_station_stats`) e `runtime/reports/thesis_protocol/datasets/clean_pm10_decoder_proxy.json`.
- Dados brutos: `TCC-wsl/data/OUTRAS_USINAS/consolidado-conceicao-do-mato-dentro-sapo.csv`.
- Ranking: `TCC-RELATORIO/artefatos/eda_sapo_station_ranking_top10_tcc.csv`.
- Tabelas: `TCC-RELATORIO/tex/tabelas/metricas_holdout.tex`, `matriz_holdout.tex` e `pareado_holdout.tex`.
