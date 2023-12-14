【ios 17】カメラと写真機能の進化
ios,ios17
ios17-camera-photos


## 新たなカメラ機能と写真撮影のクオリティ向上

こんにちは。今回は、ios 17について初心者エンジニアに向けて、新たなカメラ機能と写真撮影のクオリティ向上についてご紹介します。

ios 17では、カメラ機能が大幅に進化し、より高品質な写真撮影が可能となりました。新たなカメラ機能には、以下のような特徴があります。

- カメラセンサーの最新技術の採用
- 画像処理の高速化
- ノイズリダクションの改善
- カメラレンズの改良
- デジタルズームの精度向上

これらの新機能により、従来のiosよりもさらに高解像度で鮮明な写真を撮影することができます。また、低照度下でもより明るく美しい写真を撮影することが可能となりました。

さらに、ios 17では撮影モードの豊富さも強化されており、様々なシーンに合わせた最適なモードを選択することができます。例えば、ポートレートモードでは被写体を際立たせる背景ボケ効果を実現し、風景モードでは広角レンズを活用してより広い範囲を綺麗に撮影することができます。

また、写真撮影時の手ブレを補正する手ぶれ防止機能も搭載されており、よりクリアな写真を撮影することができます。これにより、暗い場所や動く被写体でもブレずに綺麗な写真を撮影することができます。

以下のようなサンプルコードを用意しました。

```swift
import uikit
import avfoundation

class cameraviewcontroller: uiviewcontroller, avcapturephotocapturedelegate {
    
    // カメラキャプチャのセッション
    let capturesession = avcapturesession()
    
    // カメラ入力
    var videoinput: avcapturedeviceinput!
    
    // 静止画出力
    let photooutput = avcapturephotooutput()
    
    // プレビューレイヤー
    var previewlayer: avcapturevideopreviewlayer!
    
    override func viewdidload() {
        super.viewdidload()
        
        // カメラの初期設定
        setupcamera()
    }
    
    func setupcamera() {
        // カメラデバイスの取得
        guard let camera = avcapturedevice.default(for: .video) else { return }
        
        do {
            // カメラからの入力を作成
            videoinput = try avcapturedeviceinput(device: camera)
            
            // セッションに入力を追加
            if capturesession.canaddinput(videoinput) {
                capturesession.addinput(videoinput)
            }
            
            // セッションに出力を追加
            if capturesession.canaddoutput(photooutput) {
                capturesession.addoutput(photooutput)
            }
            
            // プレビューレイヤーを作成
            previewlayer = avcapturevideopreviewlayer(session: capturesession)
            previewlayer.frame = view.bounds
            view.layer.addsublayer(previewlayer)
            
            // カメラキャプチャを開始
            capturesession.startrunning()
        } catch {
            print(error)
        }
    }
    
    // シャッターボタンが押された時に呼ばれるメソッド
    @ibaction func capturebuttontapped(_ sender: uibutton) {
        let settings = avcapturephotosettings()
        photooutput.capturephoto(with: settings, delegate: self)
    }
    
    // 静止画がキャプチャされた時に呼ばれるメソッド
    func photooutput(_ output: avcapturephotooutput, 
                     didfinishprocessingphoto photo: avcapturephoto, 
                     error: error?) {
        if let imagedata = photo.filedatarepresentation() {
            // キャプチャした写真を保存
            savephoto(imagedata)
        }
    }
    
    func savephoto(_ imagedata: data) {
        // ここで写真の保存処理を行う
    }
}
```

このサンプルコードは、avcapturesessionを使用してカメラキャプチャを行い、静止画を撮影する機能を実装しています。また、カメラのプレビュー画面も表示されます。これを利用することで、カスタムのカメラアプリや写真撮影機能を自由に開発することができます。

## プロフェッショナルな編集ツールと写真補正機能

ios 17では、写真の編集ツールや補正機能も充実しています。これにより、簡単に写真を編集してより美しい結果を得ることができます。

新たな編集ツールには、以下のような機能があります。

- トリミングや回転、フリップなどの基本的な編集機能
- 色調補正や露出補正といった写真補正機能
- フィルターやエフェクトの追加
- レタッチ機能（シミ除去、赤目補正など）の追加

しかも、これらの編集ツールは直感的に操作できるシンプルなインターフェースで提供されています。初心者の方でも簡単に写真の編集が行えるため、写真のクオリティを向上させたい方にとっては非常に便利な機能と言えます。

以下のようなサンプルコードを用意しました。

```swift
import uikit
import coreimage

class photoeditviewcontroller: uiviewcontroller {
    
    @iboutlet weak var imageview: uiimageview!
    
    var originalimage: uiimage!
    var editedimage: uiimage!
    
    override func viewdidload() {
        super.viewdidload()
        
        // 編集前の画像を表示
        imageview.image = originalimage
    }
    
    // トリミングボタンが押された時に呼ばれるメソッド
    @ibaction func cropbuttontapped(_ sender: uibutton) {
        let rect = cgrect(x: 100, y: 100, width: 200, height: 200)
        
        // トリミング処理を実行
        editedimage = cropimage(originalimage, torect: rect)
        
        // 画像を更新
        imageview.image = editedimage
    }
    
    // 色調補正ボタンが押された時に呼ばれるメソッド
    @ibaction func adjustbuttontapped(_ sender: uibutton) {
        // 色調補正処理を実行
        editedimage = adjustimage(originalimage, brightness: 0.5, contrast: 1.0, saturation: 1.0)
        
        // 画像を更新
        imageview.image = editedimage
    }
    
    // フィルターボタンが押された時に呼ばれるメソッド
    @ibaction func filterbuttontapped(_ sender: uibutton) {
        // フィルター処理を実行
        editedimage = applyfilter(originalimage, filtername: "ciphotoeffectmono")
        
        // 画像を更新
        imageview.image = editedimage
    }
    
    // トリミング処理
    func cropimage(_ image: uiimage, torect rect: cgrect) -> uiimage {
        let cgimage = image.cgimage!.cropping(to: rect)!
        return uiimage(cgimage: cgimage)
    }
    
    // 色調補正処理
    func adjustimage(_ image: uiimage, brightness: cgfloat, contrast: cgfloat, saturation: cgfloat) -> uiimage {
        let context = cicontext(options: nil)
        
        let ciimage = ciimage(image: image)!
        let filter = cifilter(name: "cicolorcontrols")!
        filter.setvalue(ciimage, forkey: kciinputimagekey)
        filter.setvalue(brightness, forkey: kciinputbrightnesskey)
        filter.setvalue(contrast, forkey: kciinputcontrastkey)
        filter.setvalue(saturation, forkey: kciinputsaturationkey)
        
        let outputimage = filter.outputimage!
        let cgimage = context.createcgimage(outputimage, from: ciimage.extent)!
        
        return uiimage(cgimage: cgimage)
    }
    
    // フィルター処理
    func applyfilter(_ image: uiimage, filtername: string) -> uiimage {
        let context = cicontext(options: nil)
        
        let ciimage = ciimage(image: image)!
        let filter = cifilter(name: filtername)!
        filter.setvalue(ciimage, forkey: kciinputimagekey)
        
        let outputimage = filter.outputimage!
        let cgimage = context.createcgimage(outputimage, from: ciimage.extent)!
        
        return uiimage(cgimage: cgimage)
    }
    
    // 保存ボタンが押された時に呼ばれるメソッド
    @ibaction func savebuttontapped(_ sender: uibutton) {
        guard let editedimage = editedimage else { return }
        
        // ここで写真の保存処理を行う
    }
}
```

このサンプルコードでは、写真のトリミング、色調補正、フィルターの適用といった基本的な編集処理を行うためのメソッドが実装されています。これを利用することで、写真の編集機能を簡単に追加することができます。

## モード切替とフィルター効果の拡大

ios 17では、カメラアプリで使えるモード切替とフィルター効果も大幅に拡大されました。これにより、より多彩な写真表現が可能となりました。

モード切替には、以下のような機能が追加されました。

- スローモーションモード: ハイスピードで動画を撮影し、スローモーションで再生することができます。
- タイムラプスモード: 複数の写真を一定の間隔で撮影し、短時間で再生することで時間の経過を表現します。
- パノラマモード: 連続して写真を撮影し、自動的にパノラマ写真を生成します。

また、フィルター効果も追加され、写真にさまざまな雰囲気を与えることができます。フィルターは、写真撮影時だけでなく、事後の編集時にも適用することができるため、より自由な表現が可能となりました。

以下のようなサンプルコードを用意しました。

```swift
import uikit
import coreimage

class cameraviewcontroller: uiviewcontroller {
    
    @iboutlet weak var imageview: uiimageview!
    
    var originalimage: uiimage!
    var filteredimage: uiimage!
    
    override func viewdidload() {
        super.viewdidload()
        
        // カメラの初期設定
        setupcamera()
    }
    
    func setupcamera() {
        // カメラの初期設定
    }
    
    @ibaction func takephotobuttontapped(_ sender: uibutton) {
        // 写真を撮影し、フィルターを適用
        capturephoto { image in
            self.originalimage = image
            self.filteredimage = self.applyfilter(image, filtername: "ciphotoeffectmono")
            
            // フィルターを適用した画像を表示
            self.imageview.image = self.filteredimage
        }
    }
    
    // フィルター処理
    func applyfilter(_ image: uiimage, filtername: string) -> uiimage {
        let context = cicontext(options: nil)
        
        let ciimage = ciimage(image: image)!
        let filter = cifilter(name: filtername)!
        filter.setvalue(ciimage, forkey: kciinputimagekey)
        
        let outputimage = filter.outputimage!
        let cgimage = context.createcgimage(outputimage, from: ciimage.extent)!
        
        return uiimage(cgimage: cgimage)
    }
    
    // 保存ボタンが押された時に呼ばれるメソッド
    @ibaction func savebuttontapped(_ sender: uibutton) {
        guard let filteredimage = filteredimage else { return }
        
        // ここで写真の保存処理を行う
    }
}
```

このサンプルコードでは、カメラアプリで写真を撮影し、撮影した写真にフィルターを適用しています。フィルター処理は、coreimageフレームワークを使用して実装しています。また、撮影した写真はフィルターを適用する前後の2つの画像として保持しており、保存ボタンが押された時に適用後の画像を保存する処理を行います。

## ライブフォトとメモリー機能の魅力的な活用法

ios 17では、写真アプリのライブフォトとメモリー機能が大幅に進化し、より魅力的な写真体験を提供しています。

ライブフォトでは、写真を撮影するだけでなく、被写体の一瞬の動きや音声も撮影することができます。また、ライブフォトを再生すると、被写体が動き出し、写真がより生き生きとした印象を与えます。


　

## 【iOS 17】関連のまとめ
https://hack-note.com/summary/ios17-summary/

　

## オンラインスクールを講師として活用する！
https://hack-note.com/programming-schools/

　

## 0円でプログラミングを学ぶという選択
- [techacademyの無料体験](//af.moshimo.com/af/c/click?a_id=2612475&amp;p_id=1555&amp;pc_id=2816&amp;pl_id=22706&amp;url=https%3a%2f%2ftechacademy.jp%2fhtmlcss-trial%3futm_source%3dmoshimo%26utm_medium%3daffiliate%26utm_campaign%3dtextad)
- [オンラインスクール dmm webcamp pro](//af.moshimo.com/af/c/click?a_id=2612482&amp;p_id=1363&amp;pc_id=2297&amp;pl_id=39999&amp;guid=on)
- [レバテックカレッジ｜大学生向け 無料説明会](//af.moshimo.com/af/c/click?a_id=4071793&p_id=3198&pc_id=7488&pl_id=41848)

