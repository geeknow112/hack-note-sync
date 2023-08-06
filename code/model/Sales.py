class Sales:
	def __init__(self):
		self._name = 'yc_sales'

	def getTableName(self):
		return self._name

	def getCurUser(self):
		# wp_get_current_user() のPython版を使用してください
		cur_user = wp_get_current_user()
		return cur_user

	def getValidElement(self, step_num=None):
		messages = {
			'name.required': 'ユーザー名を入力してください',
			'name.string': '正しい形式で入力してください',
			'name.max': '文字数をオーバーしています。',
			'email.required': 'メールアドレスを入力してください。',
			'email.email': '正しい形式でメールアドレスを入力してください',
			'email.max': '文字数をオーバーしています。',
			'email.unique': '登録済みのユーザーです',
			'password.required': 'パスワードを入力してください',
			'password.min': 'パスワードは8文字以上で入力してください。',
			'password.confirmed': 'パスワードが一致しません。',
		}

		step1 = {
			'rules': {
				'apply_service': 'required|max:100',
				'apply_plan': 'required|max:100',
				'biz_fg': 'required|max:100',
				'biz_number': 'required|regex:/^[0-9]{13}+$/i',
				'company_name': 'required|max:100',
				'company_name_kana': 'required|max:100|regex:/^[ァ-ヶｦ-ﾟー]+$/u',
				'zip': 'required|max:100',
				'pref': 'required|max:100',
				'addr': 'required|max:100',
				'addr2': 'required|max:100',
				'addr3': 'max:100',
				'addr_kana': 'required|max:100|regex:/^[ァ-ヶｦ-ﾟー]+$/u',
				'tel': 'required|max:100',
				'fax': 'max:100',
				'est_dt': 'required|max:100',
				'num_employ': 'required|max:100',
				'capital': 'required|max:100',
				'annual_sales': 'max:100',
				'goods_class': 'required|max:100',
				'goods': 'required|max:100',
				'delivery_company': 'max:100',
				'url': 'max:100',
				# 'name': 'required|max:2',
				# 'email': 'required|email',
				# 'password': 'required|min:6',
				# 'confirm_password': 'required|same:password',
				# 'avatar': 'required|uploaded_file:0,500K,png,jpeg',
				# 'skills': 'array',
				# 'skills.*.id': 'required|numeric',
				# 'skills.*.percentage': 'required|numeric'
			},
			'messages': messages
		}

		step2 = {
			'rules': {
				'tank': 'required|max:100',
				'lot': 'required|max:100',
			},
			'messages': messages
		}

		if step_num is None or step_num == 1:
			return step1
		elif step_num == 2:
			return step2

def get_list(get=None, un_convert=None):
	get = get or {}
	cur_user = wp_get_current_user()
	global wpdb

	sql = "SELECT s.*, sc.repeat, sc.period, sc.span, sc.day_of_week, sc.st_dt, sc.ed_dt, g.name as goods_name "
	sql += "FROM yc_sales as s "
	sql += "LEFT JOIN yc_schedule_repeat as sc ON s.id = sc.sales "
	sql += "LEFT JOIN yc_goods as g ON s.goods = g.goods "
	sql += "WHERE s.id is not null "

	if current(cur_user.roles[0]) != 'administrator':
		# sql += "AND ap.mail = '" + cur_user.user_email + "'"
		pass

	if not get.get('action'):
		# sql += "ORDER BY ap.rgdt desc"
		# sql += ";"
		pass
	else:
		if get['action'] == 'search':
			if get['s'].get('no'):
				sql += "AND s.id = '{}' ".format(get['s']['no'])
			if get['s'].get('goods_name'):
				sql += "AND g.name LIKE '{}%' ".format(get['s']['goods_name'])

			if get['s'].get('order_s_dt'):
				sql += "AND s.rgdt >= '{} 00:00:00' ".format(get['s']['order_s_dt'])
			if get['s'].get('order_e_dt'):
				sql += "AND s.rgdt <= '{} 23:59:59' ".format(get['s']['order_e_dt'])

			if get['s'].get('arrival_s_dt'):
				sql += "AND s.arrival_dt >= '{} 00:00:00' ".format(get['s']['arrival_s_dt'])
			if get['s'].get('arrival_e_dt'):
				sql += "AND s.arrival_dt <= '{} 23:59:59' ".format(get['s']['arrival_e_dt'])

			sql += "ORDER BY s.rgdt desc"
			sql += ";"

		else:
			# sql += "AND ap.applicant = '" + prm.post + "';"
			pass

	rows = wpdb.get_results(sql)

	days10 = [
		'2023-07-17', '2023-07-18', '2023-07-19', '2023-07-20', '2023-07-21', '2023-07-22',
		'2022-12-20', '2022-12-21', '2022-12-22', '2022-12-23', '2022-12-24', '2022-12-25'
	]

	e_list = [2, 5]

	for i, row in enumerate(rows):
		if row.repeat_fg:
			if row.period == 1:
				for i in range(1, 6):
					if i in e_list:
						continue
					r = row
					r.id = None
					r.goods_name = 'rep:' + r.goods_name
					date = datetime.datetime.strptime(r.delivery_dt, '%Y-%m-%d')
					date += datetime.timedelta(days=i)
					r.delivery_dt = date.strftime('%Y-%m-%d')
					r.rgdt = None
					r.rep_i = i
					rows.append(r)

	if un_convert:
		dts = []
		for row in rows:
			dts.append(row.delivery_dt)
		rows.sort(key=lambda x: x.delivery_dt, reverse=True)
		return rows
	else:
		tmp = {}
		for row in rows:
			tmp.setdefault(row.delivery_dt, {})[row.id] = row

		result = {}
		for day in days10:
			t = tmp.copy()
			t['delivery_dt'] = day
			result[day] = [t]
			if tmp.get(day):
				for list_ in tmp[day].values():
					result[day].append(list_)

		return result

	def get_detail(get=None):
		get = get or {}
		cur_user = wp_get_current_user()
		global wpdb

		sql = "SELECT s.* FROM yc_sales as s "
		sql += "WHERE s.id = '{}'".format(get.get('sales', ''))

		if current(cur_user.roles[0]) != 'administrator':
			# sql += "AND ap.mail = '" + cur_user.user_email + "'"
			pass

		sql += "LIMIT 1;"
		rows = wpdb.get_results(sql)

		return rows[0] if rows else None


	def get_detail_by_sales_code(sales=None):
		global wpdb

		sql = "SELECT s.* FROM {} as s ".format(get_table_name())
		sql += "WHERE s.id = '{}' ".format(sales)
		sql += "LIMIT 1;"

		rows = wpdb.get_results(sql)
		return rows[0] if rows else None


	def get_detail_by_applicant_code(applicant=None):
		global wpdb
		# $this->vd($applicant);exit;

		sql = "SELECT ap.* FROM {} as ap ".format($wpdb->prefix."applicant")
		sql += "WHERE ap.applicant = '{}' ".format(applicant)
		sql += "LIMIT 1;"

		rows = wpdb.get_results(sql)
		return rows[0] if rows else None


	def get_lot_number_list_by_sales(get=None):
		get = get or {}
		cur_user = wp_get_current_user()
		global wpdb

		sql = "SELECT s.id, s.ship_addr, s.arrival_dt, s.name, g.goods, g.name as goods_name, g.qty as goods_qty, gd.id as lot_tmp_id, gd.lot, gd.tank "
		sql += "FROM yc_sales as s "
		sql += "LEFT JOIN yc_goods as g ON s.goods = g.goods "
		sql += "LEFT JOIN yc_goods_detail as gd on s.id = gd.sales "
		sql += "WHERE s.id is not null "
		sql += "AND gd.id is not null "

		if get.get('action') in ['save', 'confirm', 'edit', 'complete']:
			sql += "AND s.id = {} and g.goods = {} ".format(get.get('sales', 0), get.get('goods', 0))

		rows = wpdb.get_results(sql)

		conv = {}
		for row in rows:
			conv[row.lot_tmp_id] = row

		return conv
