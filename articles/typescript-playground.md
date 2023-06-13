<!--
title: 【typescript】playgroundを使って学ぶ、型の使い方とデバッグテクニック
tags: typescript,playground
id: 
private: false
-->

こんにちは。今回は、typescriptについて初心者エンジニアに向けて、playgroundを利用した型の使い方とデバッグテクニックについて解説したいと思います。

近年、web開発においてjavascriptを利用するケースが増えてきました。しかし、javascriptは動的に型付けされるのが特徴であり、開発者が複数人いた場合に予期せぬバグが生じることがあります。そこで、javascriptの型付けを可能とするライブラリであるtypescriptが注目されています。

typescriptは、microsoftが開発したフリーソフトウェアで、javascriptのスーパーセットとして機能します。つまり、javascriptを拡張した言語と言えます。変数や関数、オブジェクトなどに型情報を与えることで、開発時に早期にバグを検出することができるようになります。

しかし、typescriptを学ぶためには、開発環境を整えたり、コンパイル作業を行ったりする必要があり、初心者にはハードルが高いと感じる方も多いかもしれません。そこで、本記事では、簡単にtypescriptを試せるオンラインエディタであるplaygroundを使って、型の使い方とデバッグテクニックを学びたいと思います。

## typescript playgroundとは何か？

playgroundは、microsoftが提供するtypescriptの練習用オンラインエディタです。webブラウザ上で利用することができ、htmlやcssのように、開発環境を用意する必要がありません。また、保存やテスト、共有なども簡単に行うことができます。

playgroundでの開発は、左側のエディタでコードを書き、右側の出力で結果を表示する形式です。また、エディタ下部には、エラーや警告、デバッグ情報も表示されるため、開発時に役立ちます。

## playgroundで型の使い方を学ぶ

playgroundを使って、まずは型の使い方を学んでみましょう。

### 基本的な型

```typescript
const num: number = 123;
const str: string = "hello world";
const bool: boolean = true;
```

上記のように、変数には型を明示することができます。例えば、numには数値型、strには文字列型、boolには真偽値型の情報が与えられます。

### 配列とタプル型

```typescript
const arr: number[] = [1, 2, 3];
const tuple: [string, number] = ["typescript", 3];
```

配列型は、大括弧[]で囲んだ中に、要素の型を記述します。タプル型は、配列とは異なり、各要素の型も明示する必要があります。

### オブジェクトとインターフェイス

```typescript
interface person {
  name: string;
  age: number;
}
const person: person = { name: "john", age: 20 };
```

インターフェイスは、オブジェクトの型を定義する方法です。例えば、上記のようにpersonというインターフェイスを定義し、オブジェクトに適用することで、nameプロパティとageプロパティの型を明示的に表現することができます。

### 関数とジェネリクス

```typescript
function multiply(a: number, b: number): number {
  return a * b;
}
const result = multiply(2, 3);

function toarray<t>(arg1: t, arg2: t): t[] {
  return [arg1, arg2];
}
const arr = toarray<string>("hello", "world");
```

関数にも型付けをすることができます。上記のように、multiply関数には数値型の引数aとb、数値型の戻り値を与えることができます。ジェネリクスを使うことで、関数の型に柔軟性を持たせることもできます。

### 型の継承

```typescript
interface animal {
  name: string;
  age: number;
}
interface dog extends animal {
  breed: string;
}
const dog: dog = { name: "pochi", age: 3, breed: "shiba" };
```

インターフェイスは、他のインターフェイスから型を継承することができます。上記のように、dogというインターフェイスはanimalから派生しており、nameとageプロパティを継承しています。

## playgroundでデバッグテクニックを磨く

次に、playgroundを使ってデバッグテクニックを磨いてみましょう。playgroundには、変数の値を表示したり、調査したい箇所にブレークポイントを設定することができます。

### デバッグ用console.log

```typescript
const str = "hello";
console.log(str.length);
```

console.log関数は、webブラウザのコンソールに変数の値を表示させることができます。上記の例では、str.lengthをconsole.logに渡すことで、文字列の長さを表示しています。

### ブレークポイントの設定

```typescript
let sum = 0;
for (let i = 1; i <= 10; i++) {
  sum += i;
}
console.log(sum);
```

playgroundのエディタの左端にある行番号をクリックすることで、ブレークポイントを設定することができます。ブレークポイントを設定してから、実行ボタンをクリックすると、その箇所で処理が一時停止します。

## 使い方についてのヒントとコツ

playgroundを使って学ぶ際に、以下のようなヒントやコツを押さえておくと、より効率的な学習を行うことができます。

### サンプルコードの利用

playgroundには、サンプルコードが多数用意されています。これらのコードを読み込んで、自分で手を加えて動作を確認することで、型の使い方について理解を深めることができます。

### 試行錯誤する

playgroundは、コンパイルが即座に実行されます。そのため、試行錯誤を繰り返し、コードを修正することで、深い理解を得ることができます。

### エラーをチェックしよう

playgroundは、エディタ下部にエラーや警告の情報を表示します。エラーが表示された場合は、その箇所を修正することで正しいコードに修正できます。

## より良いコードを書くためのアドバイス

最後に、より良いコードを書くためのアドバイスを紹介します。

### 不要な型指定を避ける

変数の型が明らかな場合は、型指定を省略することができます。これにより、コードの可読性が上がり、冗長な情報が減るため、コードのサイズも小さくなります。

```typescript
const num = 123;
```

### 型エイリアスを使う

複雑な型や、何度も使い回す型は、型エイリアスを定義することにより、コードの重複を避けることができます。

```typescript
type user = {
  name: string;
  age: number;
};
const user: user = { name: "john", age: 20 };
```

### オーバーロードを使う

型の違いによって引数の数や型が異なる場合、オーバーロードを使うことで、コードの可読性を上げることができます。

```typescript
function twice(num: number): number;
function twice(str: string): string;
function twice(arg: number | string): number | string {
  return arg + arg;
}
const result1 = twice(2);
const result2 = twice("hello");
```

以上、playgroundを使って学ぶ、型の使い方とデバッグテクニックについて紹介しました。typescriptは、動的に型付けされるjavascriptよりも、開発者の間で注目を集めている言語です。playgroundを利用することで、初心者でも手軽にtypescriptの学習を始めることができます。ぜひ、本記事を参考にして、typescriptの使い方をマスターしていきましょう。

参考url：

- [typescript playground](https://www.typescriptlang.org/play) 
- [typescript playgroundの使い方](https://qiita.com/tonkotsuboy_com/items/a1da811323057b8cf32e)


## typescript関連のまとめ
https://hack-note.com/tools/typescript-summary/


## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)

