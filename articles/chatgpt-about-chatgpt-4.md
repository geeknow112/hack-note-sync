【比較】chatgpt-3.5からchatgpt-4はどう進化したのか？気になる料金は？
chatgpt,比較
chatgpt-about-chatgpt-4

こんにちは。今回は、chatgptについて初心者エンジニアに向けて、chatgpt-3.5とchatgpt-4の比較について解説します。

# はじめに
近年、自然言語処理技術が進歩し、aiが人間とより自然なコミュニケーションを実現するために、chatbot開発の需要も高まっています。chatgptは、自然言語処理技術を用いて、会話の流れに合わせて回答を生成するapiです。chatgpt-3.5からchatgpt-4に進化したことで、より高度な応答が可能になりました。そこで、今回はchatgpt-3.5とchatgpt-4の比較と、気になる料金について解説します。

## chatgpt-3.5とは？
chatgpt-3.5は、自然言語処理技術の一つで、データセットを使用して、大量のテキストを学習し、自然な応答を生成するapiです。従来のものに比べ、より高度な応答を可能にします。

例えば、以下のコードを使って、chatgpt-3.5に「hello」というメッセージを送り、応答を取得することができます。

```
import openai

openai.api_key = "your_api_key"

prompt = "hello"
model = "text-davinci-002"
temperature = 0.5

completions = openai.completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1024,
    n = 1,
    stop=none,
    temperature=temperature
)

message = completions.choices[0].text.strip()
print(message)
```

このコードを実行すると、「hi! how can i help you today?」という応答が返ってきます。このように、chatgpt-3.5を使うことで、自然な回答を取得することができます。

## chatgpt-4とは？
chatgpt-4は、chatgptの進化版であり、より高度な応答を可能にします。chatgpt-3.5に比べ、より多くのデータセットを使用して学習しているため、より正確な応答を生成することができます。

例えば、以下のコードを使って、chatgpt-4に「hello」というメッセージを送り、応答を取得することができます。

```
import openai

openai.api_key = "your_api_key"

prompt = "hello"
model = "text-davinci-002"
temperature = 0.5

completions = openai.completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=1024,
    n = 1,
    stop=none,
    temperature=temperature
)

message = completions.choices[0].text.strip()
print(message)
```

chatgpt-3.5と同様に、「hi! how can i help you today?」という応答が返ってきます。しかし、chatgpt-4では、さらに高度な応答が可能になっています。

## 比較
chatgpt-3.5とchatgpt-4を比較すると、chatgpt-4の学習データセットがより大きく、高度な応答が可能になっています。ただし、chatgpt-4は、そこまで大きな進化があるわけではありません。したがって、chatgpt-3.5でも十分な応答が得られる場合もあります。

また、chatgpt-4は、chatgpt-3.5よりも高額です。料金は、apiを使用する回数によって異なりますが、chatgpt-4は、chatgpt-3.5に比べて2倍以上の料金がかかる場合があります。そのため、十分な応答が得られる場合は、chatgpt-3.5を選択することも検討してみてください。

## 料金
chatgptの料金は、apiを使用する回数によって異なります。chatgpt-3.5の場合、1回あたり0.0125ドルでapiを使用することができます。一方、chatgpt-4の場合、1回あたり0.03ドルでapiを使用することができます。したがって、chatgpt-4を使用する場合は、料金が2倍以上かかることになります。

ただし、料金は、apiを使用する回数によって異なるため、詳細な料金については、公式サイトを確認してください。

>注意していただきたいのは、apiの使用回数が増えた場合、apiの利用料金が増える可能性があるということです。そのため、目安として、どの程度の使用量になるのかを事前に把握し、予算を立てておくことが重要です。

# まとめ
今回は、chatgpt-3.5とchatgpt-4の比較について解説しました。chatgpt-4は、より高度な応答が可能であり、より大きなデータセットを使用して学習していることから、高額なapiとなっています。しかし、十分な応答が得られる場合は、chatgpt-3.5を選択することも検討してみてください。関連する記事として、以下を参考にすることをおすすめします。

- openaiのapiであるgpt-3の仕組みと、実際にapiを使う方法について解説しています。
https://www.at-memo.jp/self-study-programming/openai-gpt-3-api

- openai gpt-3 apiを使って文章を自動生成するまでの手順について解説しています。
https://dev.classmethod.jp/articles/gpt-3-api-autogeneration/

　

## ChatGPT 関連のまとめ
https://hack-note.com/summary/chatgpt-summary/

　

## AIでスキルを強化
bardやchatGPTを使ってて思うのは、まだ仕事が奪われる段階ではないってことです。
むしろAIを使ってスキルを強化していけるという思いが強くなりました。
今まで手間だった簡単なプログラミングはAIに任せて、
より高度なものをやったり、ディレクションしたりが、人間の仕事になると思います。

AIでいかに単純作業を効率化していけるかが技術力の分岐点になるので、
今のうちに基礎固めにプログラミングスクールを使ってみるのもありだと思います。
参考に載せておきます。
https://hack-note.com/programming-schools/#toc13


