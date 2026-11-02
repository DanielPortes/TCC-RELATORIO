# Transcrição do áudio da orientadora, Rodada 4

Origem: `Revisoes-orientadora/luciana4/Luciana correção 4.m4a` (reunião de 1 h 30 min aprox., transcrição automática com separação de falantes; o áudio não está no repositório). PDF comentado: `luciana4_pdf_anotado.pdf` (versão de 05/10/2026; marcas do Resumo até a p. 37 impressa, na Seção 4.2.1). Texto sobre XGBoost que ela enviou: `luciana4_texto_xgboost.docx`. Análise ponto a ponto: `luciana4_resumo_das_correcoes.md`.



**Daniel** [00:00:00]
Oi, Luciana, tudo bem com você? 

**Luciana** [00:00:03]
Tudo jóia. Tô atrasadaça com o seu texto, mas eu tava lendo, aí eu falei, nossa, vou ter que perguntar pra ele, deixa eu ver se eu tô com o texto certo. Eu compartilhei aqui, eu anotei, deixa eu ver, eu acho que eu abri um negócio errado. PDF, eu abri coisa errada por aqui. Não, aqui não, a coisa tá certa, porque, nossa, eu odeio esse tablet, eu não consigo ordenar as coisas no meu dia a dia, peraí, deixa eu ver aqui onde eu tô compartilhando, você tá vendo minha tela, não tá? 

**Daniel** [00:00:44]
Tô, eu tô vendo o PDF. 

**Luciana** [00:00:47]
É isso. Então, aqui, comecei a ler, e aí, a única coisa que eu chamei atenção aqui, né, o inglês aqui, o PN maiúsculo, e aqui, eu já comecei a não gostar dessa parte aqui, que você vai falar só os resultados indicam que o XGBoost e a regressão linear tiveram os menores erros médios. Para por aqui, porque isso tudo aqui, aí eu escrevi aqui, porém todos os modelos subestimaram os picos de concentração. Depois eu vejo no resultado se tem mais alguma coisa. Esse aqui conclui que a escolha do modelo alterou pouco a qualidade da previsão. Não sei, não gostei desse texto, não pedi para tirar. Mas não é esse o problema. Deixa eu ir lá, porque eu quero entender mais o que você fez Aqui, então, eu já te passei esse texto Pode ir arrumando algumas coisas E aqui é uma coisa que eu queria perguntar Porque lá em cima você fala que você usou regressão linear Você usou regressão linear como um dos modelos de comparação, não é? 

**Daniel** [00:01:59]
É, foi.

**Luciana** [00:02:03]
Você usou LSTM e simplesmente o modelo padrão também? 

**Luciana** [00:02:07]
Peraí, vamos lá Você usou LSTM Essa seq2seq Um XGBoost E regressão linear 

**Daniel** [00:02:16]
Sim 

**Luciana** [00:02:17]
Foi quatro, quatro modelos 

**Daniel** [00:02:21]
É Ele não é exatamente Um modelo, é simplesmente pegar o 

**Luciana** [00:02:28]
Não, é modelo É modelo, de qualquer jeito Tipo assim O LSTM é um modelo Se você aplicou seq2seq é outro modelo. Sim. 

**Daniel** [00:02:40]
Então, lá no final, se não me engano, eu coloco, simplesmente, por exemplo, pegando a média do dia anterior. 

**Luciana** [00:02:47]
Não, calma, Daniel. Quero saber o seguinte. O que que você fez comparativo? Você rodou quatro modelos. Sim. Diferentes. A LSTM, esse que você colocou o seq2seq, o XGBoost e usou regressão linear como modelo de comparativo. então aqui na introdução porque lá no resumo você fala de regressão linear aqui você não colocou, então tem que colocar regressão linear aqui aqui o que você chama de uso como caso principal não, é o estudo de caso que você usa a estação Sapo, beleza aí eu pedi pra tirar essa sessão de motivação e deixar o texto corrido porque um parágrafo só de motivação não é motivação e eu acho que isso aqui está mais ligado aqui do que criar uma sessão depois se precisar a gente cria uma sessão mas não precisa da sessão de motivação os objetivos já fiquei preocupada porque o objetivo geral desse trabalho é comparar diferentes modelos de aprendizado de máquina para previsão horária de curto prazo de PM2,5 para que esse negócio de horizonte, avaliando desempenho médio, comportamento Então, quer dizer, ele está fazendo comparativo de modelos, isso aqui é detalhe de como você fez o horizonte, isso não tem que entrar aqui a princípio. O objetivo do seu trabalho foi comparar diferentes modelos de aprendizado de máquina, sendo que regressão linear não é aprendizado de máquina. então tem que tirar esse aqui, diferentes modelos até, pra previsão horária de curto prazo de PM 2,5, isso que é o objetivo os específicos eu não gostei tá ruim que eu achei então o que você vai colocar aqui por exemplo, falar o mesmo conjunto de teste a mesma comparação dos dados isso é óbvio, pra ser comparação você coloca às vezes no seu texto como, ai eu tô fazendo isso de diferente, não Todo modelo que faz comparação Ele tem que usar o mesmo conjunto de teste Senão não é comparativo Então você não precisa detalhar isso Não tem problema lá Eu vou mostrar lá na frente Se deixar claro que fez isso Mas não se colocar isso Como é o objetivo fazer isso Porque isso é óbvio Se é comparativo Agora o que você vai colocar como objetivo Específico É só as etapas da metodologia Então, para você fazer essa previsão de curto prazo, o que você tem que fazer? Eu tenho que fazer a preparação da série temporal, aí, por exemplo, sua série temporal tem dados faltantes, tem que preencher, fazer a imputação de dados faltantes, tem que, a cada etapa de metodologia, um pipeline da metodologia, isso vai ser os objetivos específicos. Então isso aqui tem que arrumar Não existe cronograma e monografia Não sei por que você colocou isso TCC1 e monografia TCC2 não 

**Daniel** [00:06:09]
TCC Então, isso não é por Então, eu tinha colocado isso aí Porque eu achei que precisava para enviar Para o projeto 

**Luciana** [00:06:19]
Mas o seu é TCC2 Já 

**Daniel** [00:06:21]
Eu coloquei por segurança 

**Luciana** [00:06:25]
Não O projeto tudo bem mas a monografia não tem cronograma não o projeto lá que é o TCC1 tem que ter mas agora o seu já é TCC2 então não tem cronograma não e a organização do trabalho tirei motivação aqui porque não tem agora você tem um objetivo só você não tem os objetivos você tem um objetivo, fazer previsão de PM2,5 não vi mais de um objetivo no seu trabalho então um objetinho aí aqui tá legal isso aqui tira porque não tem cronograma aqui eu coloquei só isso apresenta o conceito necessário pra compreender o trabalho só isso agora, hora do dia é porque você colocou o seguinte quando várias o que é multivariado? Quando várias grandezas são registradas nos mesmos instantes. Quando PM2,5, PM10, está certo, isso é multivariável. E a hora do dia? Não, a hora do dia é o tempo, é o T. Isso não é variável. 

**Daniel** [00:07:43]
Espera aí. 

**Luciana** [00:07:45]
Entendeu? A hora do dia é um instante, isso não é uma variável. O que você vai chamar de multivariável, univariável, são variáveis. 

**Daniel** [00:07:54]
Sim. 

**Luciana** [00:07:54]
Que são as colunas. colunas, o t não é coluna, a hora do dia não é coluna, para você fazer previsão. 

**Daniel** [00:08:01]
Espera aí, deixa eu só ler um rapidinho. No caso, a hora do dia... espera aí... Eu fiquei em dúvida, o que acontece? Lá no trabalho, normalmente a gente coloca, por exemplo, quando eu coloquei lá, eu coloquei o horário do dia como função 

**Luciana** [00:08:33]
de seno e cosseno. Mas isso aí, seno e cosseno em relação ao PM 2,5 que você fez, não é a hora do dia. 

**Daniel** [00:08:44]
Não, então, é para mostrar a simplicidade do dia, no caso. Não, mas não tem nada a ver com a hora do dia. 

**Luciana** [00:08:53]
A hora do dia é o próprio tempo, porque se a sua previsão é horária, se você coloca aqui, vai ficar confuso. Previsão é o horário e a hora do dia é o tempo E até escrevi aqui O que é multivariável? O que é a diferença do multivariável com a exógeno? Eu posso ter duas variáveis A e B Agora quando as duas são A caneta do negócio ficou horrível Porque eu quis escrever previstas Quando as duas são previstas ao mesmo tempo Aí é multivariável Agora se eu uso PM2,5, PM10, mas eu só vou prever PM2,5 pra repariar a vez hoje. Não tô fazendo multivariar. E outra coisa, quando eu tô fazendo a previsão das duas ao mesmo tempo, a afeta B e a B tem que afetar A. Tem que ser a via de mão dupla. Então, se eu tô prevendo as duas ao mesmo tempo e uma afeta a outra, as duas, uma afeta ou outra, aí eu chamo de modelo multivariável. Sim. Agora o seu, pelo que eu lembro, é variável exógena. Você tá usando só a previsão de PM2,5 e tá usando o PM10 pra ajudar a explicar. 

**Daniel** [00:10:12]
Sim, sim. 

**Luciana** [00:10:14]
Agora, se você tá fazendo isso, então não tem que falar de multivariado aqui, ó. Até completei aqui pra ter certeza, mas você só vai falar do que você tá falando, porque senão você fala de modelo multivariado, chega lá na frente e derruba o variado. Então, você não tem que falar de multivariado aqui. E aqui, ó, o conjunto de degrandezão não está... Então, assim, eu até completei aqui, queria uma coisa, mas o seu não é multivariado. É isso que eu queria chegar ao ponto. O seu é de variável exógena. Então, o que você vai explicar aqui é variável exógena. aqui eu pedi pra fazer que tem mais, quando a gente coloca a equação, não tem problema até depois o parente corrigir porque você tá citando a equação só que geralmente quando a gente coloca uma equação a gente tira o parágrafo e coloca onde o T o que cada um representa mas eu acho que fazer assim também não tá ruim qualquer coisa eu deixo assim deixa a banca corrigir agora as sessões também a gente quebra a sessão quando muda o assunto se você que está falando de séries temporais, janelas e variáveis exógenas faz parte de séries temporais então é 2.1.1 continua o mesmo assunto então aqui se está falando da da janela né total aqui ó alguns atributos além disso são conhecidos de antemão para os instantes futuros como não entendi nada disso não sei o que tentou explicar aqui mas hora do dia não é atributo tô voltando a falar então isso aqui não ficou legal isso aqui tem que arrumar né que subiu aqui em cima isso aqui ficou legal tem que explicar o que é o variável exógena porque cê tá já usando variável exógena mas cê não explicou então antes cê usar um termo cê tem que explicar porque aqui o PM dois e meio ali tá usando como variável exógena isso aqui ó né o Z de T aqui vai entrar como variável exógena ela não faz parte da entrada ela é um variável exógena mas cê tem que explicar antes aí cê vai explicar lá atrás aqui ó em algum lugar aqui então tudo que cê vai usar cê tem que explicar antes então tentei rabiscar aqui alguns textos vou pedir pra ó aqui nesse que cê tá explicando pedir pra deixar um exemplo numérico pra ficar mais claro tirar isso aqui porque achei que não vale a pena não tá legal esse texto não precisou eh cê já mostrou isso equação dois ponto três sobre previsão multiorizonte então o que eu falei ó não achei relevante isso aqui de mostrar esses três tipos porque cê já mostrou na equação dois ponto três que que ele tá aqui cê já mostra o que que é o feito né de horizonte pra frente o YT aqui já mostrou aqui só explicar clicar isso aqui então e não faz sentido você mostrar esses três tipos se você não vai a não ser que você tá comparando as três formas é o caso de você tá comparando as três formas de 

**Daniel** [00:13:53]
trabalhar então tem uma uma das lestem são recursiva a outra direta e o codificador de O codificador é o seq2seq Então são três modelos Fazendo previsão multi-horizonte De forma diferente 

**Luciana** [00:14:10]
Ah, mas não ficou Bem explicado isso aqui, não Porque, ó, recursivo O modelo aprende a prever apenas um instante à frente Beleza E a previsão obtida é reinserida Na entrada para obter E assim por diante Isso aqui é janelamento Isso que você chamou de recursivo Eu conheço como janelamento A janela deslizante é isso Então isso aqui é janela deslizante Agora direto O modelo produz cada horizonte Sem depender das previsões anteriores Na verdade é colocar O que você chamou de direta É ampliar a janela do horizonte Na verdade O que está fazendo é o seguinte Se eu colocar aqui o H igual a 1 Eu estou prevendo um passo à frente Se eu aumentar Estou fazendo tantos passos à frente Isso tudo é janela deslizante Não entendi muito Essa explicação com esse nome Não sei se os autores usam isso Mas eu achei que ficou confuso Esse texto Não sei o que você comparar Se você quer detalhar e foi feito isso, ou talvez lá na frente, mas você não precisa dar uma sessão pra isso aqui na fundamentação teórica. Lá na frente você mostra que uma vez que o horizonte aqui, H, mudou, ou você pode chamar só atenção, né? Se o H é igual a 1, aí a janela, aí você pode escrever assim, que é uma forma, mas não que é uma sessão. Você fala assim, de acordo com H, previsão multiorizonte vários instantes agora que você está explicando é que seu texto para mim ficou confuso agora que você explica talvez faça sentido o modelo estima vários instantes futuros a partir do mesmo instante emissão e não apenas o próximo na verdade esse não apenas o próximo que estragou na previsão multiorizonte o modelo estima instantes futuros a partir do instante emissão T que a gente determina por T mais H aí você pode determinar chamamos de recursiva quando H é igual a 1 então aí você mostra isso chamamos de direta quando o H é maior que 1 e aí tem esse cara aqui e o outro então baseia naquele H e referencia essa equação do 2.3 aqui Então pode manter Talvez a sessão Se você está usando as três formas Tem que escrever um pouco melhor Então eu rabisquei aqui tudo Mas você arruma Validação temporal Continua falando de série temporal Então continua a sessão aqui Esse texto eu gostei Aqui só faltou falar o que é L Porque você fala do CV Então L é É o erro, é o nós mas como o erro a gente chama de erro talvez chamar sua atenção pra isso aqui dados faltantes imputação e precisamento temporal, então cada um é uma seção aqui se o seu modelo não faz isso, retire esse texto não vai criar perguntas do porquê, porque uma forma de manter essa distinção é acrescentar ao modelo um indicador de ausência uma variável 

**Daniel** [00:17:53]
no caso o meu faz isso mesmo ele marca se o dado Ele é imputado ou não 

**Luciana** [00:17:59]
Mas qual é o modelo que faz isso? 

**Daniel** [00:18:02]
Todos eles Não, na entrada, como variável Naquele instante O valor é imputado de PM2.5 

**Luciana** [00:18:12]
Como é que você faz isso? Me explica Você tem o dado de PM2.5 E aí ele é um vetor de 0.1 Se ele está imputado Ou se ele é direto 

**Daniel** [00:18:27]
Então, ele vai passar pela imputação linear, certo? Os valores que são imputados nessa imputação linear, eu marco como verdadeiro ou falso nessa etapa de preparação. 

**Luciana** [00:18:44]
Pois é, mas entendi, você marcou como verdadeiro ou falso, zero e um, mas como que entra na rede neural? 

**Daniel** [00:18:52]
Entra com uma coluna, não dá. Igual aos outros dados. 

**Luciana** [00:18:55]
Pra que isso? 

**Daniel** [00:19:00]
Ah, pra para o modelo não a ideia minha era para o modelo saber se aquele dado é de valor de confiança ou não porque eu vi alguns trabalhos que eu cheguei a referenciar aí eles não calculam o erro baseado se aquele dado for imputado nas métricas de erro 

**Luciana** [00:19:18]
mas é porque não faz sentido olha só você tem uma série temporal 

**Daniel** [00:19:24]
entendeu 

**Luciana** [00:19:26]
eu teria que ter 10 valores eu tenho 7, então 3 ali do meio Estão perdidos Aí eu usei a imputação dos dados Aí eu vou colocar Essa série temporal na rede neural Vou colocar os Considerando que isso é dado de treinamento Vou colocar os 10 dados Se eu coloco pelas colunas O outro está servindo como variável exógena 

**Daniel** [00:19:52]
O outro você fala qual? 

**Luciana** [00:19:55]
O 0 e 1, verdadeiro e falso 

**Daniel** [00:19:57]
Sim, sim 

**Luciana** [00:19:58]
Mas essa variável exógena Ela vai Explicar O O valor do modelo E não explica 

**Daniel** [00:20:10]
Então, mas aquele valor imputado Não representa 100% O valor que era real, sabe? Sim, mas isso 

**Luciana** [00:20:18]
Faz parte da imputação dos dados Ela é É aceitável Por isso que a gente escolhe o melhor modelo de implantação de dados 

**Daniel** [00:20:28]
então, eu vi trabalhos recentes, eu vi dois trabalhos recentes que o pessoal não estava medindo o erro baseado nisso, aí ele tem até explicação lá, o motivo aí eu achei que fazia sentido, porque o valor imputado apesar de ele estar lá pra ajudar o modelo, ele não representa sem fielmente o valor real, né 

**Luciana** [00:20:51]
sim, mas isso faz parte da literatura a gente sabe disso Só que até tem estudo Quem que fez esse estudo? Teve uma pessoa Que fez estudo sem imputar dados E imputando dados E o imputando ficou melhor Foi você, não foi? 

**Daniel** [00:21:11]
Não, mas não dá pra Passar o LSTM Sem imputar dados Porque aí você vai cortar A questão temporal da série temporal 

**Luciana** [00:21:21]
Alguém fez isso 

**Daniel** [00:21:24]
Eu tinha feito 

**Luciana** [00:21:25]
estudo comparar a gente fez isso mas tem gente que fez isso assim não importou dava em ter buraco tudo bem deixa a série com buraco no sentido assim o tom 

**Daniel** [00:21:41]
tem um tempo eu não lembro mas é uma esposa mas aí não faz mas aí se você cortar a 

**Luciana** [00:21:48]
sequência? O temporário perdeu a sequência, é. Mas olha só, não, não sei como é que foi feito, se fez média, se é imputar dado, fez a média, ou repetiu o último 

**Daniel** [00:22:01]
dado, foi isso? Mas e se imputar dado também, Luciana? 

**Luciana** [00:22:06]
É, mas quando se repete dado, aí como é que eu... Eu não lembro mais o trabalho, mas teve gente que fez um comparativo, se era melhor não imputar mas eu não lembro como é que ficou o buraco ou se não teve buraco agora eu não lembro mas resumindo 

**Daniel** [00:22:23]
mas antes de falar até pelo que eu pesquisei mesmo quando você faz uma regressão linear entre dois pontos entre duas faixas isso pode ser um tipo de vazamento de dado porque 

**Luciana** [00:22:36]
pode, se você é igual você falou lá na frente se eu usar um dado 

**Daniel** [00:22:41]
lá da frente para traçar uma reta aí você está mostrando uma entendência, isso também é um vazamento de dados 

**Luciana** [00:22:49]
sim, e isso tem que tomar cuidado isso eu concordo, mas o que eu estou chamando atenção é o seguinte, se você coloca uma coluna extra no modelo eu entendi que você está querendo dizer se esse dado é importante ou não 

**Daniel** [00:23:08]
para o modelo aprender ou não 

**Luciana** [00:23:11]
só que eu vejo isso, porque olha só, o que que é um modelo? É pegar as entradas e fazer uma projeção pra saída. Se você coloca zero em um, é como se você estivesse dando um peso pra aquela entrada. Eu concordo. Tipo assim, o dado que tiver com o verdadeiro, com um, ele é pra conseguir liderar um peso a mais. Só que eu não sei o quanto que isso afeta na sua resposta, Porque ele não faz parte da previsão. 

**Daniel** [00:23:47]
Não faz, mas... 

**Luciana** [00:23:49]
Mas o modelo não entende isso, entendeu? Ele entende como fazer no corte da previsão. Você não coloca o PM10 como sendo uma variável exógena, porque ela ajuda a explicar o PM2,5? 

**Daniel** [00:24:02]
Sim, sim. 

**Luciana** [00:24:04]
Porque ele tem correlação, então ele ajuda a explicar. Agora, o quanto que verdadeiro ou falso ajuda a explicar? Isso que eu não sei Tudo bem, já que você fez Você escreve sobre isso Mas eu preciso que você explique isso aqui um pouco melhor 

**Daniel** [00:24:19]
Não com 

**Luciana** [00:24:20]
Essas três páginas Essas três frasetinhas Linhas Porque está muito confuso Isso, faz exemplo Numérico aqui E coloca a referência de onde você tirou essa ideia 

**Daniel** [00:24:35]
Eu cheguei a colocar aí Não sei se é essa aí logo embaixo Mas eu acho que eu tinha encontrado duas 

**Luciana** [00:24:41]
Mas detalhe Isso melhor O ponto foi feito em Pra Ter um respaldo disso aqui Eu não lembrava que você tinha me contado Que fez isso e agora eu fiquei preocupada Porque isso tá entrando Como variáveis hoje Tudo bem, não é que tá errado Entendeu, Daniel? Mas tem que explicar direito 

**Daniel** [00:25:04]
Tá confuso 

**Luciana** [00:25:05]
Porque eu estou entendendo eu entendi que você quis fazer tipo um peso então chama isso de peso você está pesando a variável que não foi imputada, mas eu não sei quanto isso interfere no resultado final depois a gente vê sobre isso, mas coloca a referência que você baseou na literatura e escreve melhor essa parte beleza aqui não tem isso de calendário, não sei o que está tá tentando explicar a variáveis futuras só podem ser usadas quando forem conhecidas antes da 

**Daniel** [00:25:43]
previsão como o calendário que que é isso isso estaria mais relacionado que a funcionalizando com sendo da data mesmo que entra como variável exógena para uma não entendi explique-se melhor 

**Luciana** [00:25:58]
O que é seno e cosseno? 

**Daniel** [00:26:00]
Por exemplo, você vê que você faz ou não coloca a data como variável, você colocaria só o seno e o cosseno. Aí, tipo assim, meia-noite estaria próxima de uma hora da manhã, sabe? 23 horas, próximo de 24 horas, próximo de uma hora, certo? 

**Luciana** [00:26:18]
Mas você não coloca a data como variável? 

**Daniel** [00:26:21]
Não, coloca só ela em função de seno. Entendeu? você não pode a data pura 

**Luciana** [00:26:28]
mas não é variável de entrada isso por que isso é variável de entrada? o que eu entendo de seno e cosseno é quando você faz uma transformação do dado é um tipo de tratamento de dado para você suavizar alguma coisa eles são filtros suavizadores que eu conheço de tratamento de dados beleza mas a data não tinha que entrar como variável de entrada do seu modelo por que que ela está entrando? 

**Daniel** [00:26:59]
ela está entrando para por exemplo justamente para horários próximos de 23 horas, 24 horas e meia noite, eles na verdade por exemplo, eles não são datas distantes, na verdade são datas que estão uma próxima da outra certo? esse é um motivo e isso 

**Luciana** [00:27:19]
vai ter que explicar isso melhor, colocar referência da literatura que não está aqui e explicar esse calendário, mostrar o modelo numérico mesmo, porque não está com a sua 

**Daniel** [00:27:30]
inteligência. Ao mesmo tempo, Luciana, por exemplo, os horários de PM2.5 tem picos bem específicos, por exemplo, das 18 horas, sabe? E de manhã. 

**Luciana** [00:27:39]
Mas isso faz parte da série. 

**Daniel** [00:27:42]
Sim, então, mas a ideia era justamente pra pra essas tendências, esses momentos, ficar mais claro para o modelo. Aqui é um momento que tem tendência de ser mais pico, aqui tem tendência de ser um momento de ser mais baixo. Mas isso ele vai 

**Luciana** [00:27:57]
ver pelo comportamento ainda mais se for sazonal, ele vai enxergar essa sazonalidade pela série, não por você colocar um peso nele. 

**Daniel** [00:28:07]
Então, a ideia do cena e cossena era justamente para essa sazonalidade independente do horário, ficar mais claro. 

**Luciana** [00:28:15]
Coloca a referência de onde você tirou isso da literatura e explica-se melhor. desenhos muito pior aqui. Não está claro isso, não. Só isso aqui de variáveis futuras aqui ficou ruim, não deu pra entender, não. 

**Daniel** [00:28:28]
Tá, posso colocar. 

**Luciana** [00:28:29]
Quando você coloca a rede neural, aí sim, mudou de sessão. Aí, beleza. Tá aqui, tá legal. Tá recorrente, long shot mesmo. Cara, não gostei dessa elaboração própria. Por que você não pega aquela figura da LSTM mesmo, que aí depois eu fui ver, Ela está aqui atrás, leva ela para frente e explica isso aqui. Porque isso aqui não são três redes, isso aqui são três camadas, pelo que eu entendo. Então, até perguntei aqui, aí não está legal esse texto não, unir esse texto com a figura e essas equações. O que eu quero dizer com isso? cara, a LSTM é apresentada na figura 2.5 começa o texto assim como a gente pode ver na parte A, a parte inicial a gente tem o portão de não sei o que o que ele está fazendo ele pega esse dado aí mostra as equações disso vai o texto direcionando o leitor para a figura e para as fórmulas porque aqui você fala do texto todo depois você fala o cara tem que imaginar aí depois ele vai pra figura depois que ele vai à fórmula, tenta unir isso pra ficar bem legal tem muito texto, tem TCC tem um livro mesmo que explica a STM que tá bem claro isso, tá bem direcionado pega isso da literatura não tenta fazer elaboração própria não ficou esquisito aqui não é que ficou esquisito eu acho que você tentou explicar muito E tem coisa aqui que eu acho que ficou errado. Como, por exemplo, chamar isso aqui de três fases da rede, alguma coisa assim. Eu acho que não ficou claro. Então, por isso que eu estou falando, usa da literatura. Aí você vai explicar o seq2seq e atenção. Aí eu pedi figura para entender melhor isso. isso, apresenta como cada estado HJ é calculado no identificador. Aí, o identificador é outra rede recorrente que gera saída um elemento por vez. O que significa isso? Aí eu estou entendendo que você quer falar aquele sequencial que está lá em cima. Não ficou claro, não. Você tem que direcionar. Então, vai ser um horizonte, um elemento previsto cada vez. na previsão a janela de entrada é a sequência de entrada e o horizonte previsto é a sequência de saída, não entendi nada disso o que é isso? sequência de entrada e sequência de saída, o que você quer dizer com isso? 

**Daniel** [00:31:24]
na entrada ele forma pesos internos no decodificador no decodificador ele pega esse peso e traduz para o valor do PM2.5 em si, assim de fato o que seria seria a sequência de saída de fato 

**Luciana** [00:31:39]
Só essa frase aqui não fica claro não, desenhe isso aqui, coloque um detalhe, coloque um exemplo numérico, acho que fica legal. Ó, figura, direcionando o texto para a figura, ó, esse vetor único é um gargalo, por quê? Por que que é gargalo? 

**Daniel** [00:32:02]
Era por causa justamente da tensão, para representar os dados, mas não lembro direito o motivo. 

**Luciana** [00:32:19]
Está claro essa tensão não, achei muito confuso, Daniel, a sua parte tem que olhar. Não entendi nada disso, os pés indivíduos com quais instantes da entrada são mais importantes para aquele passo? 

**Daniel** [00:32:30]
esses pesos é sobre a camada de atenção mesmo 

**Luciana** [00:32:34]
pois é, mas não está bem legal não você falou que mostrou um esquema adaptado eu pedi, mostra o original ao invés de adaptado para ver se fica mais claro porque isso aqui eu acho que não esclareceu muita coisa não na fundamentação teórica acho importante você pegar a definição da literatura e colocar de forma didática no seu texto eu acho que ainda está confuso entender esse modelo não ficou claro para mim não não sei onde se encaixa, se é subseção do anterior, esse negócio de codificador regressivo que cê chama. Aham. Esse texto está ótimo. Então, esse texto é o que eu gostei, porque que ó, cê conseguiu explicar direcionando com a figura, esse aqui ficou legal. Uhum. Só pode ser usado, só que é o seguinte, o que cê chamou aqui, eu chamei atenção, ele só pode ser usado no treinamento né, porque você não tem na prática o valor real pra poder ficar imputando você vai sempre usar o free running então você tem que deixar isso claro no texto aqui porque você chama tem essas duas formas mas tem que deixar claro isso são formas de fazer no treinamento porque não é eu quero entender isso Por que e quando usar o teacher forcing em relação ao free running? Por que é importante usar ele? O senhor até se explicou, mas não falou por quê. Aí você falou, existem ainda decodificadores que dispensam a realimentação, isto é, não recebem a previsão anterior como entrada. Mas aí não é esse modelo. O que você está falando de receber previsão como entrada? Eu não entendi por que isso está aqui. Tá. 

**Daniel** [00:34:32]
Melhor pagar. 

**Luciana** [00:34:34]
Eu explico um pouco melhor essa parte. A parte do XGBoost, eu vou te mandar um texto, porque eu acho que o seu texto se entendeu errado. Porque não é isso aqui, não. Pelo que eu conheço do XGBoost, eu ainda pedi pro chat fazer um negócio pra ver se o que eu sabia que estava certo. E é exatamente porque aqui está dando pra entender que você está somando resposta desses caras. Uh-huh. E não é isso na prática, cê não tem várias árvores, cê tem uma árvore por interação, o que ele faz é somar os resultados aqui, aí ele faz a média, aí quando ele vem pra cá, ele melhora os erros que ele faz aqui, eu vou te mandar um um texto, eu pedi dois já pra fazer um texto com três exemplos e aí eu vou pedir, ó, usa o texto que eu coloquei. Tá. Eu vou te mandar treinamento, perder preparandos. Ó, o que que você chama uma fração das unidades da rede? O que que é isso? 

**Daniel** [00:35:41]
Dropout, se liga. Uma fração da unidade seria os próprios neurônios. Uma parte dos neurônios.

**Luciana** [00:35:46]
É, mas então usa neurônio. 

**Luciana** [00:35:47]
Porque o leitor não pode ficar confuso. Você tem que padronizar. Não pode uma hora chamar de unidade da rede e outra hora de neurônio. Chama ele humano e certo. Tá bom. Porque senão fica muito confuso. Poucas unidades. O que é unidade? O que é pouca unidade? Neurônios. A camada com poucos 

**Daniel** [00:36:05]
neurônios fica melhor. Sim. 

**Luciana** [00:36:08]
Seu texto não tem contexto. O que eu achei, esse aqui, tá vendo? Você tá falando de várias coisas picadinho, não tem um contexto, não tem uma descrição do porquê tá falando as coisas. Pegou várias informações ali, definições e jogou. O que que eu tô falando aqui do weight decay, do dropout, separado sem um contexto. Tem que construir melhor essa parte. Mas isso aqui pode fazer depois. O que é mais crítico é a parte de cima, isso aqui depois a gente vê se coloca, se tira. O que que é orçamento de treinamento? O que que é isso? Orçamento limitado. O que que é orçamento? 

**Daniel** [00:36:54]
Ah, é do próprio é do Optuna quanto que ele vai continuar treinando o modelo até ele podar ele, no caso o orçamento é o tempo computacional mesmo.

**Luciana** [00:37:08]
Tem muitas coisas nessa parte do seu texto que ficaram soltas. 

**Luciana** [00:37:12]
não tá coisa nisso que eu achei estranho tá, aí 2.5 vai falar de métrica tira isso aqui porque quando você está fazendo fundamentação teórica, você não tem que falar do seu trabalho, você vai falar do que está na literatura. Isso é que eu achei estranho, porque, olha só, tudo bem você falar igual o MAE, ele mantém a mesma unidade de grandeza, ótimo, ele é usado por isso, mas quando você fala que eleva a raiz quadrada, quem eleva é o MSE, o RMSE tira a raiz quadrada, então ele vai manter na mesma unidade, então, não entendi se chamar a atenção de elevar ao quadrado, porque ele tira a raiz depois. Então, tem que ver. Aí você falou, o MAE e o RMSE respondem a perguntas diferentes. Quais? Porque é legal dizer quando usa um, quando usa outro, mas explica isso melhor. E quem eleva ao quadrado é o MSE, o RMSE tira. Tanto é que por isso que ele é usado de comparativo. Então, só chamar a atenção. Isso aqui eu gostei Agora, isso aqui eu não entendi nada Você usa isso aqui? Vies, médio E média Você usa Esses negócios aqui? Como é? 

**Daniel** [00:38:36]
Usei O viés médio Acho que se não me engano Justamente para ver se o modelo está repetindo o modelo passado ou não Ele está muito tendencioso Para o passado recente 

**Luciana** [00:38:48]
Entendi Então, detalha para mim melhor isso aqui, como você fez com fórmula e tal, porque eu acho que está... E coloca a referência de onde você tirou isso, porque não está legal muito, não. O fio MAE pode ser calculado separadamente para cada horizonte. Por que você usa isso? Qual o motivo de usar isso? 

**Daniel** [00:39:11]
Para ver se a tendência no horizonte mais recente ou mais longo, se o erro vai crescendo de forma muito grande ou se ele mantém. 

**Luciana** [00:39:20]
Explica isso melhor então, que é usado nisso e referência de onde você tirou isso, tá? Tá faltando. Tá, comparação estatística de previsões, mas só falar se você usa isso. Isso pode ser usado em séries temporais? Como é feito? Quero figura, porque você tá falando do bootstrap em blocos. que aí você repete o bloco de teste mas se você repetir você está perdendo a sequência temporal isso é usado em série temporal? não entendi isso não essa parte de fazer esse bootstrap de bloco isso aqui essas métricas aqui se você usou isso você colocou um monte de referência beleza, mas isso é usado na série temporal, detalha isso com um pouco de exemplo do porquê que usa isso, não só definir, mas porquê que é usado isso. A parte do trabalho relacionado, você falou o seguinte, uma revisão de 2024 sobre arquitetura de aprendizado para previsão de PM2,5 amenou a semelhança e a diferença entre esses modelos e concluiu que falta um referencial unificado e padronizado para avaliar o desempenho deles o que é isso? que referencial unificado? 

**Daniel** [00:40:57]
ah, mas eu não lembro dizer não 

**Luciana** [00:40:59]
o que é isso aqui? está confuso, não entendi nem o que é esse referencial unificado eu tiraria isso aqui só falaria que fez o concluir não que concluiu mas tipo assim, vê o que ele concluiu mas não gostei disso aqui não, achei estranho, mas beleza. LSTM otimizado, o que que significa LSTM otimizado? 

**Daniel** [00:41:33]
Seria justamente depois do treinamento, né? 

**Luciana** [00:41:36]
Não, mas isso todo modelo é treinado, então a previsão horária usando uma LSTM, Não tem nada de LSTM otimizado LSTM Aí decomposição Por modos empíricos Isso é um modelo? 

**Daniel** [00:41:53]
Decomposição Por modos empíricos Não 

**Luciana** [00:42:00]
Combinaram a decomposição por modos empíricos Com LSTM Então não entendi Tudo bem que você colocou a referência Mas só Só não entendi se isso é um modelo Ou se eles fizeram Às vezes, decomposição por modos empíricos, como o da Céu. Eu não sei, explica isso aqui um pouquinho melhor, que eu fiquei com dúvida. Tá. O que é PM2,5 urbano? 

**Daniel** [00:42:29]
Isso aí só está referindo, não tem nada demais, é só questão da cidade mesmo, não tem? Ou que coloquei só um vídeo da cidade. 

**Luciana** [00:42:38]
Porque senão fica chamando a atenção que é alguma coisa. Então, PM2,5. também há modelos que incorporam informação espacial entre várias estações que modelos? está falando de uma referência de modelos que modelos? tenta listar alguns aqui agora isso, a informação espacial vai entrar como atributo, explica melhor isso aqui ou dar sistemas de navegação como atributo, explica um pouco melhor altura da camada limite planetário, esse também é atributo ele diz que foi a variável mais importante para as florestas aleatórias o que indica o peso da meteorologia na previsão, mas você não tem esse atributo que eu lembro então não é toda estação que vai ter esse atributo 

**Daniel** [00:43:30]
então 

**Luciana** [00:43:31]
além de falar disso fala de onde, que foi em Curitiba mas chama atenção que nem todas as situações tem essas variáveis, porque senão fica parecendo, por que você não usou? Você não tem, então chama atenção aqui. Não precisa separar aqui, porque eu acho que continuou falando de modelos, de coisas, não tem que separar isso tudo, comparo vários modelos, aqui está comparando também, isso não interessa, se está comparando um ou vários, não interessa. Então esse texto aqui continuaria corrido e isso aqui eu tiraria que eu não vi relevância nenhuma dessa parte dessa tabela de fazer isso aqui não entendi muito o que você quis mostrar aqui, mas o importante é fazer a sessão assim trabalhos relacionados sob previsão de PM2,5 o que eu gostaria, mais ou menos você fez, é colocar em ordem cronológica por exemplo, 2023 podia vir depois de 2021 2021 para 5 que aí a gente vê a sequência desde quando tem trabalho aí beleza, modelo de sequência, atenção e séries temporais séries temporais como geral, ficou legal agora, o que é referência simples? referência simples eu tiraria isso, referência simples e avaliação pelo que eu li aqui, não acho confiável isso aqui Porque eles mostraram 1.045 séries mensais Da competição M3 E mostraram que métodos estatísticos Tradicionais tiveram erro menor Que os métodos de aprendizagem de máquina Cara, depende da série Isso não pode comparar assim Porque, por exemplo Eu não sei se essas séries aqui são lineares Se ela for linear é lógico que O modelo estatístico é melhor Não achei relevante isso aqui não Então, aí o que eu queria é realmente trabalho sobre como você faz imputação de dados, então trabalhos relacionados sobre dados faltantes para falar dos métodos mais usados. Isso, legal, isso eu acho interessante. E o seu, você falou de um só, aí eu gostaria que tivesse mais de um. Aqui, você fala Este trabalho se ocupa desse conjunto Ele compara as redes Com o mesmo tratamento dos dados E os mesmos treinamentos para todos Isso não é um diferencial Todo trabalho que faz comparação tem que fazer isso Então, não achei interessante ter essa seção aqui Então, o que eu queria no capítulo 3 é isso Trabalhos relacionados sobre previsão de PM2,5 E trabalhos relacionados sobre Imputação de dados Que são as duas coisas que você fez Até se você achar trabalhos relacionados Sobre alguma coisa muito específica Você pode colocar no geral Mas eu acho que esses dois Estão bons para trabalhos relacionados Agora vai na parte que eu comecei a ficar preocupada Porque eu não entendi um monte de coisa Aqui, eu falei Tudo bem deixar isso claro aqui, mas isso não é o diferencial do seu trabalho, né? Que você sempre usou os mesmos dados. Mas é que é legal você falar só para explicar. Daniel, deixa eu me dar dois segundos disso. Vou precisar ir no banheiro daqui a pouco. 

**Daniel** [00:47:15]
Tudo bem, pode ir lá. Tomei uma xícara de chá, fez efeito. 

**Luciana** [00:49:18]
Vamos lá. Por que foi escolhida a estação? Então, quando você falou da estação Aqui você Você explicou Lá embaixo você escolhe a da estação O que eu quero No seu trabalho Pra eu me voltar a ler esse capítulo 4 Você tem coisa Você nunca pode referenciar Coisa pra frente Você referencia coisa pra trás Se você tá jogando Uma coisa lá na frente Tipo assim, aqui Ah, vê lá na frente Não é que não pode A não ser que seja uma coisa muito pontual Tipo assim, vou ter uma sessão Explicando isso, preciso Separar, mas vou falar disso primeiro Agora o que eu li do seu texto As coisas que você está falando na frente Você pode trazer para antes Então, por exemplo Quando você fala aqui que foi escolhida A estação Sapo, beleza Você pode falar da escolha Antes desse texto aqui Vou pedir pra você explicar, mas antes de chegar lá ó, não entendi a única outra coluna em cobertura relevante é a de partículas totais em suspensão que não foi incluída, pois seu uso seria uma nova hipótese e não parte da comparação o que que é isso? 

**Daniel** [00:50:40]
eu acho que isso aí foi eu eu tenho quase certeza que não existe essa coluna na verdade 

**Luciana** [00:50:47]
então tira esse texto aqui, pelo amor de Deus 

**Daniel** [00:50:49]
porque eu acho que não existe de colunas totais 

**Luciana** [00:50:53]
pois é não entendi nada também os primeiros registros até 31 de dezembro foram usados em etapas exploratórias anteriores a este estudo que orientaram algumas histórias de projeto e os anos de 2021 a 2023 não foram usados em nenhuma etapa de desenvolvimento e formam um período de confirmação rolling origin, escrito na sessão 4.3.2.1. Não, não pode jogar lá na sessão. Você está vai escrever uma coisa e traz para cá. Não fala isso aqui. Agora, o que você está chamando de etapas exploratórias anteriores? 

**Daniel** [00:51:33]
Foi simplesmente tentar ativar, ver como o modelo se comporta. 

**Luciana** [00:51:38]
Então, você vai falar assim, através de estudos preliminares, não é etapa exploratória anterior, estudos preliminares estudos preliminares então fez uma escolha, mas não significa que o que você quer explicar nesse texto aí, me explica com suas palavras 

**Daniel** [00:51:59]
então, quando eu estava fazendo teste lá, eu comecei fazendo teste qual que seria o melhor momento por exemplo, qual que são as faixas de dados que tem mais dados e menos dados imputados aí eu selecionei parte deles uma faixa deles e comparei qual tinha o resultado melhor no modelo 

**Luciana** [00:52:25]
mas comparou com fazendo previsão? 

**Daniel** [00:52:28]
fazendo previsão, treinei o modelo e previ 

**Luciana** [00:52:30]
então explica ali em suas preliminares eu quebrei eu tenho 61 700 registros então eu quebrei e peguei uma rede simples você pegou uma LSTM sim 

**Daniel** [00:52:47]
é 

**Luciana** [00:52:49]
foi isso? foi a LSTM o primeiro modelo? 

**Daniel** [00:52:52]
eu testei principalmente o modelo seq2seq, principalmente pra ser honesto, eu testei nele e peguei assim, quais faixas tem dados mais contínuos, né? menos dados faltantes e nessas faixas eu peguei o que serve melhor, no caso aí eu selecionei aquele início e aquele final, aquelas datas 

**Luciana** [00:53:14]
Beleza, não, concordo com isso Só que tem que explicar melhor isso aqui Tá muito confuso Então, eu peguei o modelo seq2seq E Com os parâmetros Os hiperparâmetros padrões No caso, né Você não chegou a otimizar ele não, né 

**Daniel** [00:53:33]
Cheguei a otimizar um pouco sim Porque o seq2seq é treino rápido até 

**Luciana** [00:53:39]
Tá Então vamos pro passo Então, você vai falar assim, em estudos preliminares, então não precisa falar com o modelo, deixa isso para lá. Em estudos preliminares, eu peguei esses dados, você tem de 4 de janeiro a 31 de dezembro. Então, eu peguei de 31 de dezembro, você tem de 4 de, cadê o negócio, 4 de janeiro a 31 de dezembro. aí eu peguei aí você vai completar aqui peguei de 4 de janeiro até faz completo 4 de janeiro até ter um dezembro nem precisa colocar o o dato, você fala assim eu peguei de 2017 a 2020 coloca os anos completos de 2017 a 2020 como treinamento em estudos preliminares eu peguei de 2017 a 2020 pra treinar e de 2021 a 23 pra testar. Não é isso que você fez? 

**Daniel** [00:54:52]
2021 a 23 eu não usei pra testar, não. Meio que eu descartei. 

**Luciana** [00:54:59]
Então esquece de testar. Então fala isso. Eu peguei de 2017 a 2020 pra treinar modelos em estudos preliminares para escolher o que mesmo? O que você quer escolher? 

**Daniel** [00:55:14]
A faixa de dados. 

**Luciana** [00:55:18]
Quais estações tinham a melhor faixa de dados? Não é isso? 

**Daniel** [00:55:22]
Não. 

**Luciana** [00:55:24]
Me explica por que você descartou, por que você não usou a série toda? 

**Daniel** [00:55:31]
Porque o resultado piorava na prática. Quanto mais dados, não melhorava o resultado. Na verdade, piorava. 

**Luciana** [00:55:38]
Vamos para o Partes. usado nos resultados contém então os registros de 4 de janeiro a 31 de dezembro os 3 primeiros dias foram descartados porque as variáveis defasadas em 24 horas exigiam o histórico anterior beleza aqui você explicou então eu não consegui entender isso aqui os primeiros 34 mil registros de até 2020 foram usados em etapas exploratórias anteriores a este estudo, que orientarem algumas escolhas de projeto. Que escolhas de projeto? 

**Daniel** [00:56:54]
Por exemplo... Até aqui 

**Luciana** [00:57:00]
o texto está legal. Até as 48 horas aqui, beleza. Esse texto aqui, dos primeiros para cá, é que eu não entendi a relevância dele. 

**Daniel** [00:57:11]
Então, justamente sobre escolher qual seria a série a estação que eu usar e qual faixa de tempo de usar 

**Luciana** [00:57:20]
não, a estação você escolheu baseado nisso aqui que a gente vai chegar lá você está comparando estações você não usou, todas elas tinham a mesma faixa de valores de 2017 a 2023 todas? 

**Daniel** [00:57:36]
todas tinham, mas as lacunas variavam uma tinha bastante dados outras tinha menos 

**Luciana** [00:57:42]
isso eu entendi beleza, todas tinham a mesma faixa de dados aí, beleza se você falou assim, ah, eu usei pra escolher que tinha menos lacunes de dados pra escolher a estação, beleza, mas aí não faz sentido descartar de 2021 a 23 se você queria escolher 

**Daniel** [00:58:03]
eu, por exemplo quando você vai lá embaixo é a cobertura mensal lá mais embaixo ali, um pouco mais embaixo, a 2020 tem 3 meses faltantes Dois ou três meses 

**Luciana** [00:58:17]
Nessa estação Não tem em todas 

**Daniel** [00:58:22]
É, nessa estação 

**Luciana** [00:58:24]
Mas então não faz sentido Ainda não entendi o que você quis fazer Até isso aqui depois de chegar lá Pra reclamar disso Porque olha só Você queria determinar o que? Qual o horizonte pra trás e qual o horizonte pra frente Era isso? Nos estudos preliminares Porque aqui você usa 48 para trás E 24 para frente Era isso que você queria determinar? 

**Daniel** [00:58:58]
Não, na verdade Essa pessoa também me pegou quando eu fui escolher Porque tipo Eu tinha que escolher uma estação, certo Luciana? E eu escolhi uma faixa de tempo 

**Luciana** [00:59:08]
Faixa de tempo para quê? 

**Daniel** [00:59:10]
Você usaria todos os dados? Você usaria uma parte? Você usaria as datas mais recentes? 

**Luciana** [00:59:18]
Não Mas você sempre usa a série toda E depois você quebra lá no treino, validação e teste 

**Daniel** [00:59:25]
Então, eu posso fazer assim 

**Luciana** [00:59:29]
Não, você fez assim, não foi? O janelamento deslizante, treino, validação e teste Com toda a série Ou não, você jogou fora O que você quer dizer aqui é que você não usou de 2021 a 2023 De forma alguma 

**Daniel** [00:59:47]
Não, na verdade, lá embaixo, porque eu não lembro, no gráfico aqui eu coloquei como se eu tivesse usado realmente o ano de 2000 até 2021 como teste. 

**Luciana** [00:59:58]
Isso aqui, então vamos lá, antes de eu descer o texto, isso aqui você tem que melhorar isso aqui, porque estudos preliminares só servem para a gente, porque por que você está usando 48 horas para trás e 24 para frente? Isso foi definido com estudos preliminares Eu lembro que você experimentou várias coisas 

**Daniel** [01:00:17]
Sim, eu tinha feito teste 

**Luciana** [01:00:19]
Então isso aqui você tem que explicar Em estudos preliminares eu determinei Que o melhor horizonte foi 48 horas Horas pra trás Pra prever 24 pra frente um dia Até a primeira parte Que você tem que falar aqui dos dados Que eu não tô lendo aqui Pra começar os dados Ah, eu escolhi a série e tal Os dados são o que? São horários, são diários Aqui tem que estar falando isso 

**Daniel** [01:00:50]
Tá Eu estou Utilizando medições horários Então não é o suficiente pra falar que é horário 

**Luciana** [01:00:57]
Não, tem que mostrar Tem que deixar claro E aí, se possível, coloca aqui O... aquele do... Quando você faz Lá no Python aquela definição aquela tabelinha que você pede o info lá do pai, tu coloca aqui pra pessoa ver o que que tá não é só detalhar, coloca aqui aquela tabelinha então começar por aqui esse texto aqui isso aqui não ficou legal não deu pra entender, aqui você vai falar que você escolheu esse período pra previsão baseado em estudos preliminares beleza isso aqui que foi descartado e tal Não sei, eu acho que você não descartou Não tá legal Isso aqui tem que ir lá pra cima Porque você vai explicar Ou até não precisa ir lá pra cima Mas Aqui tudo bem Tipo assim Cadê o estudo Localizar Utilizar medições horárias Ah não, você fala que usa Isso que você mandou Não, isso aqui é suficiente Tá falando que usa medições horárias Mas aí eu quero ver a tabelinha dela aqui, localizada, que fazem parte do monitoramento. Aí aqui você pode falar. Isso aqui eu acho que... Eu queria ver se isso vem depois ou antes. É que eu acho que seu texto está pouco didático. Eu perguntei ali em cima por que não foi usado. Aqui que você vai dizer escolha. Deixa assim por enquanto, só tira esse texto aqui, porque aí a sessão sobe talvez a escolha da citação. Então, foi escolhida após uma análise exploratória de 38 citações, que considerou a cobertura do alvo. O que é alvo? 

**Daniel** [01:03:06]
O PM 2.5. 

**Luciana** [01:03:09]
Não ficou legal isso não. É, com medições PM 2.5, pronto. PM 2.5, tira esse negócio de cobertura de alvo aí. A continuidade temporal, a disponibilidade PM10 no mesmo horário, a frequência do evento, de alta concentração. O que é isso? 

**Daniel** [01:03:29]
São os picos mesmo do PM2.5. 

**Luciana** [01:03:32]
Não, mas você não vai ver isso. Não, tira isso aqui. Ó, você considerou medições PM2,5, a disponibilidade PM10 no mesmo horário, que é a variável exógena, explica aqui que é a variável e a continuidade temporal, esse negócio de eventos de autoconcentração não faz sentido porque tipo assim, você vai ver pelo objetivo da série, eu acho que não faz sentido chamar isso aqui, atenção pra isso agora, porque tá deixando o texto confuso então o objetivo dessa triagem foi selecionar uma série com volume suficiente primeiro, o que é volume suficiente? isso aí é ambíguo Não está querendo dizer nada. Então, se é na série que tiver menor quantidade de dados faltantes, detalhar isso aqui. Uma variável auxiliar, o que é variável auxiliar? 

**Daniel** [01:04:28]
Seria principalmente PM2, PM10. Não. 

**Luciana** [01:04:32]
Então, não é variável auxiliar, é variável exógena. Útil. E um número mínimo de eventos altos. Mas, isso aí não está legal, esse negócio de alta concentração. O pico faz parte do Eu não estou entendendo o que você acha que pico é bom, porque o pico dificulta a série. A não ser, para o seu caso, o fato de ter pico é para gerar melhor alerta, é isso? 

**Daniel** [01:05:00]
Na verdade, então, quando ele vai escolher, ou tem uma quantidade de pico suficiente para o modelo aprender, ou ele tem baixos picos e tem um equilíbrio maior. No caso eu procurei um equilíbrio maior entre os pedidos cronológicos Foi o que eu tentei colocar aí em cima Porque todas as vezes tem poucos picos Então na verdade eu estava procurando que tem menos picos Para atrapalhar a previsão 

**Luciana** [01:05:27]
Tá, mas não ficou legal com esse texto não Tipo assim, ou escrever assim Ou um número mínimo De Mínimo de eventos altos Para análise É porque não ficou legal esse texto Ficou confuso isso aqui não deu para entender. O que você quer dizer aqui, eu acho, então, uma série com grande volume de dados preenchidos, isso você pode escrever, nada de volume suficiente, porque suficiente é ambíguo, então, com grande volume de dados preenchidos, uma variável exógena, não é auxiliar, é exógena, útil, né, para ajudar na previsão, e... 

**Daniel** [01:06:20]
Eu tiraria essa parte mesmo 

**Luciana** [01:06:26]
Eu queria tentar Achar um texto para ajudar nisso aqui Porque tudo bem Você quer menos Eventos Não é eventos altos que chamam 

**Daniel** [01:06:44]
Seria muito 

**Luciana** [01:06:47]
Menor Dispersão Entre os dados Menor dispersão entre os dados Agora, e não a estação mais previsível Da rede? O que é isso? O que você quer chamar de estação mais previsível? 

**Daniel** [01:07:04]
Não, isso aí Eu achei que ficou o contrário da história Porque se eu quero Um equilíbrio maior A estação vai ser Mais previsível 

**Luciana** [01:07:14]
Exatamente, então tem que arrumar esse texto aqui Que ficou confuso Agora essa parte que eu não entendi Eu escrevi Não entendi nada Porque olha só 

**Daniel** [01:07:26]
A estação em primeiro lugar Teve uma pontuação 

**Luciana** [01:07:29]
O saco ficou em segundo lugar Tanto na classificação por PM2,5 Quanto na que incluiu PM10 Primeiro se ela ficou em segundo lugar Por que você escolheu ela? Já ficou meio confuso por isso Você tem que escolher o primeiro Não a segunda Aí depois, a estação em primeiro lugar Em 12 teve pontuação ligeiramente maior Mas apenas 0,19% de horas com PM2,5 acima de 35 miligramas em metros cúbicos contra 1,17. Cara, que confusão é essa? Eu não vi os dados, eu não sei o que é isso. 

**Daniel** [01:08:06]
Isso aí seria só os picos mesmo, considerando só a quantidade que passaria sem o de 35. 

**Luciana** [01:08:14]
Não está legal colocar esses valores aqui se eu não vi nada. Tipo assim, o que eu gostaria daqui? Classificação para linearização, PM2,5, mais contexto, PM10. Também não gostei desse contexto aqui. O que eu acho que você teria que mostrar aqui? Às vezes, colocar tipo assim, não mostrar esse negócio dos picos, mas o que você queria? Você queria a estação que tivesse a maior quantidade de dados preenchidos. Então, coloca a porcentagem de dados preenchidos aqui. Esse tem tanto, esse tem tanto, esse tem tanto. Aí, quando empatar, aí você detalha. Olha, as duas empataram em dados preenchidos. Mas a Rio Doce tem mais dispersão, né? O desvio padrão dos dados ali é de tanto e esse aqui é de tanto, é menor. Então, ela foi escolhida por ser uma série considerada mais simples de previsão. Pronto. Entendeu? Porque esse texto aqui está bem confuso de entender. Aí, olha só. Aqui já chama atenção. Se você vai separar, até gostei do gráfico, treino, validação, teste. beleza, só que você não falou ainda a separação de treino, validação e teste então antes de chegar nisso aqui de falar dos dados faltantes, de lacuna você vai ter que falar de como você quebrou os dados vai de 2017 a 2021 os dados considerados aí você pode falar agora entendi, então você jogou fora de 2021 a 2023 Por que? Isso eu não lembro. Por que você jogou fora esses dados? 

**Daniel** [01:10:27]
Eu me lembro aqui, pelo visto, eu não joguei fora, na verdade, eles fizeram parte do conjunto de teste e validação. Porque nos próprios outros gráficos... 

**Luciana** [01:10:36]
A gente tá falando que o teste vai até 2021. 

**Daniel** [01:10:40]
É, até 2021 mesmo. Então, Então, 22 e 23 eu joguei fora de fato. 

**Luciana** [01:10:47]
Por quê? 

**Daniel** [01:10:48]
Provavelmente porque... Acho que... Aí teria que olhar se tem uma lacuna em 22 e 23, mas não vou lembrar de cabeça. 

**Luciana** [01:10:56]
Mas tem que detalhar isso aqui melhor, tá? 

**Daniel** [01:10:59]
Aham. 

**Luciana** [01:11:00]
Então, você vai corrigir esse texto aqui pra mim, olhando lá o que você fez no programa, o porquê e tal. Então, primeiro, antes de falar aqui, você vai falar de visão dos dados. Você falou dos dados, por que escolher a estação de Sapo primeiro que não tem os dados aqui, cadê o desenho da série eu quero a série aqui desenho da série aí você vai falar da divisão dos dados, beleza só a divisão, escolhi em estudos preliminares eu resolvi escolher tantos por cento pra treino tantos por cento pra validação e teste se você fez dessa forma, você fez rolling origin você não fez validação pro Jato que lá no seu você falou de validação cruzada já começa a ficar estranho isso aí então você tem que ver realmente o que você fez se você fez validação cruzada você só vai falar que isso é o teste e que isso aqui tudo é o janelamento pra treinamento e validação 

**Daniel** [01:12:01]
então tem que arrumar 

**Luciana** [01:12:03]
aí não pode ser essa figura com essa cor, tem que arrumar aí aqui vamos lá, cobertura e lacuna Beleza, tem que falar que tem esses dados faltantes. Tá, o que é artefato final? 

**Daniel** [01:12:19]
Artefato final? 

**Luciana** [01:12:21]
Maiores lacunas originais de PM2,5 no artefato final. O que é isso? 

**Daniel** [01:12:27]
Acho que você só está falando do dataset final mesmo. 

**Luciana** [01:12:31]
O dataset não é artefato, por isso que você está falando para mim. Ah, não entendi nada disso aqui, se foi a maior beleza, eu acho que podia colocar porcentagem, eu não gostei desse, primeiro dia quebrado, você fala 8,5 meio dias, 48,25 dias, isso fica esquisito, porque dia não é quebrado, então, a não ser que você esteja considerando como é o horário, dá uma porrada disso aí, tá esquisito. isso ficou muito ruim de entender 

**Daniel** [01:13:10]
esse segundo gráfico é só para mostrar onde tem as lacunas quanto que essa lacuna dura, perdura e nas cores seria qual pertence a que parte que é o lacunas contínuos tipo assim o momento que ele fica alterado 

**Luciana** [01:13:26]
o problema é se você considerar validação cruzada isso aqui tem que ser uma cor só porque aí só vai separar o teste final apesar Ah, aqui isso também, porque o teste final é feito uma vez só, né? Mas só, beleza, agora entendi, mas tem que dar uma definição melhor aqui. A tabela resume cada bloco cronológico definido na seção 4.2.1. Então, ela tem que vir para frente. Se você vai falar dos blocos, fala dos blocos primeiro. Então, a validação concentra a maior proporção de ausência, beleza. não existe teste histórico, é teste de conjunto de teste a gente fala de série histórica, mas não tem conjunto de teste histórico não então o tema é novo a coluna entrada propagada informa a fração de horas dentro da lacuna de 24 horas ou mais em que a entrada do modelo vem da repetição do último valor medido e não dos dados novos, tem de nada 

**Daniel** [01:14:31]
a coluna entrada Também não gostei não Ficou muito humilde 

**Luciana** [01:14:42]
Os eventos de concentração alta São raros Não é concentração alta Eu estou perguntando o que é isso Toda hora você fala isso Eu entendi que você quer falar do pico Mas tenta achar uma coisa melhor Os picos da série são raros Fala o pico mesmo Que aí coloca o desenho da série Pode falar pico da série Outra coisa que isso indica mudanças do comportamento da série, seja por variação climática entre anos, seja por alterações no instrumento, e essas variações não são tratadas aqui como círculo regular, pois o conjunto abre apenas sete anos. Não entendi essa explicação não. 

**Daniel** [01:15:26]
Seria uma sazonalidade, mas não existe sazonalidade nesse conjunto assim. Não dá pra fazer um estudo tão grande. Mas também não gostei dessa parte não. 

**Luciana** [01:15:36]
É, você pode falar assim, o período da série abordada não mostrou uma sazonalidade, embora você fale que tem sazonalidade de horário 

**Daniel** [01:15:47]
existe a sazonalidade de horário existe a mas tem que separar 

**Luciana** [01:15:54]
tipo assim, eu não tenho a quantidade de porque se tem sete anos se tem sazonalidade anual, você consegue ver em sete anos então não ficou legal isso aqui não Você pode falar que não detectou nenhuma sazonalidade anual 

**Daniel** [01:16:13]
É, anual eu não diria que tem não Teria nos meses, por exemplo, nos meses mais secos O horário nos momentos no final do dia Seria isso? 

**Luciana** [01:16:25]
Então você pode detalhar isso melhor Agora, não são tratados aqui porque o conjunto cobre apenas 7 anos? Não, 7 anos dá pra ver Então você já viu Nesses sete anos não foi detectada essa anualidade anual, só essa anualidade, aí você coloca pelos meses e diária. Então detalha, isso tudo que você acabou de me explicar, explica aqui melhor. Os padrões descritos nessa sessão foram calculados apenas como os pontos medidos do período de desenvolvimento. Desenvolvimento do quê? 

**Daniel** [01:17:02]
2017, 2020 vai ser o treinamento 

**Luciana** [01:17:08]
Então não é desenvolvimento Então é um período de treinamento Agora Eu achei estranho Se a gente olha a série original E os resíduos É praticamente a mesma série Então Só o Aqui que muda os valores Mas aqui o comportamento Tá muito igual Aí eu pedi pra verificar se não tem erro nessa decomposição, porque tá a mesma série, olha só, mesmo comportamento igualzinho, tô achando estranho isso. 

**Daniel** [01:17:44]
Aham. 

**Luciana** [01:17:47]
A autocorrelação em uma hora é 0,83, 24 horas é 0,61. Explicar como isso foi calculado, pra que que isso foi feito, no que que ajudou você fazer isso. Eu acho que seu texto aqui tá muito confuso, não gostei não tem que explicar melhor essa parte dessas autocorrelações pra que que fez e isso, detalhar um pouco melhor é a formulação gostaria 

**Daniel** [01:18:20]
Luciana, essa autocorrelação eu fiquei em dúvida também se valia a pena falar sobre isso ou não porque falar sobre um dado um dado tem um valor aproximado do próximo sabe por exemplo, de uma hora pra outra 

**Luciana** [01:18:38]
em série temporal a gente já sabe disso você queria ver se o PM10 tem autocorrelação com o PM2,5 aí faz sentido, mas isso aqui de... a não ser que você fez você fez esse estudo pra ver o horizonte, era isso? 

**Daniel** [01:18:56]
ah foi não é só o horizonte mas tipo assim Para entender também, por exemplo, um modelo mais simples Que às vezes um modelo mais simples não entende tanta complexidade E fica muito apegado aos dados que estão próximos Por exemplo, às vezes ele só está repetindo a última hora anterior Aí, por exemplo, esse é um modelo mais simples que pega basicamente a data anterior Às vezes, por exemplo, a hora anterior Ele vai bem mas ele é só porque tem uma correlação muito alta com uma hora atrás, às vezes, aí por exemplo mostra que é só depois de 24 horas aí isso decai um bocado que aí seria 70% e uma semana antes já seria pra 46% 

**Luciana** [01:19:47]
tá, entendi agora se explicando faz sentido, mas eu acho que assim, seu texto tá muito confuso, então Porque aqui tá muito Parece que se tá resumido Eu entendi O que eu vou te aconselhar Faz um áudio Explicando Como se você estivesse apresentando O que você fez e tenta escrever Esse áudio Escreve esse texto Que eu fiz aqui E joga esse texto pra ver se fica melhor porque olha só, agora eu entendi então o que você vai explicar nessa sessão? pra que você fez isso? pra você saber até que ponto os dados pra trás porque você usou 48 horas até que ponto os dados pra trás era relevante, não é isso? 

**Daniel** [01:20:49]
sim, também 

**Luciana** [01:20:50]
então, aí você vai falar pra ver isso, então olha eu vi que a auto-parlação de uma hora é isso de 24 horas caia pra isso, beleza então 

**Daniel** [01:21:01]
então, depois Luciana, ao mesmo tempo isso que eu te falava esses modelos mais simples até o XGBoost eles tem um resultado muito bom assim, ele até em certas partes ele supera o seq2seq que é o modelo mais complexo mas é porque ele é um modelo assim Ele é mais linear A previsão dele é mais Simples, sabe? Não muito dinâmico Igual a série temporal em si É E meio que pra mim Eu não sei como eu vou explicar isso No TCC exatamente, mas eu vejo 

**Luciana** [01:21:45]
A princípio da parcimônia Quando o modelo usa menos parâmetros Ele é escolhido Você comparou vários modelos O XGBoost tem menos parâmetros que a rede neural se tem camadas se tem não sei o que, ele tem parâmetros mas ele tem menos então é o princípio da parcimônia que chama isso por exemplo você conhece o autoregressivo o AR o modelo AR, o do Arima 

**Daniel** [01:22:16]
sim 

**Luciana** [01:22:17]
então o AR, se eu tenho um AR4 e um AR por exemplo, um AR22 e um AR22 o AR2 porque ele tem menos parâmetros para ajustar isso se chama princípio da parcimônia então isso você pode explicar mas isso você vai explicar lá na frente nos seus resultados aqui pelo que eu estou entendendo essa autocorrelação dos elementos da série você está fazendo para tentar explicar por que você está usando o PM10 como variável exótica e por que que tá usando o horizonte de 48 pra trás e 24 pra frente você pode falar que fez estudos preliminares mas eu acho que, sinceramente ver se é relevante mesmo colocar isso aqui como estudo preliminar ou coloca isso no apêndice às vezes entendeu? joga isso lá pro apêndice E coloca lá Quando você colocou que usou 48 pra trás Aí você fala assim, ó, no apêndice Na seção tal Tá o estudo das Autocorrelações, estudos preliminares Pra determinar Eu jogarei isso no apêndice Pra não ficar bagunçado aqui Agora o que você chama de tarefa 

**Daniel** [01:23:48]
Que eu não gostei 

**Luciana** [01:23:49]
Então você vai colocar aqui Horizonte de previsão né, o que você fez aqui, o que você escolheu, e aí isso faz parte para você determinar seu horizonte de previsão, então aqui você vai falar, vai jogar lá no, ou você coloca esses textos juntos, né, determina o que, que usou 48, e 24 para frente, agora, o que que é isso? O horizonte de 24 horas corresponde a uma previsão para o dia seguinte, E a escala do padrão de qualidade do ar De 24 horas da resolução O que é isso? Eu não entendi nada disso aqui Quando você colocou Porque você baseou em 24 horas pra frente Por causa dessa resolução? 

**Daniel** [01:24:36]
Não, não foi por agição Acho que a própria IAC Pegou esse negócio aí Depois eu vou ler o que é que esse dia 

**Luciana** [01:24:44]
É, porque esse não ficou legal não Tá muito confuso Não entendi nada Porque olha só A escolha L48 É uma decisão de projeto Ela cobre dois ciclos diários E contém as defasagens de 24 e 48 Horas usadas pelas referências simples O que é isso? 

**Daniel** [01:25:09]
Referência simples eu não sei Tem que olhar lá na seção Mas eu cheguei a fazer Acho que eu não coloquei no texto A tempo Mas eu cheguei a comparar Colocar 24 horas de entrada 48 de entrada E prever 

**Luciana** [01:25:24]
Você não precisa mostrar todos esses resultados Isso você pode falar Fiz em estudos preliminares Isso com isso E cheguei que a melhor combinação foi isso Agora a referência sim Não colocar pra frente Tá vendo? Se a sessão tá lá na frente Traz o texto pra cá Porque não tá legal isso Então aqui tem que explicar melhor Aí E aqui, o treino ajusta os parâmetros dos modelos e as estatísticas de normalização. O que é isso? Estatística de normalização. Quando você faz normalização dos dados, você usa um dado de treinamento, mas não é que ela fez uma estatística de normalização. Isso não ficou legal, não. Preserva os limites de etapas exploratórias anteriores. O que é etapa exploratória anterior? 

**Daniel** [01:26:17]
São os próprios estudos anteriores das datas, ou seja, a meditação serve para a parada antecipada, para escolher o melhor modelo de treinamento, busca e treinamento, avaliação e treinamento anteriores. 

**Luciana** [01:26:36]
Eu também gostei disso. Eu acho que essa parte você tem que arrumar aqui, então assim, se eu tivesse parei de ler aqui, porque eu falei assim, não, eu quero que traz coisa pra frente, eu tenho que ler isso tudo ainda, já tô na metade ainda mas assim, dá uma relida nesse quadro seu aqui, pra mim pegar ele depois de novo tenta arrumar essas partes, trazer coisa pra frente que aí eu pego seu capítulo 4, o resto lá pra trás você vai arrumando melhor, mas dá uma relida nesse quadro, eu parei nesse tenta arrumar isso tudo que eu achei confuso o que está para trás você referencia o que está lá na frente tenta trazer para o lugar certo fazer uma um texto mais didático não falar de coisa lá na frente lá na frente você vai ver isso não, traz o lado da frente tenta construir essa sequência de texto e me passe que aí eu vou ler o capítulo 4 avanço para o 5 

**Daniel** [01:27:45]
vamos corrigir essas questões todas 

**Luciana** [01:27:47]
começa com 4 e aí enquanto eu estou lendo você vai para trás as correções desculpa a demora Daniel é porque realmente era leitura para a minha briga e eu sou muito demorada e não estou lenta então 

**Daniel** [01:28:06]
lá no final Eu coloquei muito tabela de resultado Provavelmente eu vou tirar muita coisa, tá? 

**Luciana** [01:28:16]
Tá 

**Daniel** [01:28:16]
Porque... 

**Luciana** [01:28:18]
Quando eu vi 98 páginas Se entregar isso pro pessoal de TCC O pessoal vai infartar Essas tabelas, o que você pode fazer Em vez de você Jogar fora Coloca no apêndice Que depois a gente corta E deixa aqui O que for mais relevante 

**Daniel** [01:28:39]
Ficou quebrado Pois é, ficou quebrado 

**Luciana** [01:28:45]
Ah, tenta arrumar isso aí Não tá legal isso aqui não Agora, de qualquer jeito, tá, Bela? Mesmo que você mostre aqui o resultado O importante é mostrar o que realmente importa E ter grito pra quem ganhou 

**Daniel** [01:28:59]
Tá, igual eu te falei Esse negócio de mostrar Eu não sei se eu coloquei o gráfico aqui simplesmente mostrar se você fazia a média móvel, qual que seria o resultado de fazer isso simplesmente, isso como fosse um baseline, né? 

**Luciana** [01:29:20]
É, não preciso fazer de tudo não, só porque senão, realmente, o que que você vai apresentar? Só o melhor resultado, você fala no geral de todos mas você só apresenta o melhor 

**Daniel** [01:29:33]
tá 

**Luciana** [01:29:33]
então faz o seguinte pra mim, assim que terminar começa no capítulo 4 na pisqueira que eu fiz aí dá uma lida traz pra frente deixa ele didático e manda pra mim, assim que eu conseguir terminar, aí enquanto eu tô lendo você vai fazendo pra trás 

**Daniel** [01:29:53]
tá bom Luciana 

**Luciana** [01:29:55]
e aí eu faço o 4 e o 5 e o 6 

**Daniel** [01:29:57]
agora começou uma barulhida aqui com cada eleição 

**Luciana** [01:30:01]
é, aqui também tá uma gritaria 

**Daniel** [01:30:03]
então, Luciana Obrigado, não tem problema 

**Luciana** [01:30:07]
Não, desculpa, estou atrasada Estou atrasada, mas vai dar certo Vamos pegar firme Para terminar 

**Daniel** [01:30:15]
Tá, joia Um abraço 

**Luciana** [01:30:18]
Um abraço também 

**Daniel** [01:30:21]
Boa noite, tchau 