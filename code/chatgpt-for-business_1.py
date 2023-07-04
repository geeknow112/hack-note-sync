# 必要なライブラリをimportする
from transformers import pipeline

# Chatbotのインスタンスを生成する
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-large", max_length=1000)

# 対話を開始する
print("ChatGPTから返答があります。終了するときは「exit」と入力してください。")

while True:
	# ユーザーからの入力を受け取る
	user_input = input("ユーザー: ")

	# 終了条件
	if user_input == "exit":
		print("ChatGPTからの返答を終了します。")
		break

	# Chatbotからの返答を表示する
	chatbot_output = chatbot(user_input)
	print("ChatGPT: " + chatbot_output[0]["generated_text"])
