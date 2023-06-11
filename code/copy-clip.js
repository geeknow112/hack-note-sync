<script src="https://lober-env-imp.work/wp-content/plugins/order-export/js/jquery.min.js"></script>
<script src="https://lober-env-imp.work/wp-content/plugins/order-export/js/encoding.min.js"></script>

<script>
function copy_html(num) {
	console.log('test');
	/*
	ad_pop();
	var textarea = document.getElementsByTagName("textarea")[num];
	textarea.select();
	document.execCommand("copy");
	*/
}
function test_copy() {
	var code = $("file-cmds-txt-LC88");
	console.log(code);
	console.log(123);
}
function copy_sheet() {
	var sh = document.getElementsById("sheet")[0];
	sh.select();
	document.execCommand("copy");
}
</script>

<h3>HTML</h3>
<form>

<script src="https://gist.github.com/geeknow112/3d3fbfb942c56392b98e94dd417fd058.js"></script>

<textarea style="width:600px; height:50px;" id="export_html0" name="export_html[]"></textarea>
<input type="button" value="copy" onclick="test_copy();" />
<textarea style="width:600px; height:50px;" id="export_html1" name="export_html[]"></textarea>
<input type="button" value="copy" onclick="copy_html(1);" />
<textarea style="width:600px; height:50px;" id="export_html2" name="export_html[]"></textarea>
<input type="button" value="copy" onclick="copy_html(2);" />
<textarea style="width:600px; height:50px;" id="export_html3" name="export_html[]"></textarea>
<input type="button" value="copy" onclick="copy_html(3);" />
<textarea style="width:600px; height:50px;" id="export_html4" name="export_html[]"></textarea>
<input type="button" value="copy" onclick="copy_html(4);" />
<textarea style="width:600px; height:50px;" id="export_html5" name="export_html[]"></textarea>
<input type="button" value="copy" onclick="copy_html(5);" />

</form>

<!--
<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRXAE7EDWSwDjqv7Qj4QufaEeiGYlmlIkI46yZyeZGeSBzBIyXQMnoDLsOLAV43-_buOlE2YWZzjOHq/pubhtml?widget=true&amp;headers=false" style="width:1000px; height:600px;" id="sheet"></iframe>
<input type="button" value="copy" onclick="copy_sheet();" />
-->

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<script language="javascript" type="text/javascript">
	const url = "https://sheets.googleapis.com/v4/spreadsheets/1DOGqoDJ5Byjgx3dw8Wq2Eufu_hwGoIOX_GOmPZDBw2g/values/sample?key=AIzaSyDFIvA2iRqXyEgpbzQqF5Psb6D-lAurye0";
	$.getJSON(url, (data) => {
		//console.log(data['values'][0]);
		var i = 0;
		for (i=0; i<5; i++) {
			var test_data = data['values'][i][1];
			var textarea = document.getElementsByTagName("textarea")[i];
			textarea.innerHTML += test_data;
		}
	});
</script>


<script>
	document.getElementById('ad_area').innerHTML = '';
</script>

<iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vRXAE7EDWSwDjqv7Qj4QufaEeiGYlmlIkI46yZyeZGeSBzBIyXQMnoDLsOLAV43-_buOlE2YWZzjOHq/pubhtml?gid=404801809&amp;single=true&amp;widget=true&amp;headers=false" style="width:800px; height:600px;"></iframe>
