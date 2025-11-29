#!/usr/bin/env python3
"""
GitHub CLI ユーザー切替スクリプト
"""

import subprocess
import os
import sys

# ユーザー設定
USERS = {
    'geeknow112': {
        'name': 'geeknow112',
        'email': 'geeknow112@example.com',
        'token_env': 'GITHUB_TOKEN_GEEKNOW112'
    },
    'przorzcrzc': {
        'name': 'przorzcrzc', 
        'email': 'przorzcrzc@example.com',
        'token_env': 'GITHUB_TOKEN_PRZORZCRZC'
    }
}

def run_command(cmd):
    """コマンド実行"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def switch_user(username):
    """ユーザー切替"""
    if username not in USERS:
        print(f"❌ 未知のユーザー: {username}")
        print(f"利用可能: {list(USERS.keys())}")
        return False
    
    user = USERS[username]
    
    print(f"🔄 {username}に切替中...")
    
    # 1. Git設定変更
    print("📝 Git設定更新中...")
    success, _, _ = run_command(f'git config user.name "{user["name"]}"')
    if not success:
        print("❌ Git名前設定失敗")
        return False
        
    success, _, _ = run_command(f'git config user.email "{user["email"]}"')
    if not success:
        print("❌ Gitメール設定失敗")
        return False
    
    # 2. GitHub CLI認証切替
    print("🔑 GitHub CLI認証切替中...")
    
    # ログアウト
    run_command('gh auth logout --hostname github.com')
    
    # トークン取得
    token = os.getenv(user['token_env'])
    if not token:
        print(f"❌ 環境変数 {user['token_env']} が設定されていません")
        return False
    
    # ログイン
    success, _, stderr = run_command(f'echo "{token}" | gh auth login --with-token')
    if not success:
        print(f"❌ GitHub CLI認証失敗: {stderr}")
        return False
    
    print(f"✅ {username}への切替完了")
    return True

def show_current_user():
    """現在のユーザー表示"""
    print("📊 現在の設定:")
    
    # Git設定
    success, name, _ = run_command('git config user.name')
    if success:
        print(f"  Git名前: {name.strip()}")
    
    success, email, _ = run_command('git config user.email')
    if success:
        print(f"  Gitメール: {email.strip()}")
    
    # GitHub CLI
    success, output, _ = run_command('gh auth status')
    if success and 'account' in output:
        lines = output.split('\n')
        for line in lines:
            if 'account' in line:
                print(f"  GitHub CLI: {line.strip()}")
                break

def main():
    if len(sys.argv) < 2:
        print("🔧 GitHub ユーザー切替ツール")
        print("\n使用方法:")
        print("  python3 switch_github_user.py <username>")
        print("  python3 switch_github_user.py status")
        print(f"\n利用可能ユーザー: {list(USERS.keys())}")
        return
    
    command = sys.argv[1]
    
    if command == 'status':
        show_current_user()
    elif command in USERS:
        switch_user(command)
    else:
        print(f"❌ 不明なコマンド: {command}")
        print(f"利用可能: {list(USERS.keys())} または status")

if __name__ == "__main__":
    main()
