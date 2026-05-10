Descrição
=====
Este repositório possui arquivos tex para produção de TCCs do Departamento de Ciência da Computação da UFJF. Os arquivos foram gerados por reuso de outros arquivos tex. As citações seguem o projeto abntex2.


Como usar
=========
Para começar a utilizar, leia atentamente o arquivo modelo.pdf. Para editar, atualize os arquivos pretexto.tex e modelo.tex.

Manual de citações
======
Caso precise realizar citações mais detalhadas, como citação de páginas de trabalhos ou citações de citações, sugerimos ler o conteúdo da pasta "manual citações".

Release do PDF
======
Para publicar uma nova versão do PDF mantendo o histórico, use:

```bash
scripts/criar_release_pdf.sh
```

O script cria uma tag nova no formato `release-AAAA-MM-DD-HHMM`, publica um novo release no GitHub e deixa o workflow `Build PDF` anexar o PDF gerado. O workflow não sobrescreve mais um PDF já anexado a um release existente.
