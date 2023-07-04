import openai

# プロンプトを設定
prompt = "Hello, how are you today?"

# パラメータを設定
parameters = {
	"model": "text-davinci-002",
	"prompt": prompt,
	"temperature": 0.5,
	"max_tokens": 50,
	"n": 1,
	"stop": "\n"
}

# APIを呼び出し
response = openai.Completion.create(**parameters)

# 結果を出力
print(response.choices[0].text)
