【amazon connect】機能解説: ビジネスの効率化と改善に使える
amazon,connect
aws-connect-feature-overview

## amazon connect機能解説: ビジネスの効率化と改善に使える

こんにちは。今回は、amazon connectについて初心者エンジニアに向けて、その機能や使い方について解説します。amazon connectは、クラウドベースのコンタクトセンターサービスであり、ビジネスの効率化と改善を実現するための機能が豊富に備わっています。この記事では、amazon connectの主要な機能やその活用方法について詳しく説明します。

### ivr自動応答機能の使い方

ivr（interactive voice response）自動応答機能は、顧客との通話において自動的に応答する機能です。この機能を使うことで、顧客が特定の番号を押すことで特定のメニューや情報にアクセスしたり、必要な情報を入力して問い合わせ内容を事前に捉えることができます。以下に、pythonを使ってivr自動応答機能を実装するサンプルコードを示します。

```python
import boto3

connect = boto3.client('connect')

def lambda_handler(event, context):
    # ハンドリングするメニューオプションを定義する
    options = [
        {
            'name': '1',
            'description': '商品についてのお問い合わせ',
            'type': 'incoming_number',
            'number': '000-1111-2222'
        },
        {
            'name': '2',
            'description': '注文のキャンセルについてのお問い合わせ',
            'type': 'incoming_number',
            'number': '000-3333-4444'
        }
    ]

    # ivrレジュームステータスを作成する
    response = connect.create_contact_flow(
        instanceid='instance_id',
        name='ivr_resume_status',
        type='contact_flow',
        content=json.dumps({
            'version': '1.0',
            'startaction': 'disconnect',
            'metadata': {},
            'definition': {
                'start': {
                    'type': 'sendtasksuccess',
                    'next': 'menu'
                },
                'menu': {
                    'type': 'parallel',
                    'branches': [
                        {
                            'start': 'menuoption1',
                            'conditions': {
                                'variable': '$.option',
                                'values': ['1']
                            }
                        },
                        {
                            'start': 'menuoption2',
                            'conditions': {
                                'variable': '$.option',
                                'values': ['2']
                            }
                        }
                    ]
                },
                'menuoption1': {
                    'type': 'getcustomerinput',
                    'parameters': {
                        'type': 'dtmf',
                        'dtmfdigits': '1',
                        'dtmfinputtimermilliseconds': '10000',
                        'dtmffinishtimermilliseconds': '10000',
                        'dtmfattempts': '3',
                        'dtmffallbackflow': 'ivr_resume_status'
                    },
                    'next': 'transfer'
                },
                'menuoption2': {
                    'type': 'getcustomerinput',
                    'parameters': {
                        'type': 'dtmf',
                        'dtmfdigits': '2',
                        'dtmfinputtimermilliseconds': '10000',
                        'dtmffinishtimermilliseconds': '10000',
                        'dtmfattempts': '3',
                        'dtmffallbackflow': 'ivr_resume_status'
                    },
                    'next': 'transfer'
                },
                'transfer': {
                    'type': 'transfertophonenumber',
                    'parameters': {
                        'phonenumber': json.dumps(options)
                    },
                    'end': true
                }
            }
        })
    )

    return response
```

### キュー機能の活用方法

キュー機能は、連絡先を効率的に処理するための機能です。この機能を使用することで、異なる種類の問い合わせや要望を受け付けるためのキューを作成し、エージェントに効率的に割り当てることができます。以下に、pythonを使ってキュー機能を活用するサンプルコードを示します。

```python
import boto3
import json

connect = boto3.client('connect')

def lambda_handler(event, context):
    # キューを作成する
    response = connect.create_queue(
        instanceid='instance_id',
        name='myqueue',
        hoursofoperationid='hours_of_operation_id',
        maxcontacts=10,
        quickconnectids=[
            'quick_connect_id'
        ],
        description='my queue'
    )

    return response
```

### レポートの見方と分析手順

amazon connectでは、コンタクトセンターのパフォーマンスやエージェントの活動に関するレポートを利用することができます。この機能を使用することで、コンタクトの状態や応答時間、通話時間などのデータを分析し、ビジネスの改善や効率化に役立てることができます。以下に、レポートの見方と分析手順を説明します。

1. ダッシュボードにアクセスします。
2. レポートセクションを選択します。
3. 必要なレポートを選択します（例：通話時間レポート）。
4. 必要なフィルタリングと期間を設定します。
5. レポートデータをグラフや表で表示して分析します。
6. 分析結果を元に改善点や効率化のための施策を立案します。

### エージェントのスキルと状態設定

amazon connectでは、エージェントのスキルと状態を設定することができます。これにより、特定のスキルを持つエージェントに対応してもらうことや、エージェントの状態を管理することができます。以下に、pythonを使ってエージェントのスキルと状態設定を行うサンプルコードを示します。

```python
import boto3
import json

connect = boto3.client('connect')

def lambda_handler(event, context):
    # スキルを作成する
    response = connect.create_skill(
        instanceid='instance_id',
        skilltype='queue',
        skillname='myskill',
        queuereference={
            'queueid': 'queue_id'
        },
        description='my skill'
    )

    # エージェントの状態を設定する
    response = connect.update_user_routing_profile(
        userid='user_id',
        instanceid='instance_id',
        routingprofileid='routing_profile_id',
        userroutingprofile={
            'queueid': 'queue_id'
        }
    )

    return response
```

### コンタクトフローの設計手順

コンタクトフローは、amazon connectでのコールフローを設計するためのグラフィカルなツールです。このツールを使用することで、コールルーティング、音声の録音、認証、タスクの割り当てなど、さまざまな機能を組み合わせて柔軟なコールフローを作成することができます。以下に、コンタクトフローの設計手順を説明します。

1. amazon connectコンソールにアクセスします。
2. コンタクトフローコンソールを選択します。
3. 新しいコンタクトフローを作成します。
4. コンタクトフローのスタートを設定します。
5. 必要なアクションやブロックを追加し、接続します。
6. アクションやブロックの設定を編集します（例：音声を再生するアクション）。
7. コンタクトフローのテストを行います。
8. 必要に応じてコンタクトフローを公開します。

### amazon connect cti adapterの導入手順

amazon connect cti adapterは、amazon connectと外部システム（例：カスタマーリレーションシップ管理）を連携するためのアダプタです。このアダプタを使用することで、通話情報やタスク情報を外部システムに取り込むことができます。以下に、cti adapterの導入手順を説明します。

1. cti adapterをダウンロードします。
2. cti adapterを適切なディレクトリに展開します。
3. cti adapterの設定ファイルを編集し、必要な情報を入力します（例：amazon connectのインスタンスid）。
4. cti adapterを起動します。
5. amazon connectコンソールにアクセスし、ctiインテグレーションを作成します。
6. 必要な設定を入力します（例：ホスト名、ポート番号）。
7. コンタクトフロー内でctiインテグレーションを使用する設定を行います。
8. cti adapterと外部システムの連携が正しく動作していることを確認します。

これらの機能や手順を活用することで、amazon connectをより効果的に利用することができます。初心者エンジニアにとっても、これらの機能を学ぶことはビジネスの効率化と改善につながる重要なスキルとなるでしょう。

参考ブログ記事：
- [amazon connect ドキュメント](https://docs.aws.amazon.com/connect/index.html)
- [awsコンタクトセンターサービス「amazon connect」の機能と価格](https://www.misoca.jp/tech/insight/aws-amazon-connect-function-price.html)

　

## 【Amazon Connect】まとめ
https://hack-note.com/summary/aws-connect-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

