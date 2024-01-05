【aws cli】dynamodbテーブルの作成とクエリ
aws,cli
aws_cli_dynamodb

こんにちは。今回は、aws cliについて初心者エンジニアに向けて、dynamodbテーブルの作成とクエリについて解説します。

## aws cliを使用したdynamodbテーブルの作成手順

まずは、aws cliを使用してdynamodbテーブルを作成する手順を紹介します。

1. dynamodbテーブルの作成コマンドを実行します。
```bash
aws dynamodb create-table \
  --table-name mytable \
  --attribute-definitions \
    attributename=id,attributetype=s \
    attributename=timestamp,attributetype=n \
  --key-schema \
    attributename=id,keytype=hash \
    attributename=timestamp,keytype=range \
  --provisioned-throughput \
    readcapacityunits=5,writecapacityunits=5
```
2. dynamodbテーブルの作成が成功した場合、以下のようなレスポンスが返されます。
```
{
    "tabledescription": {
        "tablename": "mytable",
        "tablestatus": "creating",
        ...
    }
}
```

以上で、dynamodbテーブルの作成手順は完了です。

- 参考ブログ記事1: [aws公式ドキュメント - creating tables with the aws cli](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/create-table.html)

## dynamodbテーブルの属性とキーの設定方法

次に、dynamodbテーブルの属性とキーの設定方法について解説します。

- **属性の設定**
dynamodbテーブルの属性は、`--attribute-definitions`オプションを使用して定義します。
```bash
aws dynamodb create-table \
  --table-name mytable \
  --attribute-definitions \
    attributename=id,attributetype=s \
    attributename=timestamp,attributetype=n \
...
```

- **キーの設定**
dynamodbテーブルのキーは、`--key-schema`オプションを使用して定義します。
```bash
aws dynamodb create-table \
  --table-name mytable \
  --key-schema \
    attributename=id,keytype=hash \
    attributename=timestamp,keytype=range \
...
```

- 参考ブログ記事2: [aws advent calendar 2017 - aws cliでdynamodbを使う時の基礎](https://qiita.com/retoruto_carry/items/2067d7d3f2d062ef9afe)

## aws cliでのdynamodbテーブルへのデータの挿入と更新

aws cliを使用してdynamodbテーブルへのデータの挿入と更新方法を解説します。

- **データの挿入**
dynamodbテーブルにデータを挿入するには、`put-item`コマンドを使用します。
```bash
aws dynamodb put-item \
  --table-name mytable \
  --item '{
    "id": {"s": "123"},
    "timestamp": {"n": "1609459200"},
    "title": {"s": "hello world"},
    "content": {"s": "this is a sample blog post"}
}'
```

- **データの更新**
dynamodbテーブルのデータを更新するには、`update-item`コマンドを使用します。
```bash
aws dynamodb update-item \
  --table-name mytable \
  --key '{
    "id": {"s": "123"},
    "timestamp": {"n": "1609459200"}
}' \
  --update-expression 'set content = :content' \
  --expression-attribute-values '{":content":{"s":"updated content"}}'
```

- 参考ブログ記事3: [scalable web architecture and distributed systems - dynamodb and aws cli: a story of two friends](http://www.tagwith.com/question_488606_dynamodb-and-aws-cli-a-story-of-two-friends/)

## dynamodbテーブルのスキャンとクエリの基本的な使い方

dynamodbテーブルのスキャンとクエリの基本的な使い方を解説します。

- **テーブルのスキャン**
テーブル全体をスキャンするには、`scan`コマンドを使用します。
```bash
aws dynamodb scan \
  --table-name mytable
```

- **クエリの実行**
クエリを実行するには、`query`コマンドを使用します。
```bash
aws dynamodb query \
  --table-name mytable \
  --key-condition-expression 'id = :id' \
  --expression-attribute-values '{":id":{"s":"123"}}'
```

- 参考ブログ記事4: [aws公式ドキュメント - querying tables with the aws cli](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/query.html)

## aws cliを使ったdynamodbテーブルのインデックスとパーティションキーの設定

最後に、aws cliを使用してdynamodbテーブルのインデックスとパーティションキーを設定する方法を解説します。

- **グローバルセカンダリインデックスの追加**
グローバルセカンダリインデックスを追加するには、`update-table`コマンドを使用します。
```bash
aws dynamodb update-table \
  --table-name mytable \
  --attribute-definitions \
    attributename=category,attributetype=s \
  --global-secondary-index-updates \
    '[{
      "create": {
        "indexname": "categoryindex",
        "keyschema": [
          {"attributename": "category","keytype": "hash"}
        ],
        "projection": {
          "projectiontype": "all"
        },
        "provisionedthroughput": {
          "readcapacityunits": 5,
          "writecapacityunits": 5
        }
      }
    }]'
```

- **ローカルセカンダリインデックスの追加**
ローカルセカンダリインデックスを追加するには、`update-table`コマンドを使用します。
```bash
aws dynamodb update-table \
  --table-name mytable \
  --attribute-definitions \
    attributename=userid,attributetype=n \
    attributename=timestamp,attributetype=n \
  --local-secondary-index-updates \
    '[{
      "create": {
        "indexname": "useridindex",
        "keyschema": [
          {"attributename": "id","keytype": "hash"},
          {"attributename": "timestamp","keytype": "range"}
        ],
        "projection": {
          "projectiontype": "all"
        }
      }
    }]'
```

以上で、dynamodbテーブルのインデックスとパーティションキーの設定方法の解説は完了です。

- 参考ブログ記事5: [aws公式ドキュメント - global secondary indexes with the aws cli](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/update-table.html#options-for-creating-or-removing-a-global-secondary-index)

以上で、aws cliを使用したdynamodbテーブルの作成とクエリについての解説を終わります。初心者エンジニアの皆さんが、aws cliを使ってdynamodbを効果的に活用できるようになることを願っています。

　

## 【aws cli】関連のまとめ
https://hack-note.com/summary/aws-cli-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

