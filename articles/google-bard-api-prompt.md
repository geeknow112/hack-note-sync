【google】bard apiに最適なプロンプト
google,bard,api,prompt
google-bard-api-prompt

こんにちは。今回は、google bardについて初心者エンジニアに向けて、bard apiに最適なプロンプトについてお話します。

google bardは、自然言語処理に特化したai技術の1つであり、雑談apiから質問応答まで様々な応用が可能です。その中でも、bard apiは、言語理解能力やコンピュータとの対話性に優れ、最新のニューラルネットワーク技術を採用しているため、高精度で自然な会話を実現しています。本稿では、bard apiを利用するために必要なプロンプトについて解説します。

## google bardでのプロンプトについて

bard apiのプロンプトは、利用者がaiに対して質問を投げる際に、「何を聞きたいのか」という情報を与えるものです。プロンプトによって、aiの出力が大きく変化するため、適切なプロンプトを設定することはaiを制御する上で非常に重要です。

具体的には、bard apiは、以下のようなプロンプトを受け取ります。

- prompt（必須）：aiに入力する文章を指定します。短い単語から長い文章まで様々なテキストを入力できます。
- max_tokens（任意）：aiから出力する文章の最大長を指定します。
- temperature（任意）：aiの生成する文章の多様性や個性を指定します。
- top_p（任意）：aiが生成する文章の選択範囲を指定します。

## 最適な解答を得るためのプロンプト

aiとの対話で重要なのは、適切なプロンプトを設定することです。aiを利用する上で、主に以下の2つのポイントに注目する必要があります。

### ・プロンプトの短めの指定

まず、aiにどのようなことを聞きたいのかを明確に伝えることが大切です。しかし、長すぎるプロンプトは、aiが意図を理解しにくくなるため、短めに指定するようにしましょう。

例えば、以下のような書き方が好ましいと言えます。

「fashionについて、最近の流行は何ですか？」

これは、aiに対して「fashionについて流行について教えて欲しい」という明確な意図を伝えつつ、過剰な情報を節約しています。

### ・前処理によるプロンプト精度の向上

次に、プロンプトに前処理を施して、aiが処理できる形式に変換する必要があります。前処理は、単純なテキストのトークン化や、特定のトークンに対して意味的な情報を与えることができます。例えば、以下のような前処理があります。

- 数字の除去
- 名詞の抽出
- 名詞の重み付け
- 同義語の置き換え

これら前処理を施すことで、より正確なプロンプトを作成し、aiの精度を向上させることができます。

## chatgptとgoogle bardのプロンプトの差

同じ自然言語処理を行うaiでも、プロンプトを変えることで、大きな違いが出ることがあります。それを例えるために、chatgptとgoogle bardで、同じトピック「天気予報について」に対して同じ問い合わせ「今日の天気は？」をしてみましょう。

### ・chatgptの設定

- prompt：今日の天気は？

chatgptは、シンプルなプロンプトであるため、短めである反面、回答が暴走する恐れがあります。

### ・google bardの設定

- prompt：今日の天気は？
- max_tokens：10
- temperature：0.5
- top_p：1.0

google bardでは、プロンプトでの情報の調整が可能であるため、回答も正確かつシンプルなものとなります。

## まとめ

bard apiを適切に利用するためには、最適なプロンプトを設定することが重要です。プロンプトの正確性により、aiの出力が大きく変化することが理解できたと思います。具体的には、プロンプトの短めの指定や前処理を施すことで、より正確で高品質なaiの出力を得ることができます。今後も、aiの進化と共に、より精度の高いプロンプトを作成するために常に学習し、実践していきましょう。

参考url：
- https://cloud.google.com/blog/ja/products/ai-machine-learning/introducing-google-researchs-open-domain-dialogue-system-replika
- https://towardsdatascience.com/creating-a-qa-chatbot-with-google-bert-and-tensorflow-2-0-5668e83d9316

　

## Google Bard 関連まとめ
https://hack-note.com/summary/google-bard-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

