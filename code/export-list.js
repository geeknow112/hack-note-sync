[wp_objects_pdf]

## PDF export
<script src="http://code.jquery.com/jquery-1.11.1.js"></script>
<script>
function export_pdf() {
	//alert('PDF');
}
</script>

<form name="testForm" action="" method="post">
	From:<input type="text" name="from" value="" />
	To:<input type="text" name="to" value="" />
	<input type="hidden" name="export" value="pdf" />
	<input type="submit" value="PDF データ検索"><br /><br />

	<div>
	[export_pdf]
	</div>
</form>

<br /><br />

## CSV export

<script>
const csvDownload = function(data, filename) {
//console.log(data);

// convert to sjis --
const csvData = [data.replace(/\n/g, '\r\n')].join('\r\n');

const unicodeList = [];
for (let i = 0; i < csvData.length; i += 1) {
  unicodeList.push(csvData.charCodeAt(i));
}

// 変換処理の実施
//const shiftJisCodeList = Encoding.convert(unicodeList, 'sjis', 'unicode');
const shiftJisCodeList = unicodeList;
const uInt8List = new Uint8Array(shiftJisCodeList);
//-- convet to sjis

    // UTF BOM
    var bom = new Uint8Array([0xEF, 0xBB, 0xBF]);
    // リンククリエイト
    var downloadLink = document.createElement("a");
    downloadLink.download = filename + ".csv";
    // ファイル情報設定
    downloadLink.href = URL.createObjectURL(new Blob([uInt8List], { type: "text/csv; charset=SJIS" }));
    downloadLink.dataset.downloadurl = ["text/csv; charset=SJIS", downloadLink.download, downloadLink.href].join(":");
    // イベント実行
    downloadLink.click();
}
</script>

<form name="testForm" action="" method="post">
	<input type="hidden" name="export" value="csv">
	<input type="submit" value="CSV データ検索"><br /><br />
	[export_csv]
</form>
