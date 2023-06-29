【解決】cloneしたgistをvimで編集してpushする方法
github,gist
github-gist-push

こんにちは。今回は、githubについて初心者エンジニアに向けて、cloneしたgistをvimで編集してpushする方法について解説します。

## githubとgistについて

githubは、バージョン管理ツールで世界中のエンジニアが利用するプラットフォームです。gistとは、githubが提供する簡易的なペーストボードのようなものです。

gistは、コードブロックやシンタックスハイライトに対応しているため、エンジニアにとって非常に便利なツールです。gistは、非公開、公開の2つの設定があり、公開されたgistはurlで共有することができます。

## gistのpush方法

gistを編集するためには、まずgistをcloneする必要があります。cloneする方法は、以下のurlの記事を参照してください。

[【解説】githubのgistを使って、共有可能なコードサンプルを作成しよう](https://techacademy.jp/magazine/7044)

gistをcloneしたら、編集して変更をpushすることができます。pushするためには、以下の手順を実行してください。

1. vimなどのテキストエディタで編集する。

2. 変更内容をコミットする。

```
git commit -am "コミットメッセージ"
```

3. pushする。

```
git push origin master
```

## gistをpushしようとしたら「repository not found」エラーが発生した場合

gistをpushしようとしたら、「repository not found」というエラーが発生することがあります。この場合は、以下の手順を実行してください。

1. gistのリポジトリ名を確認する。

gistのurlには、以下のように「gist.github.com」の後ろに「ユーザー名/リポジトリ名」という形式でurlが表示されます。

```
https://gist.github.com/ユーザー名/リポジトリ名
```

この「リポジトリ名」を確認してください。

2. リモートリポジトリを追加する。

以下のコマンドを実行して、リモートリポジトリを追加してください。

```
git remote add origin https://gist.github.com/ユーザー名/リポジトリ名.git
```

3. 再度pushする。

先程と同様に、以下のコマンドを実行してpushしてください。

```
git push origin master
```

これで、gistを編集してpushすることができるようになりました。

>注意: gistは、一般的なリポジトリとは異なるルールがあります。gistでは、masterブランチのみを使用可能です。

以上が、gistを編集してpushする方法になります。初めてのgithubやgistの利用には、少し戸惑うことがあるかもしれませんが、少しずつ慣れていけば、便利なツールとして活用することができます。

　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

