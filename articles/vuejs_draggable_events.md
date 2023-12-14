【vue.js】ドラッグアンドドロップの操作イベントとハンドリング方法
javascript,vue.js
vuejs_draggable_events

## ドラッグアンドドロップの基本的な操作イベントの概要

ドラッグアンドドロップは、ユーザーが要素をマウスでドラッグし、別の場所にドロップする操作のことです。vue.jsでは、ドラッグアンドドロップの操作に関連するさまざまなイベントが用意されており、これらのイベントをハンドリングすることで、ドラッグアンドドロップの挙動をカスタマイズすることができます。

主なドラッグアンドドロップの操作イベントは以下の通りです。

- dragstart: ドラッグが開始されたときに発火するイベント
- drag: ドラッグ中に発火するイベント
- dragenter: ドラッグ中にドロップ可能な要素にカーソルが入ったときに発火するイベント
- dragleave: ドラッグ中にドロップ可能な要素からカーソルが離れたときに発火するイベント
- dragover: ドラッグ中にドロップ可能な要素上でカーソルが動いたときに発火するイベント
- drop: ドロップ可能な要素にドロップされたときに発火するイベント
- dragend: ドラッグが終了したときに発火するイベント

これらのイベントを適切にハンドリングすることで、ドラッグアンドドロップの挙動に対してカスタマイズした処理を追加することができます。次に、それぞれのイベントのハンドリング方法と具体的な活用例について見ていきましょう。

## ドラッグ開始イベントのハンドリング方法と活用例

ドラッグ開始イベント（dragstart）は、要素がドラッグされたときに発火するイベントです。このイベントをハンドリングすることで、ドラッグアンドドロップ操作の開始時に特定の処理を追加することができます。

以下のコードは、ドラッグ可能な要素を定義し、ドラッグ開始イベントをハンドリングする方法の例です。

```html
<template>
  <div>
    <div
      draggable="true"
      @dragstart="handledragstart"
    >
      ドラッグ可能な要素
    </div>
    <div
      id="dropzone"
      @dragover="handledragover"
      @drop="handledrop"
    >
      ドロップ可能な要素
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    handledragstart(event) {
      // ドラッグを開始するときの処理
      event.datatransfer.setdata("text/plain", event.target.id);
    },
    handledragover(event) {
      // ドラッグ中に要素上でカーソルが動いたときの処理
      event.preventdefault();
    },
    handledrop(event) {
      // ドロップされたときの処理
      event.preventdefault();
      const data = event.datatransfer.getdata("text/plain");
      const dropzone = document.getelementbyid("dropzone");
      const draggedelement = document.getelementbyid(data);
      dropzone.appendchild(draggedelement);
    },
  },
};
</script>
```

この例では、`draggable`属性をtrueに設定することで、要素をドラッグ可能にしています。また、ドラッグ開始イベント（`dragstart`）をハンドリングすることで、ドラッグが開始されたときに特定の処理（ここでは、`event.datatransfer.setdata`を使用してドラッグされた要素のidをセットしています）を実行することができます。

## ドラッグ中の要素位置の更新と表示の反映方法

ドラッグ中の要素位置の更新と表示の反映は、ドラッグ中のイベント（`drag`）を適切にハンドリングすることで行うことができます。ドラッグ中のイベントは、要素がドラッグされている間ずっと発火し続けるため、要素の位置を更新する処理をここで行うことができます。

以下のコードは、ドラッグ中の要素位置の更新と表示の反映を行う方法の例です。

```html
<template>
  <div>
    <div
      draggable="true"
      @dragstart="handledragstart"
      @drag="handledrag"
    >
      ドラッグ可能な要素
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    handledragstart(event) {
      // ドラッグを開始するときの処理
      event.datatransfer.setdata("text/plain", event.target.id);
    },
    handledrag(event) {
      // ドラッグ中の処理
      const draggedelement = document.getelementbyid(event.datatransfer.getdata("text/plain"));
      draggedelement.style.left = event.clientx + "px";
      draggedelement.style.top = event.clienty + "px";
    },
  },
};
</script>
```

この例では、`drag`イベントをハンドリングして、要素の位置を更新する処理を行っています。具体的には、`event.clientx`と`event.clienty`を使用して、マウスカーソルの座標を取得し、それを使ってドラッグ中の要素の位置を指定しています。

## ドロップイベントのハンドリングとドロップ時の処理手法

ドロップイベント（`drop`）は、ドロップ可能な要素に要素がドロップされたときに発火するイベントです。このイベントをハンドリングすることで、ドロップされたときに特定の処理を追加することができます。

以下のコードは、ドロップイベントのハンドリングとドロップ時の処理を行う方法の例です。

```html
<template>
  <div>
    <div
      draggable="true"
      @dragstart="handledragstart"
    >
      ドラッグ可能な要素
    </div>
    <div
      id="dropzone"
      @dragover="handledragover"
      @drop="handledrop"
    >
      ドロップ可能な要素
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    handledragstart(event) {
      // ドラッグを開始するときの処理
      event.datatransfer.setdata("text/plain", event.target.id);
    },
    handledragover(event) {
      // ドラッグ中に要素上でカーソルが動いたときの処理
      event.preventdefault();
    },
    handledrop(event) {
      // ドロップされたときの処理
      event.preventdefault();
      const data = event.datatransfer.getdata("text/plain");
      const dropzone = document.getelementbyid("dropzone");
      const draggedelement = document.getelementbyid(data);
      dropzone.appendchild(draggedelement);
      console.log("要素がドロップされました！");
    },
  },
};
</script>
```

この例では、ドロップイベント（`drop`）をハンドリングして、ドロップが発生したときに特定の処理（ここでは、要素をドロップ可能な要素に追加している部分と、コンソールにメッセージを出力しています）を追加しています。また、ドラッグ中の要素をドロップ可能な要素に追加するために、`appendchild`を使用しています。

## ドラッグアンドドロップ操作のキャンセルとリセット方法

ドラッグアンドドロップ操作をキャンセルしたい場合や、ドラッグアンドドロップ操作の状態をリセットしたい場合は、以下のような方法があります。

- キャンセル: `dragenter`イベントや`dragover`イベントのハンドラ内で、`event.preventdefault()`を呼び出すことで、ドロップをキャンセルすることができます。また、`dragend`イベントのハンドラ内で、`event.preventdefault()`を呼び出すことで、ドラッグをキャンセルすることができます。

- リセット: `dragend`イベントのハンドラ内で、要素の位置やプロパティを元の状態に戻すことで、ドラッグアンドドロップ操作の状態をリセットすることができます。

以下のコードは、ドラッグアンドドロップ操作のキャンセルとリセットの方法の例です。

```html
<template>
  <div>
    <div
      draggable="true"
      @dragstart="handledragstart"
      @dragend="handledragend"
    >
      ドラッグ可能な要素
    </div>
    <div
      id="dropzone"
      @dragenter="handledragenter"
      @dragover="handledragover"
      @dragleave="handledragleave"
      @drop="handledrop"
    >
      ドロップ可能な要素
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    handledragstart(event) {
      // ドラッグを開始するときの処理
      event.datatransfer.setdata("text/plain", event.target.id);
    },
    handledragend(event) {
      // ドラッグが終了したときの処理（キャンセル）
      event.preventdefault();
      console.log("ドラッグがキャンセルされました！");
    },
    handledragenter(event) {
      // ドラッグ中にドロップ可能な要素にカーソルが入ったときの処理
      event.preventdefault();
      event.target.classlist.add("dragover");
    },
    handledragover(event) {
      // ドラッグ中に要素上でカーソルが動いたときの処理
      event.preventdefault();
      event.target.classlist.add("dragover");
    },
    handledragleave(event) {
      // ドラッグ中にドロップ可能な要素からカーソルが離れたときの処理
      event.preventdefault();
      event.target.classlist.remove("dragover");
    },
    handledrop(event) {
      // ドロップされたときの処理
      event.preventdefault();
      event.target.classlist.remove("dragover");
      const data = event.datatransfer.getdata("text/plain");
      const dropzone = document.getelementbyid("dropzone");
      const draggedelement = document.getelementbyid(data);
      dropzone.appendchild(draggedelement);
      console.log("要素がドロップされました！");
    },
  },
};
</script>

<style scoped>
.dragover {
  background-color: yellow;
}
</style>
```

この例では、`dragend`イベントのハンドラ内で`event.preventdefault()`を呼び出すことで、ドラッグをキャンセルしています。また、ドラッグ中にドロップ可能な要素にカーソルが入ったとき（`dragenter`イベント）や、要素上でカーソルが動いたとき（`dragover`イベント）に、カスタムクラスを追加して背景色を変えることで、ユーザーに視覚的なフィードバックを与えています。また、`dragleave`イベントのハンドラ内で、カスタムクラスを削除することで、要素からカーソルが離れたときにもフィードバックを与えています。

以上が、vue.jsを使用したドラッグアンドドロップの操作イベントとハンドリング方法の概要です。これらのイベントとハンドリング方法を駆使することで、より柔軟なドラッグアンドドロップの挙動を実現することができます。初心者エンジニアの方もぜひチャレンジしてみてください。

参考資料：
- [vue.jsドラッグアンドドロップ関連イベント](https://jp.vuejs.org/v2/guide/events.html#%e3%83%89%e3%83%a9%e3%83%83%e3%82%b0%e3%82%a2%e3%83%b3%e3%83%89%e3%83%89%e3%83%ad%e3%83%83%e3%83%97%e9%96%a2%e9%80%a3%e3%82%a4%e3%83%99%e3%83%b3%e3%83%88)
- [mdn web docs - drag and drop api](https://developer.mozilla.org/ja/docs/web/api/html_drag_and_drop_api)

　

## 【Vue.js】関連のまとめ
https://hack-note.com/summary/vuejs-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

