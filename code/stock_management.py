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
