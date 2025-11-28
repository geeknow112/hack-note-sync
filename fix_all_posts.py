#!/usr/bin/env python3
"""
全既存投稿のMarkdownを一括修正
"""

import requests
import base64
import re

# 設定
WP_URL = "https://hack-note.com"
USERNAME = "myu"
PASSWORD = "QEBX aUmp 8ljk yXr6 OTyQ UjCd"

# 認証ヘッダー
credentials = f"{USERNAME}:{PASSWORD}"
token = base64.b64encode(credentials.encode()).decode()
headers = {
    'Authorization': f'Basic {token}',
    'Content-Type': 'application/json'
}

def markdown_to_html(markdown_text):
    """MarkdownをHTMLに変換"""
    html = markdown_text
    
    # 見出し変換
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # コードブロック変換
    html = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    
    # インラインコード変換
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # 太字変換
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # リスト変換
    lines = html.split('\n')
    in_list = False
    result_lines = []
    
    for line in lines:
        if re.match(r'^- ', line):
            if not in_list:
                result_lines.append('<ul>')
                in_list = True
            item = re.sub(r'^- (.+)', r'<li>\1</li>', line)
            result_lines.append(item)
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            result_lines.append(line)
    
    if in_list:
        result_lines.append('</ul>')
    
    # 段落変換
    html = '\n'.join(result_lines)
    paragraphs = html.split('\n\n')
    html_paragraphs = []
    
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            p = f'<p>{p}</p>'
        html_paragraphs.append(p)
    
    return '\n\n'.join(html_paragraphs)

# 修正対象の投稿とファイル
posts_to_fix = [
    {
        'id': 14999,
        'file': None,  # テスト記事は直接HTML
        'content': '''
<h1>GitHub同期システムテスト</h1>

<p>このテスト記事は、GitHubリポジトリからWordPressへの自動同期システムの動作確認用です。</p>

<h2>システムの特徴</h2>
<ul>
<li>GitHubにコミットすると自動でWordPressに投稿</li>
<li>Markdownファイルから自動でHTML変換</li>
<li>カテゴリーとタグの自動分類</li>
</ul>

<h2>技術スタック</h2>
<ul>
<li>Python</li>
<li>WordPress REST API</li>
<li>GitHub Actions</li>
</ul>

<p><em>自動投稿システムによる投稿テストです。</em></p>
'''
    },
    {
        'id': 15001,
        'file': 'articles/github_vscode_collaboration_guide.md'
    }
]

print("🔧 全投稿のMarkdown一括修正開始")

for post in posts_to_fix:
    print(f"\n📝 投稿ID {post['id']} を修正中...")
    
    if post['file']:
        # ファイルから読み込み
        with open(post['file'], 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        html_content = markdown_to_html(markdown_content)
    else:
        # 直接HTML
        html_content = post['content']
    
    # 投稿更新
    update_data = {
        'content': html_content
    }
    
    response = requests.post(
        f"{WP_URL}/wp-json/wp/v2/posts/{post['id']}",
        headers=headers,
        json=update_data
    )
    
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 修正成功: {result['link']}")
    else:
        print(f"❌ 修正失敗: {response.status_code}")
        print(f"📋 エラー: {response.text}")

print("\n🎉 全投稿のMarkdown修正完了")
