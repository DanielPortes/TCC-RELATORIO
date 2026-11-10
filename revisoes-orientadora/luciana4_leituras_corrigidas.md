# Rodada 4: leituras da letra corrigidas

Releitura das páginas 6 e 15 a 51 do PDF anotado (`luciana4_pdf_anotado.pdf`) em resolução maior, feita por três leitores independentes em 10/11/2026. Foram 198 marcas. Este arquivo lista só os pontos em que a leitura registrada em `luciana4_resumo_das_correcoes.md` estava errada ou incompleta. Em caso de conflito, vale este arquivo.

| PDF | Trecho impresso | Leitura anterior | Leitura corrigida |
|---|---|---|---|
| 6 | "…e *Extreme*… uma regressão linear como referências" | "e **da** regressão linear" | O "e" antes de *Extreme* virou vírgula; na margem há "e". Não há "da". |
| 16 | 1.1 Motivação | "tirar **uma** seção" | "tirar **essa** seção e deixar o texto corrido." |
| 20 | "(de t+1 a t+H)" e "L é o comprimento" | "a ordem que representa" ligada ao parêntese | Parênteses em volta de "de t+1 a t+H". "**a ordem que representa**" entra depois de "L é". |
| 20 | "exemplos, cada um formado" | não registrada | "cada um" riscado. |
| 21 | Legenda da Fig. 2.1 | "numerar" | "**arrumar**" (a legenda tinha subido). |
| 21 | "…é uma previsão, e não uma observação." | não registrada | "**conhecida.**" inserida depois de "observação". |
| 21 | "atributos conhecidos de antemão para o horizonte" | só a inserção | Trecho riscado e, por cima, "conhecidos como variável exógena". |
| 21 | "Defasagem" e \(\mathbf{x}_{t-L+1:t}\) | "subir defasagem e exógena" | Duas marcas: "isso é defasagem então deixa junto" e "falar antes de usar na fórmula!". |
| 22 | Seção "Previsão Multi-Horizonte" | "Só importaria **uma** seção" | Título riscado; "Só importaria **essa** seção se tivesse comparado as 3 formas!" (no áudio, ela admite manter). |
| 23 | "capacidade de generalização" | ", e o que chamamos de…" | ", o que chamamos de capacidade de generalizar." |
| 24 | indicador de ausência | "não **faz** isso" | "Se o seu modelo não **fez** isso, retire esse texto, senão vai criar perguntas do por quê não fez!" |
| 27 | "Elas leem" | não registrada | Circunflexo em "lêem" (grafia antiga; não seguir). |
| 28 | Nota do topo | "um **texto** padrão" | "um **termo** padrão da literatura, não o que você acha que é!" |
| 29–30 | "duas partes. O codificador… O decodificador" | não registrada | Numeração "1)" e "2)"; "apresenta como cada estado hj é calculado". |
| 32 | Figura do *teacher forcing* | "**deveria ter** isso na seção anterior" | "esse texto está ótimo. A figura conversa com o texto, **queria** isso na seção anterior." |
| 33 | Decodificadores sem realimentação | "não é **seu** modelo" | Trecho riscado; "mas aí não é **esse** modelo." (a objeção é de pertinência à seção). |
| 34 | Margem | "informações **jogadas**" | "seu texto não tem contexto. Várias informações **fragmentadas**". |
| 38 | Bootstrap | "não falou se você usa isso" | "mas **só falar se você usar** isso." |
| 43 | fim da 3.5 | "isso não é um diferencial; todo trabalho que compara faz isso." | Continua: "…, não fala porque isso é a base p/ comp." |
| 46 | Título "Escolha da Estação" | "**Faça** pergunta lá em cima" | "**Fiz a** pergunta lá em cima, direciona a explicação para essa seção!" |
| 46 | três "o que é isso?" | "volume suficiente", "variável auxiliar útil" | "variável auxiliar"; "mínimo de eventos altos"; "não a estação mais previsível". |
| 46 | rodapé | terminava em "dar uma aula sobre isso." | Continua: "Faz a apresentação dessa parte e escreve." |
| 47 | "concentração alta" | "o que é isso?" na "Entrada propagada" | "o que é isso?" é de "concentração alta"; "explicar melhor" é da entrada propagada. |
| 49 | "(Seção 4.5.2)" | "isso é p/ trás, não p/ frente" | "Não pode fazer fora de ordem, vc só cita p/ trás não p/ frente." |
| 50 | "teste histórico" | "o que é isso?" | Só "histórico" rabiscado; o "O que é isso?" é de "preservam os limites de etapas exploratórias". |

## Mantido contra a anotação, de propósito

- **Hora do dia como atributo** (PDF 20–21): é entrada usual; no áudio ela aceitou com referência e exemplo.
- **Seção "Previsão Multi-Horizonte"** (PDF 22): as três estratégias são comparadas no trabalho.
- **"leem"** (PDF 27): grafia vigente.
- **"3 camadas da LSTM?"** (PDF 27): é uma única rede desdobrada no tempo.
- **Decodificador sem realimentação** (PDF 33): é o usado pelos dois Seq2Seq com atenção; o parágrafo foi mantido e passou a dizer que é um terceiro tipo, ao qual o *teacher forcing* não se aplica.
- **Árvores do impulsionamento** (PDF 34) e **MSE × RMSE** (PDF 37): o texto está correto e explica a dúvida.
- **Partículas totais em suspensão** (áudio): a coluna existe (86% de cobertura).
- **Critério da estação** (áudio): o critério sugerido escolheria uma estação quase sem picos.
