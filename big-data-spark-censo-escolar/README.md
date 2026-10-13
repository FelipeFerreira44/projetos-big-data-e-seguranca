# PySpark – Censo Escolar 2021

Seis análises sobre o Censo Escolar 2021 (INEP) usando RDDs do PySpark: contagens por município e região, soma e média de colunas, e agrupamentos com ordenação.

## Como rodar
```bash
pip install pyspark
python censo_escolar_2021.py censo_escolar_2021.csv
```
O CSV (separador `;`) não está no repositório por causa do tamanho. Baixe-o no portal de dados abertos do INEP.

## Nota técnica
Os filtros de linhas vazias (colunas 338 e 305) ficam em variáveis separadas, para não reduzir o conjunto de escolas das outras atividades.

## Tecnologias
Python 3, PySpark (RDD).
