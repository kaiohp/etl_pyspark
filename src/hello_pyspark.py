from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import avg, col, count, when

spark = SparkSession.builder.master('local').appName('hello').getOrCreate()

data = [
    ('Kim', 'Park', 12, 'KOR'),
    ('James', 'Smith', 32, 'USA'),
    ('Michael', 'Rose', 19, 'USA'),
    ('Robert', 'Williams', 17, 'CAN'),
    ('Maria', 'Jones', 39, 'CAN'),
    ('Marcos', 'Santi', 25, 'BRA'),
    ('Raimundo', 'Santos', 73, 'BRA'),
]

columns = ['first_name', 'last_name', 'age', 'country']

df: DataFrame = spark.createDataFrame(data=data, schema=columns)


df1 = df.withColumn(
    'life_stage',
    when(col('age') < 13, 'child')  # noqa: PLR2004
    .when(col('age').between(13, 17), 'teenager')
    .when(col('age').between(18, 64), 'adult')
    .otherwise('elderly'),
)

df1.show()
df1.groupBy('life_stage').agg(avg('age'), count('*')).sort('life_stage').show()

spark.stop()
