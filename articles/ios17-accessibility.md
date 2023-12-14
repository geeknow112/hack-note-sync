【ios 17】アクセシビリティ機能の拡張と向上
ios,ios17
ios17-accessibility

## 【ios 17】アクセシビリティ機能の拡張と向上

こんにちは。今回は、ios 17について初心者エンジニアに向けて、アクセシビリティ機能の拡張と向上について紹介します。ios 17では、ユーザーがより快適にデバイスを操作するための機能が多く追加されました。これにより、視覚的に障害のあるユーザーや聴覚的に障害のあるユーザーもスムーズにデバイスを利用することができます。

## バイブレーションとホームボタンのアクセシビリティ設定

ios 17では、バイブレーションとホームボタンのアクセシビリティ設定をパーソナライズすることができます。これにより、視覚的に障害のあるユーザーや聴覚的に障害のあるユーザーがより使いやすい設定に調整することが可能です。

以下は、バイブレーションとホームボタンのアクセシビリティ設定をカスタマイズするサンプルコードです。

```swift
// バイブレーション設定
avaudiosession.sharedinstance().setcategory(.playback, mode: .vibration, options: [])

// ホームボタンのアクセシビリティ設定
uiapplication.shared.isidletimerdisabled = true
```

このサンプルコードでは、avaudiosessionを使用してバイブレーションの設定を変更しています。また、uiapplicationを使用してホームボタンのアクセシビリティ設定を変更しています。これにより、ユーザーは自分に最適な設定でデバイスを使用することができます。

参考：[customizing your app’s behavior](https://developer.apple.com/documentation/avfoundation/customizing_your_app_s_behavior)

## 目の疲れ軽減のためのダークモード拡充

目の疲れを軽減するために、ios 17ではダークモードの機能がさらに拡充されました。ダークモードでは、画面上の明るさを抑えることで、夜間や暗い環境での目の負担を軽減します。また、ユーザーはダークモードをオンにするかオフにするかを選択することができます。

以下は、ダークモードの設定を切り替えるサンプルコードです。

```swift
// ダークモードの設定を切り替える
override func traitcollectiondidchange(_ previoustraitcollection: uitraitcollection?) {
    super.traitcollectiondidchange(previoustraitcollection)
    
    if #available(ios 13.0, *) {
        if self.traitcollection.userinterfacestyle == .dark {
            // ダークモードがオンの場合の処理
            // 画面の明るさを抑えるなどの設定を行う
        } else {
            // ダークモードがオフの場合の処理
            // 通常の明るさの設定を行う
        }
    }
}
```
このサンプルコードでは、traitcollectiondidchangeメソッドを使用してダークモードの設定を切り替えています。ダークモードがオンの場合とオフの場合で異なる処理を行うことができます。

参考：[working with dark mode](https://developer.apple.com/documentation/xcode/supporting_dark_mode_in_your_interface)

## 聴覚支援と字幕表示の改善

聴覚的に障害のあるユーザーをサポートするため、ios 17では聴覚支援と字幕表示が改善されました。これにより、ユーザーはオーディオの内容をより正確に理解することができます。

以下は、字幕表示を有効化するサンプルコードです。

```swift
// 字幕表示の有効化
let player = avplayer(url: url(string: "https://example.com/video.mp4")!)
let subtitleurl = url(string: "https://example.com/subtitle.srt")!
let asset = avurlasset(url: subtitleurl)
let subtitle = avassetresourceloader.loadsubtitle(asset: asset)
player.add(subtitle: subtitle)
```

このサンプルコードでは、avplayerを使用して字幕表示を有効化しています。avurlassetを使用して字幕ファイルを読み込み、avplayerに字幕を追加しています。

参考：[creating a basic video player](https://developer.apple.com/documentation/avfoundation/media_assets_playback_and_editing/creating_a_basic_video_player)

## 読み上げと音声ガイダンスの精度向上

視覚的に障害のあるユーザーをサポートするため、ios 17では読み上げと音声ガイダンスの精度が向上しました。これにより、ユーザーは画面上のテキストや情報をより正確に理解することができます。

以下は、テキストを読み上げるサンプルコードです。

```swift
// テキストを読み上げる
let synthesizer = avspeechsynthesizer()
let utterance = avspeechutterance(string: "読み上げるテキスト")
utterance.voice = avspeechsynthesisvoice(language: "ja-jp")
synthesizer.speak(utterance)
```

このサンプルコードでは、avspeechsynthesizerを使用してテキストを読み上げています。avspeechutteranceを使用して読み上げるテキストを指定し、avspeechsynthesisvoiceを使用して読み上げの声の設定を行っています。

参考：[synthesizing speech](https://developer.apple.com/documentation/avfoundation/media_assets_playback_and_editing/using_avspeechsynthesizer_to_synthesize_speech)

## タッチ操作の補助とジェスチャーコントロールの拡張

タッチ操作が困難なユーザーをサポートするため、ios 17ではタッチ操作の補助とジェスチャーコントロールが拡張されました。これにより、ユーザーはオーディオの内容をより正確に理解することができます。

以下は、タッチ操作の補助とジェスチャーコントロールを設定するサンプルコードです。

```swift
// タッチ操作の補助とジェスチャーコントロールの設定
let tapgesture = uitapgesturerecognizer(target: self, action: #selector(handletap))
tapgesture.numberoftapsrequired = 1
tapgesture.numberoftouchesrequired = 1
view.addgesturerecognizer(tapgesture)

@objc func handletap() {
    // タップが検出された時の処理
}
```

このサンプルコードでは、uitapgesturerecognizerを使用してタップジェスチャーを設定しています。numberoftapsrequiredとnumberoftouchesrequiredを設定することで、タップの検出条件をカスタマイズすることができます。handletapメソッドでは、タップが検出された時の処理を記述します。

参考：[handling gesture recognizers](https://developer.apple.com/documentation/uikit/touches_presses_and_gestures/handling_gesture_recognizers)

　

## 【iOS 17】関連のまとめ
https://hack-note.com/summary/ios17-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

