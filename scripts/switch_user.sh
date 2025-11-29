#!/bin/bash
# GitHub ユーザー切替スクリプト

switch_to_geeknow112() {
    echo "🔄 geeknow112に切替中..."
    git config user.name "geeknow112"
    git config user.email "geeknow112@example.com"
    
    if [ -n "$GITHUB_TOKEN_GEEKNOW112" ]; then
        gh auth logout --hostname github.com 2>/dev/null
        echo "$GITHUB_TOKEN_GEEKNOW112" | gh auth login --with-token
        echo "✅ geeknow112への切替完了"
    else
        echo "❌ GITHUB_TOKEN_GEEKNOW112 環境変数が未設定"
    fi
}

switch_to_przorzcrzc() {
    echo "🔄 przorzcrzc に切替中..."
    git config user.name "przorzcrzc"
    git config user.email "przorzcrzc@example.com"
    
    if [ -n "$GITHUB_TOKEN_PRZORZCRZC" ]; then
        gh auth logout --hostname github.com 2>/dev/null
        echo "$GITHUB_TOKEN_PRZORZCRZC" | gh auth login --with-token
        echo "✅ przorzcrzc への切替完了"
    else
        echo "❌ GITHUB_TOKEN_PRZORZCRZC 環境変数が未設定"
    fi
}

show_status() {
    echo "📊 現在の設定:"
    echo "  Git名前: $(git config user.name)"
    echo "  Gitメール: $(git config user.email)"
    echo "  GitHub CLI:"
    gh auth status 2>/dev/null | grep "account" || echo "    未認証"
}

case "$1" in
    "geeknow112")
        switch_to_geeknow112
        ;;
    "przorzcrzc")
        switch_to_przorzcrzc
        ;;
    "status")
        show_status
        ;;
    *)
        echo "🔧 GitHub ユーザー切替ツール"
        echo ""
        echo "使用方法:"
        echo "  ./switch_user.sh geeknow112"
        echo "  ./switch_user.sh przorzcrzc"
        echo "  ./switch_user.sh status"
        echo ""
        echo "必要な環境変数:"
        echo "  GITHUB_TOKEN_GEEKNOW112"
        echo "  GITHUB_TOKEN_PRZORZCRZC"
        ;;
esac
