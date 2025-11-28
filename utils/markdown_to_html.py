#!/usr/bin/env python3
"""
MarkdownをHTMLに変換してWordPressに投稿
"""

import re

def markdown_to_html(markdown_text):
    """基本的なMarkdown記法をHTMLに変換"""
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

# テスト
if __name__ == "__main__":
    test_markdown = """
# テストタイトル

## セクション1

これは**太字**のテストです。`インラインコード`もあります。

- リスト項目1
- リスト項目2
- リスト項目3

```python
def hello():
    print("Hello World")
```

通常の段落です。
"""
    
    html_result = markdown_to_html(test_markdown)
    print("変換結果:")
    print(html_result)
