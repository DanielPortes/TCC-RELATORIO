# Orientações do repositório (relatório do TCC)

Texto do TCC "Estudo comparativo de modelos para previsão horária de PM2,5" (UFJF, graduação em Ciência da Computação).
O código dos experimentos fica em outro repositório (`TCC-wsl`, pasta `scripts/thesis/`); aqui só há o texto.

## Estrutura e comandos
- `main.tex` monta o documento; capítulos em `tex/capitulos/`, resumo em `tex/pretextuais/`, figuras em `figuras/`, bibliografia em `referencias.bib`.
- `tex/tabelas/` é gerado pelo código (`scripts/thesis/analyze.py` no `TCC-wsl`). Mudança de rótulo ou número se faz lá, não à mão.
- Compilar: `latexmk -pdf main.tex`. Pacote LaTeX novo também entra em `.github/texlive-packages.txt`, senão o build do GitHub quebra.
- Release com PDF: `bash scripts/criar_release_pdf.sh` (exige árvore limpa e build passando).

## Antes de escrever
Leia `revisoes-orientadora/CRITICAS_E_PREFERENCIAS_ORIENTADORA.md`. Ele consolida as quatro rodadas de correção da orientadora.
Ela já leu o Resumo, os Capítulos 1 a 3 e o Capítulo 4 até a Seção 4.2.1. O resto ainda não foi lido.

## Regras de escrita
São as correções que ela mais repetiu. Quebrar qualquer uma é regressão.

1. **Definir antes de usar.** Termo, sigla e símbolo são explicados no primeiro uso, com a sigla depois da explicação.
2. **Referenciar só para trás.** Nada de "como será visto adiante". Se algo é usado antes, a explicação sobe.
3. **Um nome por conceito, no texto inteiro:** pico (PM2,5 ≥ 35 µg/m³), variável exógena, neurônio, conjunto de dados, teste preliminar (2020), teste final (2021 a 2023), regressão Ridge, Seq2Seq com atenção e Seq2Seq com atenção por faixas. Contagem dos modelos: 4 famílias, 7 treinados, 5 previsões ingênuas.
4. **Texto, figura e fórmula andam juntos.** A figura fica perto do texto que a chama, e o texto diz o que observar. No Capítulo 2, figuras da literatura, não próprias.
5. **Equações** em `equation`, com `\label` e `\ref`, seguidas de "onde ..." explicando cada símbolo.
6. **Afirmação incomum pede referência**, ou é dita como escolha deste trabalho.
7. **Cada capítulo no seu papel.** Introdução: problema, dificuldade, lacuna e o que o trabalho faz, sem metodologia. Capítulo 2: só conceitos usados. Capítulo 3: literatura. Capítulo 4: o que foi feito. Capítulo 5: resultados.
8. **Nada falso ou polêmico:** "XGBoost é para dados tabulares", "acurácia" em regressão, "estudo experimental" (use "comparativo"), "prova", "garante", "estado da arte".
9. **Ganho só se afirma quando o intervalo de confiança exclui o zero.** Caso contrário é empate estatístico. Números vêm das tabelas geradas.

### Capítulo 1 (especificação dela)
- Ordem: problema do PM2,5 e saúde; dificuldade de prever; lacuna (modelos variados, sem consenso e sem comparativo); o que este trabalho faz, com a estação no fim. Pode dizer qual modelo foi melhor, sem métricas.
- Sem seção de motivação e sem "pergunta de pesquisa" escrita. Objetivo geral: comparar diferentes modelos para a previsão horária de PM2,5 nas 24 horas seguintes. Objetivos específicos são as etapas da metodologia.
- Tem de dar vontade de continuar lendo: narrativo, concreto, sem jargão.

## Clareza e tamanho
É um TCC de graduação: direto e fácil de acompanhar.

- Frases curtas, uma ideia por parágrafo, palavra comum no lugar de jargão.
- Cada resultado é dito uma vez. Não repetir no fim da seção, na discussão e na conclusão.
- Não contar a história do projeto ("estudos preliminares", "versão anterior", "foi corrigido"). O texto descreve o procedimento final.
- No corpo só entra o que responde à comparação entre os modelos. Verificações e tabelas complementares vão para o apêndice, citadas em uma frase.
- Não acrescentar experimento, métrica, seção ou figura sem o autor pedir. O documento tem 90 páginas e não deve crescer.

## Estado dos resultados
XGBoost e regressão Ridge têm os menores erros e empatam entre si; as redes ficam atrás; todos os modelos subestimam os picos.
Não afirmar que a falta de meteorologia é o que limita a previsão: o teste com as estações vizinhas e com a meteorologia do Aeroporto não reduziu o erro (Seção 5.5 e tabela no apêndice).

## Antes de entregar
- [ ] As nove regras acima foram conferidas no trecho alterado?
- [ ] O PDF compila sem referência indefinida e sem linha passando da margem?
- [ ] As figuras e tabelas ficaram perto do texto que as chama? (Conferir no PDF, não no `.tex`.)
- [ ] Os números citados batem com as tabelas?
- [ ] O trecho ficou mais curto ou igual, e não mais longo?

## Git
Commits curtos no imperativo, com escopo (`tex:`, `docs:`, `ci:`). Não citar ferramentas de IA em commits, branches ou autoria. PDFs de release e a pasta `tmp/` não entram no repositório.
