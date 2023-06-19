【google】bard apiとgasを使ったseoに強い文章作成自動化の手法
google,bard,api,gas
google-bard-api-gas

こんにちは。今回は、google bardについて初心者エンジニアに向けて、bard apiを使ったseoに強い文章作成自動化の手法について解説します。

最近、seo（search engine optimization）を意識するwebサイトが増えてきました。seoとは、検索エンジンにおいて、検索結果の上位に表示されるための対策のことです。その中でも、コンテンツの質を高めることがとても重要になっています。

ここで紹介するのが、googleから提供されている文章作成自動化ツール「google bard」。文章作成自動化によって、効率的かつ効果的なseo対策を行うことができます。今回は、そのgoogle bard apiとgasを使ったseoに強い文章作成自動化の手法について紹介します。

### google bardのapi利用方法
まず、google bard apiを利用するには、google cloud platformに登録してapiキーを取得する必要があります。apiキーを取得したら、以下のようなプロジェクトを作成し、bard apiを有効化します。

``` python
import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

print(secrets)
```

apiキーを取得後、pythonなどのプログラミング言語を使用して、apiを呼び出すことができます。以下はpythonでbard apiを呼び出す例です。

``` python
import openai
openai.api_key = "api_key"

prompt = "please explain bard api."
model = "text-davinci-002"
response = openai.completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=50
)

print(response["choices"][0]["text"])
```

### gas(google action script)でのapi利用方法
上記のpythonのコードだと、apiを呼び出す際に手動で実行する必要があります。しかし、gasでbard apiを呼び出すことで、自動化することができます。gasとは、googleの提供するスクリプトエディターで、googleのサービスと連携して自動化することができる言語です。

gasでbard apiを呼び出すには、以下のようなコードを書きます。

``` javascript
function generatetext(prompt, model, apikey) {
  var response = urlfetchapp.fetch("https://api.openai.com/v1/engines/" + model + "/completions", {
    headers: {
      'content-type': 'application/json',
      'authorization': 'bearer ' + apikey,
    },
    method: 'post',
    payload: json.stringify({
      prompt: prompt,
      max_tokens: 50,
    })
  });
  var json = json.parse(response.getcontenttext());
  var choices = json.choices[0].text;
  return choices;
}
```

このコードでは、bard apiのエンジン、プロンプト、apiキーを指定し、50トークンまでのテキストを生成するように指定しています。

### gasでgoogle bardを呼び出す
ここでは、gasでbard apiを呼び出し、スプレッドシートに自動的に文章を生成する方法を紹介します。下記のコードをgasに書き込みます。

``` javascript
function main() {
  var ss = spreadsheetapp.getactivespreadsheet();
  var sheet = ss.getsheetbyname("sheet1");
  var lastrow = sheet.getlastrow();
  var promptrange = sheet.getrange(lastrow, 1);
  var modelrange = sheet.getrange(lastrow, 2);
  var apikeyrange = sheet.getrange(lastrow, 3);
  var outputrange = sheet.getrange(lastrow, 4);
  
  var prompt = promptrange.getvalue();
  var model = modelrange.getvalue();
  var apikey = apikeyrange.getvalue();
  
  var output = generatetext(prompt, model, apikey);
  outputrange.setvalue(output);
}
```

上記コードでは、スプレッドシートの「sheet1」に格納されたプロンプト、エンジン、apiキーを取得し、`generatetext`関数を呼び出し、その結果をスプレッドシートに出力するように指定しています。

### googleのseoを意識したbardのプロンプト
最後に、googleのseoを意識したbardのプロンプトの書き方を紹介します。seoには、検索エンジンに表示された際、クリックされる可能性を高めるタイトルや、目的を表現するメタデータの設定が重要です。そのため、bardのプロンプトによって、効果的なseo対策を行うことができます。

bardのプロンプトの書き方の例を以下に示します。

「googleのseoに強い文章を生成しましょう。以下のキーワードを含めて、150ワードの文を作成してください。google、bard、api、gas。この文には、google検索の上位表示を目指した情報を含めてください。」

このように、プロンプトの中にseoに必要なキーワードや文字数、目指す検索結果を明確にし、効果的な文章を生成することができます。

## まとめ
今回は、google bardについて初心者エンジニア向けに、bard apiとgasを使ったseoに強い文章作成自動化の手法について解説しました。これらの手法を活用することにより、簡単かつ効率的なseo対策を実現することができます。是非、実践してみてください。

参考記事：
- [openai api documentation](https://beta.openai.com/docs/api-reference/introduction)
- [google apps script document](https://developers.google.com/apps-script)
- [google sheets api document](https://developers.google.com/sheets/api)


## google bard 関連のまとめ
https://hack-note.com/tools/google-bard-summary/


## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/


## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

