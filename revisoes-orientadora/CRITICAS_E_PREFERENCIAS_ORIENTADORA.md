# Críticas e preferências da orientadora (consolidado das rodadas 1, 2 e 3)

Fontes (todas relidas do zero em 2026-09-29):

| Rodada | Data | Material | Cobertura |
|---|---|---|---|
| 1 | 15/06/2026 | 7 áudios (`luciana1_transcricao.md`) + `luciana1/TccDaniel.pdf` | Resumo e Capítulo 1 |
| 2 | 16/06/2026 | 13 áudios (`luciana2_transcricao.md`) + `luciana2/TccDaniel.pdf` | Capítulo 2 inteiro (o Capítulo 1 igual à rodada 1) |
| 3 | 25/09/2026 | Chamada de 22 min (`luciana3_transcricao.md`) + PDF comentado | Resumo e Capítulo 1 (versão reescrita) |

A leitura das marcas manuscritas está em `anotacoes_manuscritas_pdf.md`, com a confiança de cada leitura. Os capítulos 3, 4, 5 e 6
**ainda não foram lidos por ela**: tudo o que este arquivo diz sobre eles é extrapolação dos princípios abaixo (marcada como tal).

---

## 1. Como ela trabalha (processo)

- **Um capítulo por vez.** Ela só avança quando o anterior está fechado: "vou pedir para você arrumar isso primeiro, para a gente fechar
  esse capítulo, aí eu vou falar 'o primeiro está legal, vamos para o próximo'". Na rodada 3 ela ainda estava no Capítulo 1.
- **Lê e comenta o PDF, não o LaTeX.** "Eu prefiro ler o PDF mesmo, como se estivesse pronto." Não se importa com GitHub ou Overleaf.
  Pediu: ao terminar o Capítulo 1, **gerar o PDF e mandar por WhatsApp** para ela pegar a última versão.
- **Ritmo semanal.** Propôs um dia fixo por semana para ela ler o que foi entregue. Daniel só não tem aula às quartas; o áudio cita os dias 16, 17 e 18 e fecha em 18 (mês não dito; reconhecimento de voz pouco nítido nesse trecho).
- **Uso de IA é permitido.** "Pode usar IA, e explica o que você quer." O limite é **não colocar coisas polêmicas ou erradas**
  (exemplo dela: a afirmação de que o XGBoost seria "para dados tabulares" e a rede neural para séries).
- **O resumo fica por último** ("deixa o resumo para depois, depois a gente reformula").
- **Tolera "por enquanto"** quando o detalhe vem depois no texto (por exemplo, definir "curto prazo" mais à frente), desde que o leitor
  não fique perdido.
- Ela quer conversar sobre os **resultados/gráficos** quando os capítulos anteriores estiverem fechados (já abriu o assunto).
- Contexto: ela pretende, depois do TCC, escrever um **artigo** com Daniel para um congresso Qualis (o áudio cita siglas de eventos, como "SPC", que o reconhecimento de voz não distingue bem); é um objetivo posterior e não altera o TCC.

## 2. Princípios de escrita que ela repete (ordem de frequência)

**P1. Definir antes de usar; sigla depois da explicação.**
"Coloca a sigla depois da explicação, não antes." Escrever o termo por extenso, explicá-lo, e só então a sigla (PM2,5, PM10, PM).
O mesmo vale para símbolos: ela cobrou L, h, y, ȳ, ρ, N, ε, p_TF, b_{i,k}, θ, "estado interno" e "gates" no ponto em que aparecem pela primeira vez.
"A primeira vez que vai mostrar alguma coisa, você tem que detalhar tudo." Se algo foi definido lá em cima, embaixo pode usar sem detalhar.
Ela nota quando a ordem está invertida ("você usa L aqui e só descreve lá na frente").

**P2. Texto, figura e fórmula têm que andar juntos.**
"Figura não é autoexplicativa." O texto deve **direcionar o olhar**: "observe na Figura 2.1: na partição 1, o treino ocupa o bloco 1 e a validação o
bloco 2; na partição 2..." e ligar cada trecho da fórmula ao pedaço da figura. A figura deve vir **antes** do texto que a usa, e não solta no fim.
Quando não há figura, ela pede uma (estado interno, LSTM, Seq2Seq, teacher forcing, janela deslizante, boosting).
Prefere **figuras padrão da literatura** (LSTM com gates, Seq2Seq do artigo original) às feitas por ele: as dele foram consideradas "muito pequenas,
espremidas, confusas". Se mantiver as próprias, o texto precisa explicar fórmula por fórmula usando a figura.

**P3. Toda equação em `equation` com `\label` e citada com `\ref`.**
Não usar `$$...$$`. E **explicar todos os elementos** de cada fórmula, sempre.

**P4. Notação padrão da literatura.**
Saída do modelo como y (ŷ), não como o ou h sem definição; padronizar entre figura e fórmula (Fig. 2.2b usa "o", a fórmula usa "h").

**P5. Afirmação incomum exige referência, e apresentada como escolha daquela referência.**
Sobre separar valor imputado de observado: "nunca vi isso… geralmente a gente imputa e trata normal. Você pode destacar que **essa referência fez isso e que você
achou importante replicar** no seu trabalho". Vale também para "recursiva/direta/codificador-decodificador" (uma referência de aplicação para cada) e para o texto do
Teutsch e Mäder. Pergunta-padrão dela: "**que referência comprova isso?**"

**P6. Cada capítulo cumpre o seu papel.**
- Introdução: problema, dificuldade, lacuna na literatura, o que este trabalho faz (alto nível). **Sem metodologia** (janela, recorte, 48/24, métricas, variáveis).
- Fundamentação (Cap. 2): **só conceitos e como o modelo funciona.** "Isso já é trabalho relacionado. Você não fala aqui." A aplicação em séries temporais fica
  no Capítulo 3.
- Justificativa da escolha da estação: na **metodologia**, "não precisa falar aqui".

**P7. Motivação é o que fez você querer o trabalho, não um resumo do trabalho.**
"Isso está genérico, não é o que motivou esse trabalho." E "não tem que separar 'problema de pesquisa'; isso está na introdução". Ver §3.

**P8. Não dizer coisa falsa ou polêmica.**
Casos concretos: (a) "a comparação entre trabalhos nem sempre é direta" (falso: "alguns são comparados diretamente sim"); (b) XGBoost como "referência tabular forte" e rede
neural como outra coisa (as duas precisam da série virar um problema supervisionado, com entrada e saída; isso é o janelamento); (c) "acurácia" para regressão ("acurácia é
métrica de classificação"; usar "qualidade de previsão"); (d) "aprendizado de máquina **e** aprendizado profundo" (profundo é um caso de máquina).

**P9. Enxugar.**
Cortar explicações redundantes ("isto é, sequências de valores observados ao longo do tempo": quem lê a introdução já sabe), a palavra "experimental" (computação não
"colhe partículas"), o "Resumo do Capítulo" (não é necessário), parágrafos soltos sem contexto (atenção "não deve ser interpretada como explicação causal") e títulos
que prometem mais do que o texto entrega ("análise por horizonte" com um parágrafo).

**P10. Cada "o que é isso?" é um sinal de que faltou definir.** Lista completa na §5.

## 3. O que ela quer no Capítulo 1 (especificação, instruções da rodada 1 + refinamentos da rodada 3)

Estrutura da introdução, na ordem dela:

1. **Problema do PM2,5, detalhado, em um parágrafo** (não resumido): o que é material particulado, por que "fino", que problemas de saúde causa,
   **mortalidade/internações**, com referências ("é fácil de achar na literatura"). Deve destacar por que prever ajuda a prevenir.
2. **Dificuldade de prever a série** (genérica): séries meteorológicas/ambientais têm lacunas, ruído de medição, mudanças de comportamento, picos raros, e
   dependem de fatores (meteorologia, emissão, dispersão, outros poluentes) que nem sempre estão disponíveis. **Não** introduzir "série temporal"
   com definição aqui (isso é do Capítulo 2). Ela reescreveu a frase: "As medições de qualidade do ar formam séries temporais **que** podem apresentar lacunas, ruídos de
   medição, mudanças de comportamento e picos pouco frequentes. Além disso, a concentração depende de fatores como condições meteorológicas, emissão de poluentes, dispersão
   no ar e relação com outros poluentes, **que** nem sempre estão disponíveis de forma completa no momento em que a previsão precisa ser feita." e **cortou** a frase
   "modelos de previsão precisam estimar valores futuros a partir de informação parcial e de dados ambientais imperfeitos" ("não existe dado perfeito").
   Mantém "prever PM2,5 não é uma tarefa simples".
3. **Lacuna na literatura**: já se usam modelos de aprendizado profundo para prever PM2,5 e séries meteorológicas, com **modelos diferentes**, sem consenso de qual é melhor
   e sem comparativo. Colocar referências. **Não** afirmar que "a comparação entre trabalhos nem sempre é direta" (foi cortado), nem discutir validade cronológica aqui.
4. **O que este trabalho faz** (alto nível): "estudo comparativo para previsão horária de curto prazo de PM2,5, **utilizando diferentes modelos e arquiteturas**
   (LSTM, Seq2Seq, XGBoost)", com estudo de caso na série da estação Sapo (Conceição do Mato Dentro, MG; dados da FEAM), **movido para o fim do parágrafo**. Pode dizer no final
   qual modelo teve melhores resultados, sem métricas. Pode manter a ideia: "buscar responder não apenas qual modelo tem menor erro de predição, mas em que condições cada
   abordagem é mais adequada". **Nada** de janelamento, 48/24, recorte, métricas, "multissaída", "referência tabular forte".

**1.1 Motivação**: por que fazer o trabalho. Modelo dela: a série é complexa (dados faltantes, dificuldades típicas de séries meteorológicas); a literatura emprega estruturas
cada vez mais variadas (desde LSTM simples até modelos recentes); isso motivou comparar essas arquiteturas **nesta** série. Sem "motivação prática e metodológica", sem
48/24 h, sem "a comparação é relevante porque…" genérico. **Remover a seção "Problema de Pesquisa"** e a "pergunta que orienta este TCC" (não fez sentido).

**1.2 Objetivos**: **objetivo geral** obrigatório (estava faltando), sem "na estação Sapo". "Curto prazo" precisa ser **quantificado** (um passo à frente? quantas horas? um
dia?): usar o horizonte de 24 h. Os específicos comparam modelos (podem nomear LSTM/Seq2Seq/XGBoost, sem detalhar as arquiteturas), definem o protocolo rastreável e avaliam o resultado.
Detalhes vão para a metodologia.

**1.3 Organização**: ela considerou adequada ("a organização do trabalho também está legal").

**Resumo**: só depois que o Capítulo 1 fechar. Feedback já dado: não usar "recorte CMD", "presença pareada", "ocorrência suficiente", "mascaramento",
"LSTM direta", "variáveis auxiliares futuras" (o leitor não sabe o que são); "emissão do quê?"; simplificar; corrigir "aprendizado de máquina e profundo";
"Porém, a previsão não é trivial"; "diferentes modelos"; sigla PM2,5 após a explicação.

## 4. O que ela pediu no Capítulo 2 (rodada 2), por seção

| Seção atual | Pedido |
|---|---|
| Abertura | Cortar "horária multi-horizonte" e "conhecidas no momento da previsão" |
| 2.1 PM2,5 e Monitoramento | **Mover para a introdução** ("a primeira coisa é definir o problema"). Sai do Capítulo 2 |
| 2.2 Séries Temporais Multivariadas | Título só "Séries Temporais"; explicar série temporal e **diferenciar univariada de multivariada** no texto; definir y, ȳ, ρ(ℓ), ℓ |
| 2.2.1 Validação cruzada / walk-forward | Fórmula em `equation`; explicar os termos de L_CV; texto conduz a Figura 2.1 (partição 1: treino = bloco 1, validação = bloco 2…; **o bloco final é o conjunto de teste reservado desde o início**); dizer treino, validação e teste |
| 2.3 Previsão Multi-Horizonte | Definir L antes de usar; "Na literatura encontramos trabalhos utilizando…"; **uma referência de aplicação para cada estratégia** (recursiva, direta, codificador-decodificador) |
| 2.4 Dados faltantes, imputação e vazamento | Separar: (i) o que são dados faltantes, (ii) métodos clássicos de imputação, (iii) o que é vazamento temporal e como evitá-lo, **com exemplos**; a distinção observado × imputado é incomum, precisa de referência e ser apresentada como escolha dela |
| 2.5 Janelas e variáveis exógenas | **Vem antes** da validação cruzada e da previsão multi-horizonte; desenho: série contínua → tabela de entrada/saída → janela deslizante; definir defasagens explícitas, variáveis exógenas, atributos de calendário, termos periódicos; justificar por que valores futuros observados não podem ser usados; cortar a frase confusa sobre decodificador |
| 2.6 Redes neurais | Saída como y/ŷ (não o/h); definir h; padronizar figura e fórmula; explicar a camada (usa a anterior); equações em `equation` |
| 2.7 RNN e LSTM | Definir "estado interno" com figura; explicar gradiente que some/explode antes; **figura padrão da LSTM com gates**, fórmulas ligadas à figura; a figura própria "não ajuda" |
| 2.8 Seq2Seq e atenção | Figura padrão da literatura, maior; equações numeradas e ligadas à figura; **mover aplicações em séries temporais (Wen et al., DeepAR, TFT) para o Cap. 3**; cortar o parágrafo sobre "pesos de atenção não são causais" (ou justificar bem) |
| 2.9 Teacher forcing / scheduled sampling | Explicar decodificador autorregressivo primeiro; figura de teacher forcing; exemplo; definir Bernoulli, p_TF, b_{i,k}, currículo, free running; "existe série não contínua?"; separar as duas figuras; texto ligado a elas; referência para o trecho de Teutsch e Mäder; trocar NRMSE por "métricas" |
| 2.10 Impulsionamento por gradiente / XGBoost | Nome completo "impulsionamento por gradiente" (gradient boosting em inglês); XGBoost é um tipo de gradient boosting (deixar claro, e título só "XGBoost" ou explicar); **remover a dicotomia "tabular × redes"**; figura + texto + equação alinhados; parágrafo dos dados faltantes "não entendi" |
| 2.11 Treinamento, perda e HPO | Definir HPO, agenda (de taxa de aprendizado), perda de Huber; descrever os elementos de J(θ) e J_w(θ); explicar por que hiperparâmetros são difíceis de ajustar à mão e o que o Optuna faz; o texto "parece resumido demais" |
| 2.12 Métricas | Não usar "acurácia" (é de classificação): "qualidade de previsão"; definir N, y, ŷ, ȳ, ε; conferir a fórmula do MAPE; **referência para calcular métricas só nos pontos observados**; a subseção fala de análise por horizonte mas só tem um parágrafo: mostrar como é feita |
| 2.13 Resumo do Capítulo | Remover ("não é necessário") |

Além: **títulos que ainda não estão prontos** para ela (2.10 e 2.11) e a fluidez geral: "o fluxo está um pouco confuso; a primeira coisa a explicar é como os dados são
estruturados (janelamento), depois validação cruzada, imputação…".

## 5. Termos que ela não entendeu ("o que é isso?")

`presença pareada`, `recorte (CMD)`, `ocorrência suficiente`, `mascaramento`, `LSTM direta`, `variáveis auxiliares futuras`, `desenho de validação`, `validade experimental`,
`fonte bruta`, `emissão` (do quê?), `estado interno`, `desaparecimento/explosão de gradientes`, `gates`, `normalização`, `vazamento temporal`, `defasagens explícitas`,
`variáveis exógenas`, `atributos de calendário`, `termos periódicos`, `decodificador autorregressivo`, `Bernoulli`, `currículos`, `free running`, `séries contínuas`,
`HPO`, `agenda`, `perda de Huber`, `h`, `θ`, `ε`, `ȳ`, `L`, `p_TF`, `b_{i,k}`, `tabular`, `janelamento`.
**Regra prática:** nenhum desses termos pode aparecer sem definição no ponto do primeiro uso, e nenhum entra na introdução nem no resumo sem uma frase de explicação.

## 6. Minha leitura: decisões que ela deixou em aberto ou que exigem cuidado

1. **"Curto prazo" e "não falar de 48/24".** Ela quer o horizonte quantificado nos objetivos, e ao mesmo tempo nada de janelamento na introdução. Proposta: objetivo geral com
   "previsão horária de PM2,5 para as próximas 24 horas"; a janela de 48 h e o recorte ficam na metodologia.
2. **Estação Sapo.** Fora do objetivo geral; presente no fim do parágrafo 4 da introdução como estudo de caso; a justificativa da escolha fica no Capítulo 4.
3. **XGBoost.** Dizer só "modelo de aprendizado de máquina baseado em árvores (impulsionamento por gradiente)". Nada de "tabular forte", "multissaída" ou comparação de "natureza dos dados".
   No texto atual do Capítulo 4 o XGBoost por horizonte precisa ser descrito sem essa dicotomia.
4. **Métricas somente nos pontos observados.** Ela nunca viu isso. Referências que encontrei: DCRNN (Li et al., 2018) exclui valores ausentes de MAE/RMSE/MAPE; Che et al. (2018) trata a
   ausência como informação de entrada; Little e Rubin (2019). Não achei artigo de PM2,5 que trate disso, e o texto deve dizer isso com franqueza e apresentar a escolha como decisão
   metodológica com análise de sensibilidade (já existe).
5. **Atenção.** O parágrafo sobre interpretação da atenção foi cortado no Capítulo 2. O tratamento (contraprova, comparação com pesos uniformes) pode voltar em Metodologia/Resultados, onde há
   contexto para justificá-lo (ela mesma disse: "se for muito relevante, explique e contextualize mais").
6. **Figuras próprias.** As figuras conceituais (LSTM, Seq2Seq, XGBoost) foram feitas por ele e ela prefere as padrão. Decisão: substituir a LSTM e o Seq2Seq por figuras padrão da
   literatura com permissão/licença adequada ou redesenhar seguindo fielmente a figura de Hochreiter e Schmidhuber (gates) e de Bahdanau et al./Luong et al., com legenda
   "adaptada de".
7. **Tom da introdução.** Ela quer uma introdução que **motive o leitor a continuar** ("se a introdução já está com o texto ruim, a pessoa fala 'nem quero ler'"): história do problema,
   mortes/internações, dificuldades reais, lacuna. É mais narrativo e menos técnico do que o resto do documento.

## 7. Implicações para os capítulos que ela ainda não leu (extrapolação)

Os problemas que ela apontou nos Capítulos 1 e 2 são estruturais e vão se repetir nos Capítulos 4 a 6, que já foram reescritos com muita terminologia interna:

- **Jargão sem definição** no texto atual: "contrato de atributos", "recorte CMD", "faixas de defasagem", "mascaramento", "holdout", "piso de ruído", "presença pareada",
  "sensibilidade", "origem", "semi-direto". Cada um precisa de definição no primeiro uso ou de substituição por linguagem comum.
- **Figuras e tabelas** precisam de parágrafo que diga o que olhar (o texto do Capítulo 5 tem tabelas com placeholders; cada tabela precisa de "observe que…").
- **Equações** do Capítulo 2 e do Capítulo 4 (métricas, bootstrap, Diebold-Mariano) em `equation` com `\label` e todos os símbolos definidos.
- **Afirmações sem referência** ("nunca vi isso"): tudo que for decisão de projeto (limiar de 35 µg/m³, pesos da perda ponderada, janela de 48 h) deve ser declarado como decisão e
  ter a sensibilidade/ablação como suporte.
- **Cada capítulo no seu papel:** metodologia não faz revisão, fundamentação não descreve o experimento, resultados não repetem a definição.

## 8. Checklist de revisão de qualquer trecho (derivado das três rodadas)

- [ ] Todo termo, sigla e símbolo está definido no primeiro uso, com a sigla **depois** da explicação?
- [ ] O parágrafo motiva, ou só resume? (Motivação = por que quis fazer.)
- [ ] Está no capítulo certo (conceito no 2, aplicação na literatura no 3, decisão no 4)?
- [ ] Cada figura/fórmula é chamada no texto **antes**, com instrução do que observar, e tem `\label`/`\ref`?
- [ ] Notação padrão (y, ŷ) e igual entre figura e fórmula?
- [ ] Toda afirmação não trivial tem referência, ou está dita como escolha do trabalho?
- [ ] Nada falso ou polêmico (tabular, "acurácia", "estudo experimental", "comparação nunca é direta")?
- [ ] Nada redundante (resumo de capítulo, "isto é…" óbvio, parágrafo sem contexto)?
- [ ] O leitor da introdução entende sem saber o que é janela, recorte, contrato ou métrica?
