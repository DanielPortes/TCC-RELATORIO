# Repository Guidelines

## Project Structure & Module Organization
The repository has two main parts. The thesis sources live at the root: `main.tex` assembles the document, `tex/capitulos/` stores chapter files, `tex/pretextuais/` holds front matter, `tex/config/` contains the ABNTeX class and style files, `figuras/` stores images, and `referencias.bib` is the bibliography database. The experimental code lives in `codigo/`: `src/` contains data, model, and training modules; `pipelines/flows/` and `pipelines/tasks/` define Prefect orchestration; `configs/` holds Hydra YAMLs; `tests/` contains pytest suites; `scripts/` and `analysis/` support operations and reporting; `data/` stores station spreadsheets.

## Preferências da Orientadora para a Escrita do TCC
As preferências abaixo são uma inferência prática a partir das correções, guias de reescrita e exigências já incorporadas ao relatório. Use esta seção como regra de escrita para qualquer alteração em `tex/`: a orientadora parece priorizar controle metodológico, coerência narrativa e conclusões defensáveis, mais do que frases promocionais sobre modelos.

### Narrativa Central Esperada
O TCC deve parecer um único estudo coerente: previsão horária de PM2.5 na estação Sapo, no recorte CMD, usando 48 horas de entrada para prever as 24 horas seguintes, split cronológico 70/15/15 e protocolo comparável entre modelos. Não deixe narrativas antigas sobre Cascata/Piratininga, horizonte de 12 horas, agregação diária, SAITS ou ablações iniciais voltarem ao centro do texto. Esses elementos só devem aparecer como histórico, contexto auxiliar ou exploração anterior, sempre identificados como não pertencentes ao resultado principal.

A contribuição deve ser formulada como estudo experimental comparativo e rastreável, não como criação de uma nova arquitetura. A forma mais segura é afirmar que o trabalho consolida um protocolo reprodutível, compara abordagens neurais e tabulares sob o mesmo contrato de dados e analisa compromissos entre erro médio, horizonte de previsão, suavização e eventos de maior concentração.

### Postura Acadêmica Preferida
- Prefira afirmações cautelosas e defensáveis. Evite dizer que o trabalho "prova", "garante", "resolve" ou estabelece uma arquitetura universalmente superior.
- Escreva em português brasileiro claro, formal e direto, com pontuação revisada e padrão acadêmico compatível com ABNT2.
- Diga exatamente o que foi comparado, sob qual contrato de dados, com qual split, em qual conjunto de avaliação e com quais métricas. Comparações precisam ser justas em horizonte, dados, orçamento de validação/HPO, disponibilidade causal de variáveis e métrica reportada.
- Explique escolhas metodológicas, não apenas liste decisões. Um bom parágrafo informa o que foi feito, por que foi feito, que evidência sustenta a escolha e qual limitação permanece.
- Separe resultado oficial de histórico exploratório. Resultados de scripts antigos, outros horizontes, outras estações, outros conjuntos de atributos ou HPO não final não devem sustentar a conclusão principal.
- Trate inspeção visual e métricas em conjunto. Um gráfico pode revelar suavização, atraso ou comportamento em picos, mas não substitui MAE/RMSE/R2 sem suporte métrico explícito.
- Discuta resultados negativos ou mistos com honestidade. Se atenção, scheduled sampling ou perdas ponderadas não venceram globalmente, diga isso e explique em que aspecto ajudaram ou não ajudaram.
- Use limitações como parte do argumento científico. Orçamento limitado de HPO, avaliação em uma única estação, esparsidade de variáveis meteorológicas e indisponibilidade causal de PM10/PTS futuros devem aparecer quando forem relevantes.

### Vocabulário Preferido
Use termos que transmitam cautela metodológica:
- "estudo experimental comparativo" em vez de "modelo proposto" para descrever a contribuição central;
- "protocolo rastreável" ou "protocolo comparável" em vez de afirmações vagas de robustez;
- "modelo de referência tabular forte" para o XGBoost, não "baseline simples" ou linha de base descartável;
- "variáveis causalmente disponíveis" para entradas do decodificador conhecidas no instante da previsão;
- "teste externo", "holdout cronológico" ou "avaliação fora da amostra" para o bloco final de teste;
- "eventos de maior concentração", "picos" e "cauda" ao discutir comportamento em PM2.5 alto;
- "função de perda absoluta ponderada" para `weighted_l1`, não regularização L1 dos parâmetros.

Evite ou qualifique expressões como "estado da arte", "produção", "operacional definitivo", "superioridade do Attention-LSTM", "melhor modelo em geral" e "baseline simples", a menos que o trecho prove exatamente essa afirmação.

### Forma Esperada de Enquadrar Resultados
O resultado final deve ser escrito com nuance:
- A LSTM direta é a vencedora principal por erro médio no protocolo final.
- O XGBoost continua sendo um modelo de referência tabular forte e é essencial para interpretar se os modelos neurais realmente agregam valor.
- O Seq2Seq com atenção e `weighted_l1` ficou competitivo e preservou melhor parte da amplitude/cauda, mas não deve ser descrito como vencedor global se MAE/RMSE/R2 não sustentarem isso.
- Experimentos `oracle` com variáveis futuras mostram limite informacional do contrato atual, não resultado operacional, porque usam informação indisponível no instante real de previsão.

### Molde de Parágrafo Preferido
Em seções metodológicas, prefira parágrafos com esta lógica:

1. Defina precisamente a decisão, objeto ou experimento.
2. Justifique por que isso importa para a tarefa de previsão.
3. Conecte a decisão ao protocolo final, artefato, figura, tabela ou referência.
4. Explique a consequência para comparabilidade ou interpretação.
5. Declare a limitação quando a escolha restringir a conclusão.

Molde útil: "Neste trabalho, X foi adotado para Y. Essa escolha se justifica por Z. Para evitar W, o protocolo usa K. Assim, a comparação mede A sob condições B, mas não permite concluir C."

### Checklist Antes de Editar o Texto
Antes de alterar qualquer capítulo, verifique:
- O parágrafo preserva Sapo/CMD, previsão horária de PM2.5, tarefa 48 -> 24 e avaliação cronológica como eixo principal?
- A afirmação é sustentada por artefato atual, tabela, figura, configuração ou referência bibliográfica?
- Experimentos históricos ou exploratórios estão claramente rotulados como tais?
- Os modelos comparados usam o mesmo horizonte, split, contrato de atributos, métrica e premissas de HPO/validação?
- O texto distingue erro médio de comportamento em picos/cauda?
- O texto evita apresentar atenção, scheduled sampling ou `weighted_l1` como vitória central sem suporte métrico?
- O texto explica por que proxies de PM10, máscara de alvos imputados e variáveis causais no decodificador importam?
- O texto evita prometer implantação operacional ou superioridade universal de modelo?
- As limitações são concretas, e não genéricas?

## Build, Test, and Development Commands
Use a local LaTeX toolchain at the repository root, for example `latexmk -pdf main.tex`; if `latexmk` is unavailable, run `pdflatex main.tex`, `bibtex main`, then `pdflatex main.tex` twice. For the Python pipeline, `make -C codigo start-services` starts MLflow and Prefect, `make -C codigo start-worker` registers deployments and starts the local worker, `make -C codigo dry-run` launches the smoke deployment, and `make -C codigo quick-run-lstm-direct` runs the single debug configuration currently wired in the `Makefile`. Use `pytest codigo/tests -q` for tests and `make -C codigo clean` to remove runtime caches and logs.

## Coding Style & Naming Conventions
Python code follows PEP 8 conventions: 4-space indentation, `snake_case` for modules and functions, `PascalCase` for classes such as `DirectLSTMLightningModule`, and type hints when they clarify interfaces. Keep YAML config names lowercase and descriptive, for example `quick_run_lstm_direct.yaml`. LaTeX chapter files use numeric prefixes like `cap_04_metodologia.tex`; figure filenames are lowercase with hyphens. No formatter or linter config is committed here, so avoid large cosmetic rewrites and keep imports grouped consistently.

## Testing Guidelines
Tests are pytest-based and live in `codigo/tests/`. Name new files `test_*.py` and prefer focused smoke or regression tests around data leakage, dataset shapes, and model forward passes. No coverage threshold is enforced in this checkout, but any change in `codigo/src/` or `codigo/pipelines/` should include tests or a short justification in the PR.

## Commit & Pull Request Guidelines
This checkout does not include `.git` history, so follow a simple imperative commit style with an optional scope, such as `codigo: fix walk-forward split edge case` or `tex: update metodologia references`. Pull requests should state which area changed, list config or data assumptions, link the related task, and include screenshots when plots, MLflow outputs, or generated PDF pages change. Avoid committing generated artifacts such as `.logs/`, `.pids/`, `mlartifacts/`, or temporary analysis outputs unless they are the intended deliverable.
