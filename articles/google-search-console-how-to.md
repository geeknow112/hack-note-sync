【基礎】google search consoleの使い方
google,google-search-console,使い方
google-search-console-how-to

こんにちは。今回は、googleの検索エンジン最適化のためのツールである「google search console」について初心者エンジニアに向けて、使い方をご紹介します。

## はじめに

google search consoleとは、自分のwebサイトがgoogleの検索エンジンでどのように表示されているかを調べることができるツールです。また、webサイトの改善や問題点の修正などにも役立ちます。

google search consoleを使って、以下のことを行うことができます。

- webサイトがgoogleに登録されているかどうかを確認する
- クロールエラーを修正する
- ページの検索順位を調べる
- 検索クエリを分析する
- サイトマップを送信してインデックスに追加する

google search consoleを使ってwebサイトのseo対策を行いましょう。

## google search consoleの使い方

### 1. google search consoleの登録方法

まずは、google search consoleに登録する必要があります。googleアカウントをお持ちの場合は、以下のurlから登録してください。
https://search.google.com/search-console/welcome

登録が完了すると、google search consoleのダッシュボードが表示されます。

### 2. サイトの登録方法

ダッシュボードの左側にある「サイトの追加」ボタンをクリックし、webサイトのurlを入力します。

![サイトの登録方法](./images/01.png)

表示された画面で、webサイトの認証方法を選択します。認証方法には、htmlファイルのアップロードやメタタグの追加、dnsレコードの変更、google analyticsとの連携などがあります。

### 3. クロールエラーのチェック

「クロールエラー」とは、googleのクローラーがwebサイト内でエラーになった場合のことを指します。クロールエラーがあると、googleがwebサイトのページを正しくインデックスできなくなるため、検索結果に表示されなくなったり、順位が下がったりする可能性があります。

google search consoleでクロールエラーを確認するには、左側のメニューから「カバレッジ」を選択します。表示された画面で、クロールエラーがあるページを確認し、修正します。

サンプルコード(html)：

```
<meta name="robots" content="noindex,nofollow">
```

上のコードは、googleがwebサイトのページをインデックスしないよう指示するためのコードです。ページの修正ができない場合は、このコードをhead要素内に追加することで、googleがインデックスしないようにすることができます。

### 4. 検索クエリの分析

「検索クエリ」とは、googleユーザーが検索したキーワードのことです。検索クエリの分析を行うことで、webサイトにどのようなキーワードでアクセスされているかを調べることができます。

google search consoleで検索クエリの分析を行うには、左側のメニューから「パフォーマンス」を選択します。表示された画面で、クエリ、クリック数、クリック率、平均順位などを確認することができます。

### 5. サイトマップの送信

「サイトマップ」とは、webサイトの内容を一覧表示するためのxmlファイルのことです。サイトマップをgoogleに送信することで、webサイトのインデックスを促進することができます。

google search consoleでサイトマップを送信するには、左側のメニューから「サイトマップ」を選択し、送信したいサイトマップのurlを入力します。

サンプルコード(xml)：

```
<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://example.com/</loc>
        <lastmod>2022-01-01t00:00:00.000z</lastmod>
        <priority>1.0</priority>
    </url>
</urlset>
```

上のコードは、サイトマップの例です。url要素内に、webサイトのurl、更新日時、優先度を記述します。

## まとめ

google search consoleは、自分のwebサイトの検索エンジン最適化に役立つツールです。クロールエラーのチェックや、検索クエリの分析、サイトマップの送信など、様々な機能を使ってwebサイトのseo対策を行いましょう。

参考：
- [google search consoleの使い方 - seo対策には必須！](https://ferret-plus.com/5991)
- [google search console 使い方ガイド - gscメニュー一覧、基礎操作、分析まで](https://eminemu.com/google-search-console-tutorial/)
