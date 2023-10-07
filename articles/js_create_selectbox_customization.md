【javascript】オリジナルのセレクトボックスを作ろう！createselectbox関数のカスタマイズ方法
javascript
js_create_selectbox_customization

## スタイルのカスタマイズとセレクトボックスのデザイン変更

セレクトボックスは、ウェブページでよく使用される要素の一つですが、デフォルトのデザインがあまり洗練されていないことが多くあります。そこで、オリジナルのセレクトボックスを作成し、デザインをカスタマイズする方法を紹介します。

セレクトボックスのデザインをカスタマイズするためには、cssを使用します。以下のようにcssを追加することで、セレクトボックスのスタイルを変更することができます。

```html
<style>
.custom-select {
  position: relative;
  display: inline-block;
  background-color: #f1f1f1;
  border-radius: 4px;
  padding: 5px;
}
.custom-select select {
  display: none;
}
.custom-select select option {
  padding: 10px;
}
.custom-select .select-selected {
  display: flex;
  align-items: center;
  cursor: pointer;
  padding: 5px;
}
.custom-select .select-selected:after {
  content: '▼';
  font-size: 12px;
  margin-left: 5px;
}
.custom-select .select-items {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  overflow: auto;
  border-radius: 4px;
}
.custom-select .select-items div {
  padding: 10px;
  cursor: pointer;
}
.custom-select .select-items div:hover {
  background-color: #888;
  color: #fff;
}
</style>
```

このcssでは、`.custom-select`クラスがセレクトボックスの親要素を指定しています。その下にある`select`要素は非表示にしておきます。`.select-selected`クラスは、選択されたオプションを表示する要素です。

カスタマイズしたスタイルを適用するためには、htmlのセレクトボックスの要素に`.custom-select`クラスを付ける必要があります。

```html
<div class="custom-select">
  <select>
    <option value="option1">option 1</option>
    <option value="option2">option 2</option>
    <option value="option3">option 3</option>
  </select>
  <div class="select-selected">選択してください</div>
  <div class="select-items">
    <div>option 1</div>
    <div>option 2</div>
    <div>option 3</div>
  </div>
</div>
```

上記のhtmlコードでは、セレクトボックスのデフォルトの見た目を非表示にし、代わりにカスタマイズした見た目を`.select-selected`要素に表示しています。クリックすることで、`.select-items`要素が表示され、その中から選択ができるようになっています。

スタイルのカスタマイズ方法は、cssを自由に編集することで可能です。例えば、背景色や文字色の変更、選択したオプションのスタイルの変更など、様々なカスタマイズが可能です。

## 参考記事:
1. [styling a dropdown with css](https://www.w3schools.com/howto/howto_custom_select.asp)
2. [design custom select box using css](https://www.geeksforgeeks.org/design-css-select-box/)

　

## 【Javascript】関連のまとめ
https://hack-note.com/summary/javascript-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

