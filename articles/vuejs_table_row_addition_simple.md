【vue.js】シンプルな方法でテーブルに行を追加する手順
javascript,vue.js
vuejs_table_row_addition_simple

## 【vue.js】シンプルな方法でテーブルに行を追加する手順

こんにちは。今回は、vue.jsについて初心者エンジニアに向けて、シンプルな方法でテーブルに行を追加する手順について解説します。

### vue.jsでの基本的なテーブルコンポーネントの作成

まず最初に、vue.jsで基本的なテーブルコンポーネントを作成しましょう。以下のようなコードを `table.vue` というファイルに保存します。

```vue
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>name</th>
          <th>email</th>
          <th>age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.age }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { name: "john doe", email: "johndoe@example.com", age: 30 },
        { name: "jane smith", email: "janesmith@example.com", age: 25 },
      ],
    };
  },
};
</script>
```

このコードでは、`items` というデータ配列を用意し、テーブルの各行に対してループ処理を行っています。

### テーブルデータの初期化と表示方法の設定

次に、テーブルデータの初期化と表示方法の設定を行います。

```vue
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>name</th>
          <th>email</th>
          <th>age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.age }}</td>
        </tr>
      </tbody>
    </table>

    <button @click="addrow">add row</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    this.items = [
      { name: "john doe", email: "johndoe@example.com", age: 30 },
      { name: "jane smith", email: "janesmith@example.com", age: 25 },
    ];
  },
  methods: {
    addrow() {
      this.items.push({ name: "", email: "", age: "" });
    },
  },
};
</script>
```

このコードでは、`mounted` ライフサイクルフックを使用して、テーブルの初期データを設定しています。また、`addrow` メソッドを追加して、新しい行をテーブルに追加する処理を実装しています。

### ボタンクリックイベントのリスナー登録と行追加処理の実装

次に、ボタンクリックイベントのリスナー登録と行追加処理の実装を行います。

```vue
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>name</th>
          <th>email</th>
          <th>age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td>{{ item.name }}</td>
          <td>{{ item.email }}</td>
          <td>{{ item.age }}</td>
        </tr>
      </tbody>
    </table>

    <button @click="addrow">add row</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    this.items = [
      { name: "john doe", email: "johndoe@example.com", age: 30 },
      { name: "jane smith", email: "janesmith@example.com", age: 25 },
    ];
  },
  methods: {
    addrow() {
      this.items.push({ name: "", email: "", age: "" });
    },
  },
};
</script>
```

このコードでは、`@click` ディレクティブを使用して、ボタンクリック時に `addrow` メソッドが実行されるように設定しています。`addrow` メソッドでは、`items` 配列に新しいオブジェクトを追加することで、テーブルに行を追加しています。

### データのバインディングと新しい行の表示方法

データのバインディングと新しい行の表示方法を設定してみましょう。

```vue
<template>
  <div>
    <table>
      <thead>
        <tr>
          <th>name</th>
          <th>email</th>
          <th>age</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td><input v-model="item.name" /></td>
          <td><input v-model="item.email" /></td>
          <td><input v-model="item.age" /></td>
        </tr>
      </tbody>
    </table>

    <button @click="addrow">add row</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    this.items = [
      { name: "john doe", email: "johndoe@example.com", age: 30 },
      { name: "jane smith", email: "janesmith@example.com", age: 25 },
    ];
  },
  methods: {
    addrow() {
      this.items.push({ name: "", email: "", age: "" });
    },
  },
};
</script>
```

このコードでは、各セルに input 要素を追加し、`v-model` ディレクティブを使用してデータのバインディングを行っています。これにより、テーブル内のデータを編集できるようになります。

### シンプルなテーブル行追加の手順のまとめと応用例

ここまでの手順をまとめると、以下のようなフローとなります。

1. テーブルコンポーネントを作成する。
2. テーブルデータを初期化し、表示方法を設定する。
3. 行追加のためのボタンクリックイベントのリスナーを登録し、行追加処理を実装する。
4. データのバインディングを行い、新しい行の表示方法を設定する。

この手順を理解していれば、vue.jsでシンプルな方法でテーブルに行を追加することができます。

### 参考url

1. [vue.js 公式ドキュメント](https://vuejs.org/)
2. [vue mastery](https://www.vuemastery.com/)

　

## 【Vue.js】関連のまとめ
https://hack-note.com/summary/vuejs-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

