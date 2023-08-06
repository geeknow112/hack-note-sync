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
