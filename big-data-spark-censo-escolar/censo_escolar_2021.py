"""Censo Escolar 2021 com PySpark (RDDs).

Uso:
    pip install pyspark
    python censo_escolar_2021.py censo_escolar_2021.csv
Cada atividade grava a saída em uma pasta atividadeN.txt.
"""
import sys

from pyspark.sql import SparkSession

caminho = sys.argv[1] if len(sys.argv) > 1 else "censo_escolar_2021.csv"

spark = SparkSession.builder.appName("CensoEscolar2021").getOrCreate()
sc = spark.sparkContext

linhas = sc.textFile(caminho)
# rdd = todas as escolas (sem o cabeçalho). Não é sobrescrito abaixo:
# as atividades que precisam de filtros usam variáveis próprias.
rdd = linhas.filter(lambda x: x.split(";")[0] != "NU_ANO_CENSO")

# Atividade 1: número de escolas em Curitiba
a1 = (rdd.map(lambda x: (x.split(";")[6], 1))
         .filter(lambda x: x[0] == "Curitiba")
         .reduceByKey(lambda x, y: x + y))
a1.coalesce(1).saveAsTextFile("atividade1.txt")

# Atividade 2: número de escolas por região
a2 = (rdd.map(lambda x: (x.split(";")[1], 1))
         .reduceByKey(lambda x, y: x + y)
         .sortByKey())
a2.coalesce(1).saveAsTextFile("atividade2.txt")

# Atividade 3: município com maior soma das colunas 338, 360 e 363
# (só linhas com a coluna 338 preenchida)
rdd_338 = rdd.filter(lambda x: x.split(";")[338] != "")


def soma_colunas(x):
    c = x.split(";")
    return int(c[338] or 0) + int(c[360] or 0) + int(c[363] or 0)


a3 = (rdd_338.map(lambda x: ((x.split(";")[1], x.split(";")[6]), soma_colunas(x)))
             .reduce(lambda x, y: x if x[1] > y[1] else y))
sc.parallelize([a3]).coalesce(1).saveAsTextFile("atividade3.txt")

# Atividade 4: média da coluna 305 por região (só linhas com a coluna 305 preenchida)
rdd_305 = rdd.filter(lambda x: x.split(";")[305] != "")
a4 = (rdd_305.map(lambda x: (x.split(";")[1], (int(x.split(";")[305]), 1)))
             .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
             .mapValues(lambda x: round(x[0] / x[1])))
a4.coalesce(1).saveAsTextFile("atividade4.txt")

# Atividade 5: contagem por (coluna 15, coluna 17), usando todas as escolas
a5 = (rdd.map(lambda x: ((x.split(";")[15], x.split(";")[17]), 1))
         .reduceByKey(lambda x, y: x + y))
a5.coalesce(1).saveAsTextFile("atividade5.txt")

# Atividade 6: contagem por (coluna 4, coluna 15), ordenada do maior para o menor
a6 = (rdd.map(lambda x: ((x.split(";")[4], x.split(";")[15]), 1))
         .reduceByKey(lambda x, y: x + y)
         .sortBy(lambda x: x[1], ascending=False))
a6.coalesce(1).saveAsTextFile("atividade6.txt")

spark.stop()
