# MapReduce com mrjob – Colisões de veículos em Nova York

Sete jobs MapReduce em Python (biblioteca `mrjob`) sobre o conjunto de dados público de colisões de veículos de Nova York (NYC Open Data, "Motor Vehicle Collisions – Crashes").

| Job | O que calcula |
|---|---|
| `atividade1.py` | acidentes por ano |
| `atividade2.py` | ciclistas feridos no Bronx por ano |
| `atividade3.py` | acidentes por bairro (borough) e ano |
| `atividade4.py` | média de pessoas feridas por acidente, por ano |
| `atividade5.py` | média de ciclistas feridos por bairro e ano |
| `atividade6.py` | mês de maior número de acidentes por bairro (2 etapas, com combiner) |
| `atividade7.py` | média de feridos em 2022 por bairro, com maior e menor média (2 etapas) |

## Como rodar
```bash
pip install mrjob
python atividade1.py Motor_Vehicle_Collisions_-_Crashes.csv > resultado1.txt
```
O arquivo de dados não está no repositório por causa do tamanho. Baixe-o no portal NYC Open Data.

## Nota técnica
O campo `LOCATION` do CSV tem vírgula dentro de aspas. Por isso os jobs usam `csv.reader` em vez de `split(",")`, que deslocaria as colunas seguintes.

## Tecnologias
Python 3, mrjob (MapReduce).
