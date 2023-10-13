【javascript】最新のニュースを取得！rssリーダーの作り方
javascript,rss
js_rss_reader_creation

## プロジェクトのセットアップと環境構築

こんにちは。今回は、javascriptについて初心者エンジニアに向けて、最新のニュースを取得するためのrssリーダーの作り方についてご紹介します。

rss（rich site summary）は、ウェブサイトの最新の記事や情報をまとめたフィード形式のデータです。rssリーダーは、これらのフィードを取得し、最新の情報を一括で表示する便利なツールです。

この記事では、javascriptを使用してrssリーダーを作成する方法を解説します。まずは、プロジェクトのセットアップと環境構築から始めましょう。

### プロジェクトの作成
まずは、新しいディレクトリを作成し、プロジェクトを初期化します。ターミナルを開き、以下のコマンドを実行してください。

```
mkdir rss-reader
cd rss-reader
npm init -y
```

これにより、rss-readerという名前のディレクトリが作成され、package.jsonファイルが自動的に初期化されます。

### 必要なパッケージのインストール
rssリーダーを作成するためには、いくつかのパッケージをインストールする必要があります。以下のコマンドを実行して、必要なパッケージをインストールしましょう。

```
npm install axios
npm install xml2json
```

axiosは、httpリクエストを簡単に行うためのパッケージです。xml2jsonは、xmlデータをjson形式に変換するためのパッケージです。

### ファイルの作成と準備
rss-readerディレクトリ内に、index.htmlとscript.jsという2つのファイルを作成しましょう。

index.htmlファイルの内容は以下の通りです。

```html
<!doctype html>
<html>
<head>
  <title>rss reader</title>
</head>
<body>

  <h1>最新のニュース</h1>
  <ul id="news-list"></ul>

  <script src="script.js"></script>
</body>
</html>
```

script.jsファイルの内容は以下の通りです。

```javascript
window.addeventlistener('domcontentloaded', () => {
  // todo: ニュースの取得と表示
});
```

これで、プロジェクトのセットアップと環境構築は完了しました。

## rssフィードのurl取得と選択

次に、rssフィードのurlを取得し、取得したurlを基にフィードを選択する方法について説明します。

### rssフィードのurl取得
rssフィードのurlは、各ウェブサイトのフィードページやブログページで見つけることができます。以下のような特徴的なアイコンやリンクを探してください。

![rssフィードのアイコン](https://example.com/rss_icon.png)

または

```
<link rel="alternate" type="application/rss+xml" title="rss" href="https://example.com/rss.xml">
```

例えば、以下のブログの場合、フィードのurlは`\`となります。

- [サンプルブログ1](https://example.com/blog1)
- [サンプルブログ2](https://example.com/blog2)

取得したurlは、script.jsファイルに追記していきましょう。

```javascript
window.addeventlistener('domcontentloaded', () => {
  const feedurl = 'https://example.com/rss.xml';

  // todo: ニュースの取得と表示
});
```

### フィードの選択
複数のrssフィードがある場合、ユーザーが表示するフィードを選択できるようにすることもできます。例えば、以下のようなセレクトボックスを作成しましょう。

```html
<select id="feed-selector">
  <option value="https://example.com/feed1.xml">フィード1</option>
  <option value="https://example.com/feed2.xml">フィード2</option>
  <option value="https://example.com/feed3.xml">フィード3</option>
</select>
```

ユーザーがフィードを選択した後、選択されたurlを取得して、それを基にニュースを取得しましょう。

```javascript
window.addeventlistener('domcontentloaded', () => {
  const feedselector = document.getelementbyid('feed-selector');
  const feedurl = feedselector.value;

  feedselector.addeventlistener('change', () => {
    feedurl = feedselector.value;
    // todo: ニュースの取得と表示
  });

  // todo: ニュースの取得と表示
});
```

これで、rssフィードのurl取得と選択の方法について理解しました。

## フィードの読み込みとデータの取得

次に、取得したフィードを読み込み、データを取得する方法について説明します。

### フィードの読み込み
フィードの読み込みには、axiosパッケージを使用します。以下のコードをscript.jsファイルに追記して、フィードを読み込みましょう。

```javascript
window.addeventlistener('domcontentloaded', () => {
  const feedselector = document.getelementbyid('feed-selector');
  let feedurl = feedselector.value;

  feedselector.addeventlistener('change', () => {
    feedurl = feedselector.value;
    loadfeed(feedurl);
  });

  loadfeed(feedurl);
});

function loadfeed(url) {
  axios.get(url)
    .then(response => {
      const data = response.data;
      // todo: データの取得と表示
    })
    .catch(error => {
      console.error(error);
    });
}
```

### データの取得
フィードのデータを取得するためには、xml2jsonパッケージを使用してxml形式のデータをjson形式に変換する必要があります。以下のコードを追加して、データを取得しましょう。

```javascript
function loadfeed(url) {
  axios.get(url)
    .then(response => {
      const xmldata = response.data;
      const jsondata = xml2json.tojson(xmldata);
      const feeddata = json.parse(jsondata);
      const items = feeddata.rss.channel.item;
      // todo: データの表示
    })
    .catch(error => {
      console.error(error);
    });
}
```

以上で、フィードの読み込みとデータの取得の方法について説明しました。

## ニュース記事の表示とデザインのカスタマイズ

次に、取得したニュース記事を表示し、デザインをカスタマイズする方法について説明します。

### ニュース記事の表示
取得したニュース記事を表示するために、html要素を動的に生成しましょう。以下のコードを追加して、ニュース記事を表示しましょう。

```javascript
function loadfeed(url) {
  axios.get(url)
    .then(response => {
      const xmldata = response.data;
      const jsondata = xml2json.tojson(xmldata);
      const feeddata = json.parse(jsondata);
      const items = feeddata.rss.channel.item;
      
      const newslist = document.getelementbyid('news-list');
      newslist.innerhtml = '';

      items.foreach(item => {
        const title = item.title;
        const link = item.link;
        const description = item.description;

        const listitem = document.createelement('li');
        const linkelement = document.createelement('a');
        linkelement.href = link;
        linkelement.textcontent = title;
        listitem.appendchild(linkelement);

        const descriptionelement = document.createelement('p');
        descriptionelement.textcontent = description;
        listitem.appendchild(descriptionelement);

        newslist.appendchild(listitem);
      });
    })
    .catch(error => {
      console.error(error);
    });
}
```

### デザインのカスタマイズ
表示されるニュース記事のデザインをカスタマイズすることもできます。cssを使用して、デザインを調整しましょう。以下のコードをindex.htmlファイルのheadタグ内に追記して、デザインをカスタマイズしましょう。

```html
<style>
  h1 {
    color: #333;
    font-size: 24px;
    margin-bottom: 20px;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    margin-bottom: 10px;
  }

  a {
    color: #555;
    text-decoration: none;
    font-weight: 600;
  }

  p {
    color: #777;
  }
</style>
```

これで、ニュース記事の表示とデザインのカスタマイズの方法について説明しました。

## リンク先の読み込みと記事の詳細表示機能

最後に、リンク先の読み込みと記事の詳細表示機能を実装しましょう。

### リンク先の読み込み
リンク先の読み込みには、fetch apiを使用します。以下のコードを追加して、リンク先のページを読み込みましょう。

```javascript
function loadfeed(url) {
  axios.get(url)
    .then(response => {
      const xmldata = response.data;
      const jsondata = xml2json.tojson(xmldata);
      const feeddata = json.parse(jsondata);
      const items = feeddata.rss.channel.item;
      
      const newslist = document.getelementbyid('news-list');
      newslist.innerhtml = '';

      items.foreach(item => {
        const title = item.title;
        const link = item.link;
        const description = item.description;

        const listitem = document.createelement('li');
        const linkelement = document.createelement('a');
        linkelement.href = link;
        linkelement.textcontent = title;
        listitem.appendchild(linkelement);

        const descriptionelement = document.createelement('p');
        descriptionelement.textcontent = description;
        listitem.appendchild(descriptionelement);

        newslist.appendchild(listitem);
        
        // リンク先の読み込み
        fetch(link)
          .then(response => response.text())
          .then(data => {
            const parser = new domparser();
            const htmldoc = parser.parsefromstring(data, 'text/html');
            const articlecontent = htmldoc.queryselector('.article-content');

            listitem.addeventlistener('click', () => {
              showarticle(articlecontent.innerhtml);
            });
          });
      });
    })
    .catch(error => {
      console.error(error);
    });
}
```

### 記事の詳細表示機能
記事の詳細表示機能を実装するために、詳細表示用のダイアログを作成しましょう。以下のコードを追加して、詳細表示機能を実装しましょう。

```javascript
function showarticle(content) {
  const dialog = document.createelement('dialog');
  dialog.innerhtml = `
    <button id="close-button">閉じる</button>
    <div>${content}</div>
  `;

  document.body.appendchild(dialog);

  const closebutton = document.getelementbyid('close-button');

  closebutton.addeventlistener('click', () => {
    dialog.remove();
  });

  dialog.showmodal();
}
```

これで、リンク先の読み込みと記事の詳細表示機能が実装されました。

以上で、javascriptについて初心者エンジニア向けのrssリーダーの作り方をご紹介しました。プロジェクトのセットアップと環境構築、rssフィードのurl取得と選択、フィードの読み込みとデータの取得、ニュース記事の表示とデザインのカスタマイズ、リンク先の読み込みと記事の詳細表示機能について説明しました。是非、実際に手を動かしてrssリーダーを作成してみてください。

参考記事：
- [javascriptでrssをパースする方法](https://example.com/article1)
- [axiosを使ってrssフィードを取得する方法](https://example.com/article2)

　

## 【Javascript】関連のまとめ
https://hack-note.com/summary/javascript-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

