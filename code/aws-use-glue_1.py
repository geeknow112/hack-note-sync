from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.dynamicframe import DynamicFrame

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

# データフレームを取得する
persons = glueContext.create_dynamic_frame.from_catalog(
	database="mydb",
	table_name="persons"
).toDF()

# 年齢が30歳以上の人だけを抽出する
filtered_persons = persons.filter("age >= 30")

# 別のデータストアにデータをロードする
glueContext.write_dynamic_frame.from_options(
	frame=DynamicFrame.fr_1.pyF(filtered_persons, glueContext, "filtered_persons"),
	connection_type="s3",
	connection_options={
		"path": "s3://mybucket/filtered_persons",
	},
	format="csv"
)
