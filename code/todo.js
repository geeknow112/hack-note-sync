<!--<iframe width="800px" height="600px" src="https://jp.kabumap.com/servlets/kabumap/Action?SRC=stockList/base&chart=marketIndustry&code=260&name=%1b%24%42%33%24%31%3f%1b%28%42">
</iframe>-->

[ad_area]
<script src="https://lober-env-imp.work/wp-content/plugins/order-export/js/jquery.min.js"></script>
<script src="https://lober-env-imp.work/wp-content/plugins/order-export/js/encoding.min.js"></script>
<script>
// .s_01 .accordion_one
$(function(){
  //.accordion_oneの中の.accordion_headerがクリックされたら
  $('.s_01 .accordion_one .accordion_header').click(function(){
    //クリックされた.accordion_oneの中の.accordion_headerに隣接する.accordion_innerが開いたり閉じたりする。
    $(this).next('.accordion_inner').slideToggle();
    $(this).toggleClass("open");
  });
});
</script>

<style>
/*====================================================================
.s_01 .accordion_one
====================================================================*/
.s_01 .accordion_one {
  max-width: 1024px;
  margin: 0 auto;
}
.s_01 .accordion_one .accordion_header {
  background-color: #db0f2f;
  color: #fff;
  font-size: 26px;
  font-weight: bold;
  padding: 20px 11%;
  text-align: center;
  position: relative;
  z-index: +1;
  cursor: pointer;
  transition-duration: 0.2s;
}
.s_01 .accordion_one:nth-of-type(2) .accordion_header {
    background-color: #ff9a05;
}
.s_01 .accordion_one:nth-of-type(3) .accordion_header {
    background-color: #1c85d8;
}
.s_01 .accordion_one .accordion_header:hover {
  opacity: .8;
}
.s_01 .accordion_one .accordion_header .i_box {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  top: 50%;
  right: 5%;
  width: 40px;
  height: 40px;
  border: 1px solid #fff;
  margin-top: -20px;
  box-sizing: border-box;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  transform-origin: center center;
  transition-duration: 0.2s;
}
.s_01 .accordion_one .accordion_header .i_box .one_i {
  display: block;
  width: 18px;
  height: 18px;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  transform-origin: center center;
  transition-duration: 0.2s;
  position: relative;
}
.s_01 .accordion_one .accordion_header.open .i_box {
  -webkit-transform: rotate(-360deg);
  transform: rotate(-360deg);
}
.s_01 .accordion_one .accordion_header .i_box .one_i:before, .s_01 .accordion_one .accordion_header .i_box .one_i:after {
  display: flex;
  content: '';
  background-color: #fff;
  border-radius: 10px;
  width: 18px;
  height: 4px;
  position: absolute;
  top: 7px;
  left: 0;
  -webkit-transform: rotate(0deg);
  transform: rotate(0deg);
  transform-origin: center center;
}
.s_01 .accordion_one .accordion_header .i_box .one_i:before {
  width: 4px;
  height: 18px;
  top: 0;
  left: 7px;
}
.s_01 .accordion_one .accordion_header.open .i_box .one_i:before {
  content: none;
}
.s_01 .accordion_one .accordion_header.open .i_box .one_i:after {
  -webkit-transform: rotate(-45deg);
  transform: rotate(-45deg);
}
.s_01 .accordion_one .accordion_inner {
  display: none;
  padding: 30px 30px;
  border-left: 2px solid #db0f2f;
  border-right: 2px solid #db0f2f;
  border-bottom: 2px solid #db0f2f;
  box-sizing: border-box;
}
.s_01 .accordion_one:nth-of-type(2) .accordion_inner {
  border-left: 2px solid #ff9a05;
  border-right: 2px solid #ff9a05;
  border-bottom: 2px solid #ff9a05;
}
.s_01 .accordion_one:nth-of-type(3) .accordion_inner {
  border-left: 2px solid #1c85d8;
  border-right: 2px solid #1c85d8;
  border-bottom: 2px solid #1c85d8;
}
.s_01 .accordion_one .accordion_inner .box_one {
  height: 300px;
}
.s_01 .accordion_one .accordion_inner p.txt_a_ac {
  margin: 0;
}
@media screen and (max-width: 1024px) {
  .s_01 .accordion_one .accordion_header {
    font-size: 18px;
  }
  .s_01 .accordion_one .accordion_header .i_box {
    width: 30px;
    height: 30px;
    margin-top: -15px;
  }
}
@media screen and (max-width: 767px) {
  .s_01 .accordion_one .accordion_header {
    font-size: 16px;
    text-align: left;
    padding: 15px 60px 15px 15px;
  }
}

/*====================================================================
以下は不要です。
====================================================================*/

body {
  font-family: YuGothic, "游ゴシック体", "Yu Gothic", "ヒラギノ角ゴ Pro", "Hiragino Kaku Gothic Pro", "メイリオ", Meiryo, "ＭＳ Ｐゴシック", "MS PGothic", sans-serif;
  font-size: 16px;
  letter-spacing: .025em;
  line-height: 1.8;
  margin: 0;
}
@media screen and (max-width: 1024px) {
  body {
    font-size: 14px;
  }
}
.section {
  max-width: 1024px;
  margin: 0 auto;
  padding: 20px 20px 500px;
}
.section p._a {
  font-size: 12px;
  font-weight: bold;
  margin: 30px 0 0;
}
.section p._a .link {
  display: inline-block;
  color: #607D8B;
  padding-left: 1.3em;
  text-indent: -1.3em;
}
.section p._a .link:before {
  content: '';
  display: inline-block;
  width: 5px;
  height: 5px;
  border-top: 2px solid #607D8B;
  border-right: 2px solid #607D8B;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  margin-right: 10px;
}
</style>

<div class="section s_01">
  <div class="accordion_one">
    <div class="accordion_header" onclick="ad_pop();">CentOS8にAWS CLIをインストールする<div class="i_box"><i class="one_i"></i></div></div>
    <div class="accordion_inner">
      <div class="box_one">
        <p class="txt_a_ac">
		</p>
      </div>
    </div>
  </div>

  <div class="accordion_one">
    <div class="accordion_header" onclick="ad_pop();">AWS CLIを使ってS3にファイルアップロードする or syncする<div class="i_box"><i class="one_i"></i></div></div>
    <div class="accordion_inner">
      <div class="box_one">
        <p class="txt_a_ac">アコーディオンの中身です。</p>
      </div>
    </div>
  </div>

  <div class="accordion_one">
    <div class="accordion_header" onclick="ad_pop();">AWS CLIを使ってS3にファイルアップロードする or sync後、公開する<div class="i_box"><i class="one_i"></i></div></div>
    <div class="accordion_inner">
      <div class="box_one">
        <p class="txt_a_ac">アコーディオンの中身です。</p>
      </div>
    </div>
  </div>

</div>
