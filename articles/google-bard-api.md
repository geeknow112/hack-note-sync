【基礎】google bardをapiで利用するには
google,bard,使い方
google-bard-api

こんにちは。今回は、google bardについて初心者エンジニアに向けて、apiを利用する方法について解説します。

## はじめに

google bardとは、googleが提供している自然言語処理のプラットフォームです。テキストデータを解析することで、意味や感情、カテゴリーなどの情報を取得することができます。apiを利用することで、pythonなどのプログラミング言語からも簡単に利用することができます。

しかし、初めてapiを利用する方にとっては、細かい設定や手順が複雑に感じられるかもしれません。そこで、本記事では、google bard apiを利用する手順を詳細に解説します。

### chatGPTのAPIも使いたい場合、こちらをどうぞ
https://hack-note.com/ai/chatgpt-use-api-python/

## google bard api 使い方 python

### 1. google cloud platformでプロジェクトを作成する

google bard apiを利用するためには、google cloud platformでプロジェクトを作成する必要があります。以下の手順に従って、プロジェクトを作成しましょう。

1. google cloud platformにログインします。
2. プロジェクトを作成するために、画面左上の「プロジェクトを選択」をクリックします。
3. 「新しいプロジェクト」を選択します。
4. 必要な情報を入力し、「作成」をクリックします。

### 2. apiを有効化する

プロジェクトを作成したら、apiを有効化する必要があります。

1. 「apiとサービス」→「ダッシュボード」を選択します。
2. 「apiを有効化または無効化」をクリックします。
3. 「google cloud natural language api」を検索し、クリックします。
4. apiを有効化します。

### 3. サービスアカウントキーを作成する

サービスアカウントキーを作成することで、プログラムからapiにアクセスするための認証情報を取得することができます。

1. 「apiとサービス」→「認証情報」を選択します。
2. 「+認証情報を作成」をクリックし、「サービスアカウント」を選択します。
3. 必要な情報を入力します。
4. 「役割を選択」で、自動的に追加される「natural language api」の役割を許可します。
5. 「キーを作成」をクリックし、json形式でキーをダウンロードします。

### 4. pythonからapiにアクセスする

apiへアクセスするために、pythonのリクエストライブラリを使ってhttpリクエストを送信します。以下は、pythonでapiにアクセスするためのサンプルコードです。

```python
import os
import json
import requests

# サービスアカウントキーが含まれているjsonファイルへのパスを設定
os.environ["google_application_credentials"] = "/path/to/service_account.json"

# apiにリクエストを送信するためのurlを設定
url = "https://language.googleapis.com/v1/documents:analyzesentiment"

# テキストを設定
text = "i love google bard so much!"

# リクエストデータを設定
data = {
    "document": {
        "type": "plain_text",
        "language": "en",
        "content": text
    },
    "encodingtype": "utf8"
}

# リクエストを送信し、レスポンスを取得
response = requests.post(url, json=data)

# レスポンスをjson形式に変換
response_json = json.loads(response.text)

# sentimentの値を取得
sentiment_score = response_json["documentsentiment"]["score"]

# 結果を表示
print("sentiment score: {}".format(sentiment_score))
```

このサンプルコードでは、apiにテキストを送信して感情分析結果を取得し、その結果をコンソールに表示する方法を示しています。具体的には、「i love google bard so much!」というテキストをapiに送信し、その結果の感情値を表示しています。

>apiを利用する際は、適切な認証情報を設定することが重要です。サービスアカウントキーは誰でもアクセスできない場所に保管しましょう。

### まとめ

google bard apiを利用するには、google cloud platformでプロジェクトを作成し、apiを有効化して、サービスアカウントキーを作成します。pythonからapiにアクセスする場合は、httpリクエストを利用して情報を取得することができます。

## AIでスキルを強化
bardやchatGPTを使ってて思うのは、まだ仕事が奪われる段階ではないってことです。
むしろAIを使ってスキルを強化していけるという思いが強くなりました。
今まで手間だった簡単なプログラミングはAIに任せて、
より高度なものをやったり、ディレクションしたりが、人間の仕事になると思います。

AIでいかに単純作業を効率化していけるかが技術力の分岐点になるので、
今のうちに基礎固めにプログラミングスクールを使ってみるのもありだと思います。
参考に載せておきます。
https://hack-note.com/programming-schools/#toc13

## 初心者エンジニアを脱出するには下記もおススメです
- [TechAcademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3A%2F%2Ftechacademy.jp%2Fhtmlcss-trial%3Futm_source%3Dmoshimo%26utm_medium%3Daffiliate%26utm_campaign%3Dtextad)
- [オンラインスクール DMM WEBCAMP PRO](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=ON)

参考記事：
- [google cloud platform上で自然言語処理を実行する](https://cloud.google.com/natural-language/docs/quickstart-client-libraries?hl=ja)
- [pythonでgoogle natural language apiを使って文章の感情分析してみた](https://qiita.com/xkumiyu/items/c9c3f5387ba716b59077)
