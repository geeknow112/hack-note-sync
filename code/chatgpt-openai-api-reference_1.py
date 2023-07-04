import openai
openai.api_key = "YOUR_API_KEY"

# リクエストの送信
response = openai.Completion.create(
	engine="davinci",
	prompt="Hello,",
	max_tokens=5
)

# 結果の出力
print(response.choices[0].text)
