【google】bard apiのjavascriptでの利用
google,bard,api,javascript
google-bard-api-js

こんにちは。今回は、google bardについて初心者エンジニアに向けて、apiのjavascriptでの利用方法をご紹介します。

## google bard apiのjavascriptでの利用
### google bardとは
google bardとは、googleが提供している音声合成のapiです。音声合成とは、テキストを入力すると、そのテキストを人間の話すような音声に変換することができる技術です。googleは、この技術をapi化して、開発者に提供しています。

### apiとは
apiとは、application programming interfaceの略称で、アプリケーションのプログラム（ソフトウェア）同士が情報をやり取りするためのインタフェースを提供するソフトウェアのことです。言い換えると、apiは、プログラム同士が情報を共有するためのルールです。

## google bardのapi利用方法
まずは、google developers consoleにログインし、apiキーを取得します。

1. google developers consoleにログインし、新しいプロジェクトを作成します。
2. apiを有効にします。有効にするapiは、「cloud text-to-speech api」です。
3. api keyを生成します。

これで、apiを使用する準備が整いました。

## javascriptでのapi利用方法
いよいよ、javascriptでapiを呼び出して、音声を作成する方法を見ていきましょう。まずは、必要なライブラリを読み込みます。

```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script src="https://apis.google.com/js/api.js"></script>
```

次に、google bardのapiを読み込みます。

```javascript
gapi.load('client', function() {
    gapi.client.load('texttospeech', 'v1', function() {
        console.log('texttospeach api loaded');
    });
});
```

apiを呼び出す関数を作成します。

```javascript
function getspeech(text) {
    var request = {
        input: {text: text},
        voice: {languagecode: 'en-us', ssmlgender: 'neutral'},
        audioconfig: {audioencoding: 'mp3'}
    };
    gapi.client.texttospeech.text.synthesize(request).then(function(response) {
        var audiodata = response.result.audiocontent;
        var audio = new audio('data:audio/mpeg;base64,' + audiodata);
        audio.play();
    });
}
```

このコードで、テキストを読み込んで、音声ファイルを作成し、再生することができます。

## 使えるjavascriptのライブラリ
google bardのapiを簡単に利用できるjavascriptのライブラリには、以下があります。

### google-cloud/text-to-speech
https://github.com/googleapis/nodejs-text-to-speech

このライブラリを使うと、javascriptだけでなく、node.jsでもgoogle bardのapiを利用することができます。

### react-google-bard
https://github.com/regmi-krishna/react-google-bard

このライブラリを使うと、reactアプリケーションでgoogle bardのapiを簡単に利用することができます。

## まとめ
今回は、google bardのapiをjavascriptで呼び出して、音声合成をする方法を紹介しました。apiは、プログラム同士が情報を共有するためのルールであり、googleが提供しているapiを使うことで、開発者は自由に様々なアプリケーションを作成することができます。また、googleが提供しているライブラリを利用すれば、より簡単にgoogle bardのapiを利用することができます。google bardを利用して、より人間らしい音声合成を実現するアプリケーションを作成してみてください。

　

## Google Bard 関連まとめ
https://hack-note.com/summary/google-bard-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

