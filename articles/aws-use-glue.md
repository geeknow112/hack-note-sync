AWS Glueとは？初心者向け解説と使い方
AWS,Glue,ETL,データ分析
aws-use-glue

こんにちは。今回は、AWS初心者に向けて、AWS Glueとは何か、どのように使われるかについて解説します。AWS Glueは、ETL（Extract, Transform, Load）を行うための完全マネージド型のサービスで、データ分析における重要な役割を果たします。初めて聞く人にとっては、何ができるサービスなのか、どのように使われるのか、理解するのは大変かもしれません。しかし、この記事を読むことでAWS Glueの基本的な概念を理解し、使い方を学ぶことができます。

## AWS Glueとは

AWS Glueは、AWSが提供するETLサービスで、異なるデータソースからデータを抽出し、変換してから、別のデータストアにロードすることができます。

ETLとは、データウェアハウスやビッグデータ分析などでよく使われる用語で、以下の3つのプロセスを指します。

- Extract（抽出）：データをデータソースから抽出する
- Transform（変換）：データを必要な形式に変換する
- Load（ロード）：変換したデータを別のデータストアにロードする

AWS Glueは、これらのプロセスのすべてを自動化することができます。また、サーバーレスアーキテクチャーで構築されているため、インフラストラクチャーの管理に時間をかける必要がありません。

AWS Glueの主な特徴は以下の通りです。

- フルマネージド型：AWS Glueは、マネージドサービスであるため、AWSがインフラストラクチャーやソフトウェアの管理を代行します。
- フレキシブル：AWS Glueは、PythonやScalaのような主要なプログラミング言語をサポートしているため、開発者は自分たちの好みに合わせてスクリプトを書くことができます。
- 高速：AWS Glueは、分散処理エンジンにApache Sparkを使用しているため、大量のデータを高速に処理することができます。

## AWS Glueの使い方

AWS Glueを使用するには、以下の手順が必要です。

1. クローラーの作成
2. ジョブの作成
3. ジョブの実行

### 1. クローラーの作成

まず、AWS Glueのクローラーを使用して、データを抽出するデータソースを設定する必要があります。クローラーは、データソースを認識し、スキーマを自動的に検出して、AWS Glueのジョブで使用することができる形式に変換します。以下は、AWS Glueコンソールでのクローラーの作成方法です。

>AWS Glueは、リージョンごとに利用できるサービスが異なるため、利用可能なリージョンを確認する必要があります。

### 2. ジョブの作成

クローラーでデータソースを設定したら、AWS Glueジョブを作成して、データを変換して別のデータストアにロードすることができます。Amazon S3、Amazon RDS、Amazon Redshift、Amazon Elasticsearch Serviceなど、AWSの主要なデータストアに直接ロードすることができます。以下は、AWS Glueコンソールでのジョブの作成方法です。

以下のサンプルコードは、クローラーで抽出したデータを、Apache Sparkを使用して変換する方法を示しています。

```python
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
    frame=DynamicFrame.fromDF(filtered_persons, glueContext, "filtered_persons"),
    connection_type="s3",
    connection_options={
        "path": "s3://mybucket/filtered_persons",
    },
    format="csv"
)
```

### 3. ジョブの実行

AWS Glueジョブを作成したら、ジョブを手動で実行することができます。また、スケジュールを設定して、定期的にジョブを実行することもできます。以下は、AWS Glueコンソールでのジョブの実行方法です。

## まとめ

AWS Glueは、異なるデータソースからデータを抽出し、変換してから、別のデータストアにロードするための完全マネージド型のETLサービスです。AWS Glueを使用することで、サーバーレスアーキテクチャーで高速なデータ処理を実現することができます。AWS Glueを使用するためには、クローラーでデータソースを設定し、ジョブを作成して、手動で実行する必要があります。AWS Glueは、データ分析において重要な役割を果たすため、ぜひ使い方を学んでみてください。

　

## AWS 関連のまとめ
https://hack-note.com/summary/aws-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

