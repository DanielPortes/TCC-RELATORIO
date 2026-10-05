# Repository Guidelines

## Project Structure & Module Organization
The repository has two main parts. The thesis sources live at the root: `main.tex` assembles the document, `tex/capitulos/` stores chapter files, `tex/pretextuais/` holds front matter, `tex/config/` contains the ABNTeX class and style files, `figuras/` stores images, and `referencias.bib` is the bibliography database. The experimental code lives in `codigo/`: `src/` contains data, model, and training modules; `pipelines/flows/` and `pipelines/tasks/` define Prefect orchestration; `configs/` holds Hydra YAMLs; `tests/` contains pytest suites; `scripts/` and `analysis/` support operations and reporting; `data/` stores station spreadsheets.

## Preferências da Orientadora para a Escrita do TCC

Esta seção substitui uma versão anterior que era inferência. Agora vem de três rodadas de correção da orientadora (áudios transcritos e anotações manuscritas
lidas por visão): ver `revisoes-orientadora/CRITICAS_E_PREFERENCIAS_ORIENTADORA.md` (consolidado), `revisoes-orientadora/anotacoes_manuscritas_pdf.md` e as
transcrições `revisoes-orientadora/luciana{1,2,3}_transcricao.md`. **Antes de editar qualquer capítulo, leia o consolidado.** Ela revisou até agora o Resumo, o Capítulo 1 (três vezes)
e o Capítulo 2; os Capítulos 3 a 6 ainda não foram lidos.

### Regras de escrita (em ordem de frequência nas correções)
1. **Defina antes de usar; sigla depois da explicação.** "Coloca a sigla depois da explicação, não antes." Vale para termos e para símbolos matemáticos (L, h, y, ȳ, ε, p_TF...) no ponto do primeiro uso.
   Cada "o que é isso?" dela indica definição faltando.
2. **Texto, figura e fórmula andam juntos.** A figura não é autoexplicativa: o texto direciona o que observar e liga cada trecho da fórmula à figura. A figura vem antes do texto que a usa.
   Ela prefere figuras padrão da literatura (LSTM com gates, Seq2Seq) às figuras próprias.
3. **Toda equação em `equation` com `\label` e citada por `\ref`**, nunca `$$`; todos os elementos são explicados. Notação padrão (saída y/ŷ, não o/h), igual na figura e na fórmula.
4. **Afirmação incomum exige referência** e deve ser apresentada como escolha daquela referência ("essa referência fez isso e achei importante replicar"). Pergunta dela: "que referência comprova isso?"
   Exemplos: métricas só nos pontos observados (ela nunca viu), uma referência de aplicação por estratégia (recursiva, direta, codificador-decodificador).
5. **Cada capítulo no seu papel.** Introdução: problema, dificuldade, lacuna, o que o trabalho faz, sem janela, recorte, 48/24, métricas ou variáveis. Fundamentação: só conceitos e como o
   modelo funciona; aplicação em séries temporais é do Capítulo 3. Justificativa da estação é da metodologia.
6. **Motivação é o que levou a fazer o trabalho**, não um resumo dele. Sem seção "Problema de pesquisa" separada nem "pergunta que orienta este TCC".
7. **Nada falso ou polêmico.** Proibido: "XGBoost é para dados tabulares" (e a dicotomia tabular × redes: as duas exigem a série virar um problema supervisionado); "acurácia" em regressão (use "qualidade de
   previsão"); "estudo experimental" (use "comparativo"); "aprendizado de máquina e aprendizado profundo" como coisas opostas; "a comparação entre trabalhos nem sempre é direta".
8. **Enxugar.** Sem resumo de capítulo, sem "isto é…" óbvio, sem parágrafo solto sem contexto, sem título que prometa mais do que o texto entrega.
9. **Leitor da introdução e do resumo**: não conhece "recorte CMD", "presença pareada", "mascaramento", "LSTM direta", "variáveis auxiliares futuras". Use linguagem comum.

### Postura acadêmica (mantida, ainda válida)
- Afirmações cautelosas e defensáveis; nada de "prova", "garante", "estado da arte", "melhor modelo em geral".
- Diga o que foi comparado, sob que contrato de dados, split, avaliação e métricas. Separe resultado oficial (`scripts/thesis`) de histórico exploratório.
- Resultados negativos ou mistos são escritos com honestidade; ganho só é afirmado quando o intervalo de confiança exclui zero, senão é empate estatístico.
- Limitações concretas (estação única, teste histórico já consultado, ruído da série, ausência de meteorologia na estação) fazem parte do argumento.
- Vocabulário: "estudo comparativo", "protocolo rastreável", "variáveis causalmente disponíveis", "holdout cronológico", "função de perda absoluta ponderada" (não "regularização L1"), "impulsionamento por gradiente (XGBoost)".

### Estado científico atual (para não reescrever narrativas antigas)
Os resultados oficiais vêm de `TCC-wsl/runtime/reports/thesis_protocol/tables/` (protocolo único, 2017 a 2023, teste histórico jun-dez/2020 e holdout 2021-2023). Em resumo: XGBoost por horizonte e Ridge ficam no topo ou empatados
no topo; os Seq2Seq com atenção superam a LSTM direta, mas não o XGBoost no holdout; o desenho "novo" empata com o canônico; ninguém prevê bem os picos; o erro está perto do piso de ruído da série. **A LSTM direta não é
mais a vencedora**; não repita a narrativa antiga. Redação dos resultados só depois de ler as tabelas geradas.

### Processo com a orientadora
Um capítulo por vez, fechado antes de passar ao próximo; ela lê e comenta o **PDF**; ao fechar um capítulo, gerar o PDF e enviá-lo por WhatsApp; o resumo é reescrito por último; uso de IA na redação é aceito desde que
não introduza afirmações erradas ou polêmicas.

### Checklist antes de editar o texto
- [ ] Todo termo, sigla e símbolo tem definição no primeiro uso, com a sigla depois da explicação?
- [ ] O trecho está no capítulo certo (conceito no 2, literatura aplicada no 3, decisões no 4, resultados no 5)?
- [ ] Toda figura, tabela e equação é chamada no texto com instrução do que observar, e tem `\label`/`\ref`?
- [ ] A afirmação se apoia em tabela/figura atual do protocolo, ou em referência citada? Escolhas de projeto estão declaradas como tais?
- [ ] Nada falso ou polêmico (ver regra 7)? Nada redundante?
- [ ] Os modelos comparados usam o mesmo horizonte, split, entradas, métrica e orçamento de HPO?
- [ ] O texto distingue erro médio de comportamento em picos, e não promete implantação operacional nem superioridade universal?

## Build, Test, and Development Commands
Use a local LaTeX toolchain at the repository root, for example `latexmk -pdf main.tex`; if `latexmk` is unavailable, run `pdflatex main.tex`, `bibtex main`, then `pdflatex main.tex` twice. For the Python pipeline, `make -C codigo start-services` starts MLflow and Prefect, `make -C codigo start-worker` registers deployments and starts the local worker, `make -C codigo dry-run` launches the smoke deployment, and `make -C codigo quick-run-lstm-direct` runs the single debug configuration currently wired in the `Makefile`. Use `pytest codigo/tests -q` for tests and `make -C codigo clean` to remove runtime caches and logs.

## Coding Style & Naming Conventions
Python code follows PEP 8 conventions: 4-space indentation, `snake_case` for modules and functions, `PascalCase` for classes such as `DirectLSTMLightningModule`, and type hints when they clarify interfaces. Keep YAML config names lowercase and descriptive, for example `quick_run_lstm_direct.yaml`. LaTeX chapter files use numeric prefixes like `cap_04_metodologia.tex`; figure filenames are lowercase with hyphens. No formatter or linter config is committed here, so avoid large cosmetic rewrites and keep imports grouped consistently.

## Testing Guidelines
Tests are pytest-based and live in `codigo/tests/`. Name new files `test_*.py` and prefer focused smoke or regression tests around data leakage, dataset shapes, and model forward passes. No coverage threshold is enforced in this checkout, but any change in `codigo/src/` or `codigo/pipelines/` should include tests or a short justification in the PR.

## Commit & Pull Request Guidelines
This checkout does not include `.git` history, so follow a simple imperative commit style with an optional scope, such as `codigo: fix walk-forward split edge case` or `tex: update metodologia references`. Pull requests should state which area changed, list config or data assumptions, link the related task, and include screenshots when plots, MLflow outputs, or generated PDF pages change. Avoid committing generated artifacts such as `.logs/`, `.pids/`, `mlartifacts/`, or temporary analysis outputs unless they are the intended deliverable.
