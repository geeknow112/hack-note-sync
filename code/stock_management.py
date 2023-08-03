import os
from stock_management.model.model import *
from stock_management.model.Shop import *
from stock_management.model.Applicant import *
from stock_management.model.Sales import *
from stock_management.model.Goods import *
from stock_management.model.Customer import *
from phpoffice.phpspreadsheet import Spreadsheet
from phpoffice.phpspreadsheet.writer import Xlsx

import pytz
from datetime import datetime

class StockManagement:

	def __init__(self):
		self.add_action('admin_menu', self.add_pages)
		self.add_action('admin_menu', self.add_sub_menu)
		# self.add_action('init', self.export_csv)
		# self.add_action('init', self.export_pdf)

	def add_pages(self):
		add_menu_page('在庫/発注予定管理', '在庫/発注予定管理', 'level_8', 'stock-management', self.menu_top, '', 26)

	def add_sub_menu(self):
		cur_user = wp_get_current_user()
	
		if cur_user.roles[0] == 'administrator':
			if cur_user.user_login in ['admin']:
				# 登録画面
				add_submenu_page('stock-management', '商品登録', '🔷商品登録', 'read', 'goods-detail', self.goods_detail)
				add_submenu_page('stock-management', '顧客登録', '🔷顧客登録', 'read', 'customer-detail', self.customer_detail)
				add_submenu_page('stock-management', '注文登録', '🔷注文登録', 'read', 'sales-detail', self.sales_detail)
	
				# 検索画面
				add_submenu_page('stock-management', '商品検索', '🔶商品検索', 'read', 'goods-list', self.goods_list)
				add_submenu_page('stock-management', '顧客検索', '🔶顧客検索', 'read', 'customer-list', self.customer_list)
				add_submenu_page('stock-management', '注文検索', '🔶注文検索', 'read', 'sales-list', self.sales_list)
	
				# その他
				add_submenu_page('stock-management', 'ロット番号登録', 'ロット番号登録', 'read', 'lot-regist', self.lot_regist)
				add_submenu_page('stock-management', '配送予定表③', '配送予定表③', 'read', 'delivery-graph', self.delivery_graph)
				add_submenu_page('stock-management', '日別商品集計', '日別商品集計', 'read', 'sum-day-goods', self.sum_day_goods)
			else:
				self.remove_menus()
		else:
			self.remove_menus()
			add_action('admin_bar_menu', 'remove_admin_bar_menus', 999)
		
	def reload():
	    global _POST
	    global p
	    _POST = {}
	    p = {}
	    # echo '<script type="text/javascript">if (window.name != "any") {window.location.reload();window.name = "any";} else {window.name = "";}</script>'
	
	def confirm():
	    blade = set_view()
	    prm, p, rows = preStepProcess('confirm')
	    echo(blade.run("shop-detail-confirm", rows=rows, prm=prm))
	
	def status():
	    blade = set_view()
	    prm, p, rows, step_num = preStepProcess('confirm')
	    tb = Applicant()
	    status = tb.getStatusForMenu()
	    echo(blade.run("shop-detail-status", status=status, step_num=step_num))
	
	def set_view():
	    views = __DIR__ + '/views'
	    cache = __DIR__ + '/cache'
	    blade = BladeOne(views, cache, BladeOne.MODE_AUTO)
	    return blade
	
	def menu_top():
	    blade = set_view()
	    title = '<p>menu top</p>'
	    echo(blade.run("menu-top", title=title, msg=msg))

	def get_valid_msg(step_num=None):
	    app = get_tb()
	    ve = app.get_valid_element(step_num)
	
	    # rakid
	    validator = Validator()
	    validator.set_messages({
	        # 'required': ':attribute を入力してください',
	        'required': 'を入力してください',
	        'email': ':email tidak valid',
	        'min': 'の文字数が不足しています。',
	        'max': 'が文字数をオーバーしています。',
	        'regex': 'をカタカナで入力してください。',
	        'biz_number': 'は、国税庁が指定する13桁の番号で入力してください。',
	        'goods_image1': 'が選択されていません。',
	        # etc
	    })
	
	    """
	    # 項目コピーのradioにチェックが入ってる場合、rulesを削除してValidation不要にする
	    ve = app.init_validation_rules(_POST, ve)
	
	    # 入力欄「その他」のradioにチェックが入ってる場合、rulesを変更してValidationする
	    ve = app.change_validation_rules(_POST, ve)
	
	    # 必須：商品画像①のvalidation追加
	    if not empty(_FILES) and (step_num == 3):
	        ve = app.change_file_validation_rules(_POST + _FILES, ve)
	    """
	
	    # make it
	    validation = validator.make(_POST + _FILES, ve['rules'], ve['messages'])
	
	    # then validate
	    validation.validate()
	
	    if validation.fails():
	        # handling errors
	        errors = validation.errors()
	        msg = errors.first_of_all()
	    else:
	        # validation passes
	        msg = {'msg': 'success'}
	    
	    return msg
			
	def goods_detail():
	    blade = set_view()
	    get = {}
	    post = {}
	
	    set_tb('Goods')
	    page = 'goods-detail'
	
	    rows = None
	    action = get.get('action')
	    if action == 'regist':
	        tb = Applicant()
	    else:
	        initForm = get_tb().get_init_form()
	        rows = get_tb().get_list()
	        blade.run("goods-detail")
	
	    if action == 'search':
	        tb = Applicant()
	        initForm = tb.get_init_form()
	        rows = tb.get_list(prm)
	        formPage = 'sales-list'
	        blade.run("sales-list", rows=rows, formPage=formPage, initForm=initForm)
	
	    if action == 'confirm':
	        if post:
	            if post['cmd'] == 'cmd_confirm':
	                msg = get_valid_msg()
	                rows = post
	                rows['name'] = post['goods_name']
	                rows['id'] = rows['goods']
	                if rows['goods']:
	                    rows['btn'] = 'update'
	
	                if msg['msg'] != 'success':
	                    rows['messages'] = msg
	        if rows.get('messages'):
	            msg = rows['messages']
	            get['action'] = 'save'
	        else:
	            pass
	        vd([get, post, msg, rows, page])
	        blade.run("goods-detail", rows=rows, get=get, post=post, msg=msg)
	
	    if action == 'complete':
	        prm = tb.get_prm()
	        rows = tb.reg_detail(prm)
	        blade.run("shop-detail-complete", rows=rows, prm=prm)
	
	    if action == 'save':
	        if post:
	            if post['cmd'] == 'save':
	                msg = get_valid_msg()
	                if msg['msg'] == 'success':
	                    rows = get_tb().reg_detail(get, post)
	                    rows['goods_name'] = rows['name']
	                    get['action'] = 'complete'
	                else:
	                    rows = post
	                    rows['name'] = post['goods_name']
	                    rows['messages'] = msg
	        vd(rows)
	        blade.run("goods-detail", rows=rows, get=get, post=post, msg=msg)
	
	    if action == 'edit-exe':
	        if post:
	            if post['cmd'] == 'update':
	                msg = get_valid_msg()
	                if msg['msg'] == 'success':
	                    rows = get_tb().upd_detail(get, post)
	                    rows['goods_name'] = rows['name']
	                    get['action'] = 'complete'
	                else:
	                    rows = post
	                    rows['name'] = post['goods_name']
	                    rows['messages'] = msg
	        vd(rows)
	        blade.run("goods-detail", rows=rows, get=get, post=post, msg=msg)
	
	    if action == 'edit':
	        if get.get('goods'):
	            rows = get_tb().get_detail_by_goods_code(get['goods'])
	            rows['goods_name'] = rows['name']
	            rows['cmd'] = post['cmd'] = 'cmd_update'
	        else:
	            msg = get_valid_msg()
	            rows = post
	            rows['name'] = post['goods_name']
	            if msg['msg'] != 'success':
	                rows['messages'] = msg
	        blade.run("goods-detail", rows=rows, get=get, post=post, msg=msg)
	
	    if action == 'cancel':
	        prm = get
	        del post
	        tb = Applicant()
	        rows = tb.get_detail(prm)
	        p = rows
	        formPage = 'sales-list'
	        blade.run("shop-detail", rows=rows, formPage=formPage, prm=prm, p=p)
	
	    if action == 'preview':
	        print('test preview')
	        app = Applicant()
	        curUser = app.get_cur_user()
	        if curUser['roles'] != 'administrator':
	            applicant = html.escape(get['post'])
	            row = app.get_detail_by_applicant_code(applicant)
	        else:
	            row = None
	        blade.run("preview", row=row, formPage=formPage, prm=prm, p=p)
	
	    if action == 'init-status':
	        prm = get
	        del post
	        applicant = prm['post']
	        tb = Applicant()
	        ret = tb.init_status(applicant)
	        result = 'true' if ret else 'false'
	        print(f'<script>window.location.href = "{home_url()}/wp-admin/admin.php?page=sales-list&init-status={result}";</script>')
		
