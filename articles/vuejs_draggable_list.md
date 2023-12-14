【vue.js】ドラッグ可能なリストを作成するためのdraggableの活用方法
javascript,vue.js
vuejs_draggable_list

## 【vue.js】ドラッグ可能なリストを作成するためのdraggableの活用方法

こんにちは。今回は、vue.jsについて初心者エンジニアに向けて、ドラッグ可能なリストの作成方法をご紹介します。

### リストの表示とデータバインディングの設定方法
まずは、リストの表示とデータバインディングの設定方法について説明します。

vue.jsでは、データの表示やバインディングにv-forディレクティブを使用します。これを活用して、リストを表示し、データのバインディングを行います。

```html
<template>
  <ul>
    <li v-for="(item, index) in list" :key="index">
      {{ item }}
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      list: ["item 1", "item 2", "item 3", "item 4", "item 5"]
    };
  }
};
</script>
```

上記のコードでは、v-forディレクティブを使用してリストの要素を表示しています。データのバインディングは、v-forディレクティブのループ内で行われており、リストの要素を{{ item }}で表示しています。

### ドラッグ操作の有効化とリストアイテムの設定
次に、ドラッグ操作を有効化し、リストアイテムの設定を行います。

draggableを使用することで、リストアイテムをドラッグ可能にすることができます。v-onディレクティブを使用して、ドラッグイベントを監視し、必要な処理を行います。

```html
<template>
  <ul>
    <li v-for="(item, index) in list" :key="index" draggable @dragstart="handledragstart" @dragend="handledragend">
      {{ item }}
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      list: ["item 1", "item 2", "item 3", "item 4", "item 5"],
      draggingitem: null
    };
  },
  methods: {
    handledragstart(event) {
      this.draggingitem = event.target;
      event.datatransfer.effectallowed = "move";
    },
    handledragend() {
      this.draggingitem = null;
    }
  }
};
</script>
```

上記のコードでは、各リストアイテムにdraggable属性を追加し、dragstartとdragendイベントを監視しています。また、dragstartイベントが発生した時には、ドラッグ中のアイテムをthis.draggingitemに格納し、dragendイベントが発生した時には、this.draggingitemをクリアする処理を行っています。

### ドラッグアンドドロップのソート機能の実装方法
次に、ドラッグアンドドロップのソート機能の実装方法について説明します。

vue.jsでは、v-onディレクティブを使用してドラッグイベントを監視し、リストの要素の順序を変更することで、ドラッグアンドドロップのソート機能を実現することができます。

```html
<template>
  <ul>
    <li v-for="(item, index) in list" :key="index" draggable @dragstart="handledragstart(index)" @dragenter="handledragenter" @dragover.prevent @drop="handledrop">
      {{ item }}
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      list: ["item 1", "item 2", "item 3", "item 4", "item 5"],
      draggingindex: null
    };
  },
  methods: {
    handledragstart(index) {
      this.draggingindex = index;
      event.datatransfer.effectallowed = "move";
    },
    handledragenter(event) {
      event.target.classlist.add("drag-over");
    },
    handledrop(event) {
      event.preventdefault();
      const droppedindex = event.target.getattribute("data-index");
      this.list.splice(this.draggingindex, 1);
      this.list.splice(droppedindex, 0, this.draggingindex);
      this.draggingindex = null;
      event.target.classlist.remove("drag-over");
    }
  }
};
</script>
```

上記のコードでは、ドラッグアンドドロップのソート機能を実現するために、dragenter、dragover、dropイベントを追加し、各イベントのハンドラを設定しています。また、dragenterイベントが発生した時には、ドラッグオーバー時のスタイルを適用し、dropイベントが発生した時には、ドラッグ中のアイテムの順序を変更する処理を行っています。

### リスト内の要素の移動と順序の変更手法
次に、リスト内の要素の移動と順序の変更手法について説明します。

リスト内の要素の移動と順序の変更は、ドラッグアンドドロップのソート機能を使用して行います。ユーザーが要素をドラッグして移動することで、リスト内の順序を変更することができます。

```html
<template>
  <ul>
    <li v-for="(item, index) in list" :key="index" draggable @dragstart="handledragstart(index)" @dragenter="handledragenter(index)" @dragover.prevent @drop="handledrop">
      {{ item }}
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      list: ["item 1", "item 2", "item 3", "item 4", "item 5"],
      draggingindex: null,
      droptargetindex: null
    };
  },
  methods: {
    handledragstart(index) {
      this.draggingindex = index;
      event.datatransfer.effectallowed = "move";
    },
    handledragenter(index) {
      this.droptargetindex = index;
    },
    handledrop() {
      this.list.splice(this.droptargetindex, 0, this.list.splice(this.draggingindex, 1)[0]);
      this.draggingindex = null;
      this.droptargetindex = null;
    }
  }
};
</script>
```

上記のコードでは、handledragenterイベントのハンドラに、droptargetindexを設定し、handledropイベントのハンドラ内で、リストの順序を変更する処理を行っています。

### リストの更新と変更の監視方法
最後に、リストの更新と変更の監視方法について説明します。

リストの更新と変更の監視は、vue.jsのリアクティブな機能を使用して行います。vue.jsでは、配列やオブジェクトの変更を検知して、自動的にuiを更新することができます。

```html
<template>
  <ul>
    <li v-for="(item, index) in list" :key="index" draggable @dragstart="handledragstart(index)" @dragenter="handledragenter(index)" @dragover.prevent @drop="handledrop(index)">
      {{ item }}
    </li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      list: ["item 1", "item 2", "item 3", "item 4", "item 5"],
      draggingindex: null,
      droptargetindex: null
    };
  },
  methods: {
    handledragstart(index) {
      this.draggingindex = index;
      event.datatransfer.effectallowed = "move";
    },
    handledragenter(index) {
      this.droptargetindex = index;
    },
    handledrop(index) {
      this.list.splice(this.droptargetindex, 0, this.list.splice(this.draggingindex, 1)[0]);
      this.draggingindex = null;
      this.droptargetindex = null;
    }
  },
  watch: {
    list() {
      // リストの変更を検知して処理を行う
    }
  }
};
</script>
```

上記のコードでは、vue.jsのwatch機能を使用して、リストの変更を監視し、変更があった場合に任意の処理を行うことができます。リストが変更される度にlistメソッドがトリガーされ、処理が実行されます。

以上が、vue.jsを使用してドラッグ可能なリストを作成するためのdraggableの活用方法です。これにより、初心者のエンジニアでも簡単にドラッグアンドドロップの機能を実装することができます。

参考ブログ記事:
- [creating a draggable list in vue.js](https://krishnendu.io/blog/create-draggable-list-vuejs/)
- [how to create a draggable sortable list in vue.js](https://www.digitalocean.com/community/tutorials/vuejs-draggable-sortable-list)

　

## 【Vue.js】関連のまとめ
https://hack-note.com/summary/vuejs-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)


