#!/usr/bin/env python3
"""
英語スラッグ付き記事投稿
"""

import requests
import base64

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

# 投稿データ（英語スラッグ付き）
post_data = {
    'title': '【TradingView】Advanced CSV Data Import Settings and Usage',
    'slug': 'tradingview-advanced-csv-import-guide',  # 英語スラッグ
    'content': '''
# TradingView Advanced CSV Data Import Guide

## Introduction

CSV data import in TradingView is a basic feature, but advanced settings are crucial for efficient analysis. This article explains detailed CSV import procedures and practical usage methods.

## CSV File Preparation

### Required Data Format
```
Date,Open,High,Low,Close,Volume
2024-01-01,100.5,102.3,99.8,101.2,1500000
2024-01-02,101.2,103.1,100.9,102.5,1800000
```

### Data Quality Checkpoints
- Unified date format (YYYY-MM-DD recommended)
- Missing data handling
- Outlier removal
- Timezone confirmation

## Import Procedures

### 1. Dataset Creation
1. Login to TradingView
2. Select "Chart" → "New Chart"
3. Click "+" button at bottom left → "Import Dataset"

### 2. Advanced Settings
- **Delimiter**: Choose from comma, semicolon, tab
- **Date Format**: Auto-detect or manual specification
- **Timezone**: Set according to market
- **Data Frequency**: Daily, hourly, etc.

## Advanced Usage Techniques

### Custom Indicator Integration
```javascript
//@version=5
indicator("Custom CSV Data Analysis", overlay=true)

// Moving average based on imported data
ma20 = ta.sma(close, 20)
plot(ma20, color=color.blue, title="MA20")
```

### Multiple Dataset Comparison
- Simultaneous display of different market data
- Correlation analysis
- Arbitrage opportunity discovery

## Troubleshooting

### Common Errors and Solutions
1. **"Date not recognized"**
   - Unify date format to YYYY-MM-DD
   - Check header row

2. **"Data not displayed"**
   - File size limit (under 5MB)
   - Character encoding (UTF-8 recommended)

3. **"Incorrect price data"**
   - Check decimal point symbol (use period)
   - Unify currency units

## Practical Analysis Examples

### Backtest Data Preparation
```python
import pandas as pd

# CSV data preprocessing
df = pd.read_csv('market_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna()  # Remove missing values
df.to_csv('cleaned_data.csv', index=False)
```

### Performance Analysis
- Return calculation
- Drawdown measurement
- Sharpe ratio calculation

## Summary

Effective use of CSV import in TradingView enables unique analysis. Ensuring data quality and proper settings leads to more accurate investment decisions.

---
*Delivering practical information for corporate investment decision efficiency.*
''',
    'status': 'publish',
    'categories': [954]  # ツールカテゴリー
}

print("🚀 英語スラッグ記事投稿開始")
print(f"📄 タイトル: {post_data['title']}")
print(f"🔗 スラッグ: {post_data['slug']}")

# 投稿実行
response = requests.post(
    f"{WP_URL}/wp-json/wp/v2/posts",
    headers=headers,
    json=post_data
)

if response.status_code == 201:
    result = response.json()
    print("✅ 投稿成功！")
    print(f"🔗 URL: {result['link']}")
    print(f"📊 投稿ID: {result['id']}")
else:
    print(f"❌ 投稿失敗: {response.status_code}")
    print(f"📋 エラー: {response.text}")
