Github Gistをエディタで利用する
Github,エディタ,Gist
github-gist-editor

こんにちは。今回は、Githubについて初心者エンジニアに向けて、Github Gistをエディタで利用する方法についてご紹介します。

## Github Gistとは

Github Gistとは、Githubが提供する、コードスニペットを管理するためのサービスです。無料で利用することができ、Githubアカウントがあればすぐに使えます。また、Github GistにはシークレットGistという非公開のGistがあり、自分だけがアクセスできるようにすることができます。

Github Gistは、以下のような特徴があります。

- 複数のコードスニペットを管理できる
- 公開するか非公開にするか選択できる
- コメントやスターを付けることができる
- 同じようなコードを複数の場所で利用することができる

## エディタでGithub Gistを利用する方法

Github Gistを直接編集することもできますが、エディタを使うことでより簡単に管理することができます。ここでは、Visual Studio Codeを例に説明します。

### 1. Gistをクローンする

Gistをエディタで編集するには、まずGistをクローンする必要があります。以下の手順で行います。

1. Github Gistのページで、編集したいGistを開きます。
2. "Clone"をクリックします。
3. URLをコピーします。
4. Visual Studio Codeを開き、"Ctrl+Shift+P"でコマンドパレットを開きます。
5. "Git: Clone"を選択します。
6. コピーしたURLを入力し、"Enter"を押します。

これで、Gistがエディタにクローンされます。

### 2. コードを編集する

エディタでGistを編集します。必要に応じて、ファイルを追加・削除・編集することができます。また、ファイル名を変更したり、フォルダを追加することもできます。

### 3. コミットする

変更をコミットします。エディタのGit機能を使うか、ターミナルからコミットしてください。以下は、エディタのGit機能を使ってコミットする場合の手順です。

1. Visual Studio Codeの"Source Control"パネルを開きます。
2. 変更されたファイルをステージングします。
3. "Ctrl+Enter"でコミットメッセージを入力します。
4. "Ctrl+Enter"でコミットします。

### 4. プッシュする

コミットした変更をGistにプッシュします。Visual Studio CodeのGit機能を使う場合は、"Sync"ボタンをクリックします。

以上で、エディタでGithub Gistを利用する方法が完了しました。

>Github Gistをエディタで利用するには、Gitを使えることが前提となります。Gitの基本的な使い方については別途学習する必要があります。

## サンプルコード

### HTMLファイルを追加する

以下のコマンドを実行することで、新しいHTMLファイルを追加することができます。

```
$ touch index.html
```

### CSSファイルを追加する

以下のコマンドを実行することで、新しいCSSファイルを追加することができます。

```
$ touch style.css
```

## 注意点

Github Gistは、無料で提供されているサービスですが、一定の利用制限があります。以下の点に注意して利用しましょう。

- Gistのファイルサイズは最大50MBまで。
- 匿名でGistを利用する場合、1時間に60回以内のリクエスト制限がある。

## まとめ

Github Gistをエディタで利用する方法についてご紹介しました。Gistをエディタで管理することで、より簡単かつ効率的にコードスニペットを利用することができます。しかしながら、Gitの使い方を理解していなければ、エディタでGistを利用することはできません。Gitの基本的な使い方については、別途学習する必要があります。

最後までお読みいただき、ありがとうございました。

#### 参考記事
- [Visual Studio CodeでGitHubGistを利用する方法【保存版】 \| CUBE SUGAR STORAGE](https://www.cube-sugar.jp/tech/visual-studio-code-github-gist.html)
- [【GitHub】Gist 使い方と CLI \- Qiita](https://qiita.com/HiFaMi/items/e4bf0b35b5d6f51f4a10)

　

## Github 関連のまとめ
https://hack-note.com/summary/github-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

