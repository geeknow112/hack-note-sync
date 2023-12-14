【vue.js】draggableコンポーネントの基本的な使い方と導入方法
javascript,vue.js
vuejs_draggable_basic_usage

## draggableコンポーネントの導入と依存関係の設定

vue.jsには、ドラッグアンドドロップ機能を実現するためのdraggableコンポーネントが用意されています。このコンポーネントを利用することで、要素のドラッグ操作やドロップ操作を簡単に実装することができます。

### 依存関係の設定

まずはじめに、vue.jsのプロジェクトにdraggableコンポーネントを導入するために、依存関係を設定する必要があります。依存関係は、npmパッケージを使用する場合とcdnを使用する場合とで設定方法が異なります。

#### npmパッケージを使用する場合

npmパッケージを使用する場合は、まずはじめにコマンドラインで以下のコマンドを実行して、draggableパッケージをインストールします。

```
npm install vue-draggable
```

インストールが完了したら、vueコンポーネントでdraggableコンポーネントを使用したい場所で、以下のように依存関係を設定します。

```javascript
import draggable from 'vuedraggable'
vue.component('draggable', draggable)
```

#### cdnを使用する場合

cdnを使用する場合は、htmlファイルに以下のスクリプトを追加します。

```html
<script src="https://cdn.jsdelivr.net/npm/vue"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vue.draggable/2.16.0/vuedraggable.umd.min.js"></script>
```

以上が、draggableコンポーネントの依存関係の設定方法です。

参考ブログ記事：

- [vue.draggable github レポジトリ](https://github.com/sortablejs/vue.draggable)
- [vue.jsでドラッグ＆ドロップを実現するコンポーネント「vuedraggable」を使ってみた](https://qiita.com/wiz_arabian/items/b7d7d2bfc40ab51e4690)

## 基本的なドラッグ操作と要素の移動方法

draggableコンポーネントでは、要素のドラッグ操作が基本的な機能となります。このセクションでは、draggableコンポーネントにおける基本的なドラッグ操作と要素の移動方法について解説します。

### ドラッグ可能な要素の設定

draggableコンポーネントを使用するためには、まず対象となる要素に```draggable```属性を追加する必要があります。この属性を追加することで、要素がドラッグ可能になります。

```html
<draggable>
  <div draggable>item 1</div>
  <div draggable>item 2</div>
  <div draggable>item 3</div>
</draggable>
```

### 要素の移動方法

draggableコンポーネントでは、要素の移動はデフォルトで有効になっており、ユーザーが要素をドラッグすることで移動が可能となります。また、要素の移動可能範囲は、親要素内に制約されます。

要素の移動が発生した場合は、```start```、```update```、```end``` のイベントが発火します。これらのイベントを利用することで、要素の移動に応じた処理を実装することができます。

```html
<draggable @start="onstart" @update="onupdate" @end="onend">
  <div draggable>item 1</div>
  <div draggable>item 2</div>
  <div draggable>item 3</div>
</draggable>
```

```javascript
methods: {
  onstart(event) {
    console.log("drag start: ", event.item);
  },
  onupdate(event) {
    console.log("drag update: ", event.item);
  },
  onend(event) {
    console.log("drag end: ", event.item);
  },
}
```

参考ブログ記事：

- [vue.draggable - example - basic trasition](https://sortablejs.github.io/vue.draggable/#/simple)

## ドラッグ可能な要素のカスタマイズとスタイリングの方法

draggableコンポーネントでは、ドラッグ可能な要素のカスタマイズとスタイリングを行うことができます。このセクションでは、カスタマイズとスタイリングの方法について解説します。

### ドラッグ可能な要素のカスタマイズ

draggableコンポーネントにおいて、ドラッグ可能な要素をカスタマイズするには、```tag``` 属性を使用することができます。```tag``` 属性には任意のhtmlタグ（例：```div```、```span```、```li```など）を指定することができます。

```html
<draggable>
  <div draggable>item 1 (default)</div>
  <div draggable>item 2 (default)</div>
  <div draggable tag="span">item 3 (customized)</div>
</draggable>
```

上記の例では、最初の2つの要素はデフォルトの```div```タグで表示されますが、3番目の要素は```tag``` 属性で指定した```span```タグで表示されます。

### スタイリングのカスタマイズ

draggableコンポーネントでは、要素のスタイリングを自由にカスタマイズすることが可能です。要素にcssクラスを指定したり、```style``` 属性を使用して直接スタイルを指定することができます。

```html
<draggable>
  <div draggable class="item">item 1</div>
  <div draggable class="item">item 2</div>
  <div draggable style="background-color: blue; color: white;">item 3</div>
</draggable>
```

上記の例では、最初の2つの要素には同じcssクラス```item```が指定されており、3番目の要素には```style``` 属性で直接スタイルが指定されています。

参考ブログ記事：

- [vue.draggable - example - styling & classes](https://sortablejs.github.io/vue.draggable/#/styling-classes)

## ドラッグアンドドロップのイベントとハンドリング方法

draggableコンポーネントでは、ドラッグアンドドロップ操作に関連するイベントを利用することができます。このセクションでは、イベントの一覧とそれらのハンドリング方法について解説します。

### ドラッグアンドドロップに関連するイベント

draggableコンポーネントには、以下のようなドラッグアンドドロップに関連するイベントがあります。

- ```start```：ドラッグが開始された際に発火します。
- ```add```：要素がドロップ領域に追加された際に発火します。
- ```remove```：要素がドロップ領域から削除された際に発火します。
- ```update```：要素の位置が更新された際に発火します。
- ```end```：ドラッグが終了した際に発火します。

これらのイベントは、```@```を使用してハンドリングすることができます。

```html
<draggable @start="onstart" @add="onadd" @remove="onremove" @update="onupdate" @end="onend">
  <div draggable>item 1</div>
  <div draggable>item 2</div>
  <div draggable>item 3</div>
</draggable>
```

### イベントのハンドリング方法

イベントをハンドリングするためには、以下のようにメソッドを定義する必要があります。

```javascript
methods: {
  onstart(event) {
    console.log("drag start: ", event.item);
  },
  onadd(event) {
    console.log("item added: ", event.item);
  },
  onremove(event) {
    console.log("item removed: ", event.item);
  },
  onupdate(event) {
    console.log("drag update: ", event.item);
  },
  onend(event) {
    console.log("drag end: ", event.item);
  },
}
```

上記の例では、各イベントが発生した際にコンソールにメッセージを表示するだけのシンプルな実装例です。これらのイベントを活用することで、ドラッグアンドドロップ操作に応じた処理を自由に実装することが可能です。

参考ブログ記事：

- [vue.draggable - example - events](https://sortablejs.github.io/vue.draggable/#/events)

## ドラッグ操作の制約とドロップゾーンの設定方法

draggableコンポーネントでは、要素のドラッグ操作を制約することができます。また、ドラッグアンドドロップの対象となる要素の範囲を制限するためのドロップゾーンの設定も可能です。このセクションでは、ドラッグ操作の制約とドロップゾーンの設定方法について解説します。

### ドラッグ操作の制約

draggableコンポーネントでは、要素のドラッグ操作を制約するために、```lock-axis``` 属性や```lock-handle```属性を使用することができます。

```lock-axis``` 属性は、要素のドラッグ操作を特定の軸に制限するために使用されます。具体的には、```x```を指定することで水平方向にドラッグを制約し、```y```を指定することで垂直方向にドラッグを制約します。

```lock-handle``` 属性は、ドラッグ操作が適用される要素内の特定の要素を指定するために使用されます。指定された要素内でのみドラッグ操作が有効となり、他の要素ではドラッグが無効となります。

```html
<draggable :lock-axis="'x'" :lock-handle="'.handle'">
  <div draggable class="item">
    <span class="handle">handle</span>
    item 1
  </div>
  <div draggable class="item">
    <span class="handle">handle</span>
    item 2
  </div>
  <div draggable class="item">
    <span class="handle">handle</span>
    item 3
  </div>
</draggable>
```

上記の例では、各要素の水平方向へのドラッグを制約するために```lock-axis="'x'"```が指定されており、ドラッグ操作が適用される要素内の```.handle```クラスが指定されている要素がドラッグ操作の対象となっています。

### ドロップゾーンの設定

draggableコンポーネントでは、ドロップゾーンを設定するために、```group```属性や```draggable```属性を使用することができます。

```group``` 属性は、ドラッグアンドドロップ操作を制限するために使用されます。同じ```group```属性が指定された要素間でのみ、ドラッグアンドドロップが有効となります。

```draggable``` 属性は、要素をドラッグアンドドロップの対象とするために使用されます。この属性を指定することで、要素がドラッグ可能となります。

```html
<draggable group="items">
  <div draggable class="item">item 1</div>
  <div draggable class="item">item 2</div>
  <div draggable class="item">item 3</div>
</draggable>

<draggable group="items">
  <div draggable class="item">item 4</div>
  <div draggable class="item">item 5</div>
  <div draggable class="item">item 6</div>
</draggable>
```

上記の例では、2つの```draggable```コンポーネントに同じ```group```属性```items```が指定されており、それぞれのコンポーネント内の要素がドロップゾーンとなっています。

参考ブログ記事：

- [vue.draggable - example - constraints and drop zones](https://sortablejs.github.io/vue.draggable/#/constraints)

　

## 【Vue.js】関連のまとめ
https://hack-note.com/summary/vuejs-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

