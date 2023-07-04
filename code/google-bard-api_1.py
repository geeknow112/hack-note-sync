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
