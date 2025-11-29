# ランサムウェア感染の判断材料：確実な特定のための技術的指標

## 即座に確認すべき明確な兆候

![ランサムウェア感染の初期兆候を示すファイル暗号化の様子](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?ixlib=rb-4.0.3&w=1200&q=80)

### ファイル暗号化の痕跡

```bash
find /home -name "*.encrypted" -o -name "*.locked" -o -name "*.crypto" 2>/dev/null | head -20
```

```bash
find /home -type f -mtime -1 -exec file {} \; | grep -v "ASCII\|UTF-8\|executable" | head -10
```

**典型的な暗号化ファイル拡張子：**
- `.locked`, `.encrypted`, `.crypto`
- `.wannacry`, `.locky`, `.cerber`
- ランダム文字列（`.abc123`, `.xyz789`）

### 身代金要求メッセージの存在

```bash
find / -name "*README*" -o -name "*DECRYPT*" -o -name "*RANSOM*" 2>/dev/null
```

```bash
find / -name "*.txt" -exec grep -l "bitcoin\|cryptocurrency\|ransom" {} \; 2>/dev/null
```

**典型的なファイル名：**
- `README_FOR_DECRYPT.txt`
- `HOW_TO_DECRYPT_FILES.html`
- `RANSOM_NOTE.txt`

## システムレベルでの異常検知

![システム監視とプロセス分析のイメージ](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?ixlib=rb-4.0.3&w=1200&q=80)

### プロセス監視による検出

```bash
ps aux --sort=-%cpu | head -10
```

```bash
lsof | awk '{print $2}' | sort | uniq -c | sort -nr | head -10
```

```bash
ps aux | grep -E "(crypt|encrypt|ransom)" | grep -v grep
```

### ネットワーク通信の異常

```bash
netstat -tuln | grep ESTABLISHED
```

```bash
ss -tuln | grep :443 | wc -l
```

```bash
netstat -an | grep -E "(9050|9051|9150)"
```

## ファイルシステムの変化パターン

![ファイルシステムの変更を監視する様子](https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&w=1200&q=80)

### 大量ファイル変更の検出

```bash
find /home -type f -mmin -60 | wc -l
```

```bash
find /home -type f -mmin -60 -exec ls -la {} \; | sort -k6,7
```

```bash
find /home -type f -mmin -60 -printf "%TY-%Tm-%Td %TH:%TM %p\n" | sort
```

### ファイル内容の変化確認

```bash
file /home/user/Documents/*.docx | grep -v "Microsoft Word"
```

```bash
for f in /home/user/Documents/*; do
    echo "$f: $(xxd "$f" | head -5)"
done
```

## レジストリ・設定ファイルの改変

![システム設定とレジストリの監視画面](https://images.unsplash.com/photo-1485827404703-89b55fcc595e?ixlib=rb-4.0.3&w=1200&q=80)

### Windowsレジストリの確認

```cmd
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

```cmd
reg query HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

```cmd
reg query HKLM\SOFTWARE /s | findstr /i "ransom\|crypt\|lock"
```

### Linuxシステム設定の確認

```bash
crontab -l | grep -v "^#"
```

```bash
cat /etc/crontab | grep -v "^#"
```

```bash
systemctl list-units --type=service --state=running | grep -v "loaded active running"
```

## ログファイルでの痕跡確認

![ログ分析とセキュリティ監視のダッシュボード](https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&w=1200&q=80)

### システムログの異常パターン

```bash
journalctl --since "1 hour ago" | grep -E "(open|write|rename)" | wc -l
```

```bash
journalctl --since "1 hour ago" | grep -E "Started|Stopped" | tail -20
```

```bash
grep -i "ransom\|encrypt\|crypto" /var/log/syslog /var/log/messages 2>/dev/null
```

### Webサーバーログの確認

```bash
tail -1000 /var/log/apache2/access.log | awk '{print $1}' | sort | uniq -c | sort -nr
```

```bash
grep -E "\.php\?|\.asp\?|cmd=" /var/log/apache2/access.log | tail -20
```

## メモリ・プロセス解析

![メモリ解析とフォレンジック調査のイメージ](https://images.unsplash.com/photo-1544197150-b99a580bb7a8?ixlib=rb-4.0.3&w=1200&q=80)

### メモリダンプでの確認

```bash
for pid in $(ps aux | grep -v grep | awk '{print $2}'); do
    strings /proc/$pid/mem 2>/dev/null | grep -i "ransom\|decrypt\|bitcoin" && echo "PID: $pid"
done
```

```bash
ls -la /proc/*/exe | grep -v "permission denied"
```

## ネットワーク通信の解析

![ネットワークトラフィック分析の様子](https://images.unsplash.com/photo-1461749280684-dccba630e2f6?ixlib=rb-4.0.3&w=1200&q=80)

### 外部通信先の確認

```bash
tail -100 /var/log/syslog | grep dnsmasq | grep -E "\.onion|\.bit"
```

```bash
netstat -an | grep ESTABLISHED | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
```

## 判断基準のチェックリスト

![セキュリティチェックリストと評価基準](https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?ixlib=rb-4.0.3&w=1200&q=80)

### 確実にランサムウェアと判断できる条件
- [ ] 大量ファイルが同時刻に暗号化
- [ ] 身代金要求メッセージの存在
- [ ] ファイル拡張子の一括変更
- [ ] 暗号化プロセスの実行痕跡

### 疑いが強い条件
- [ ] 異常なCPU使用率の継続
- [ ] 大量の外部通信
- [ ] システムファイルの改変
- [ ] バックアップファイルの削除痕跡

### 追加調査が必要な条件
- [ ] 一部ファイルのみ暗号化
- [ ] 明確な身代金メッセージなし
- [ ] 他のマルウェア感染の可能性

## 緊急対応の判断タイミング

![インシデント対応とエスカレーション手順](https://images.unsplash.com/photo-1504639725590-34d0984388bd?ixlib=rb-4.0.3&w=1200&q=80)

**即座に隔離すべき状況：**
1. 身代金メッセージ確認時点
2. 大量ファイル暗号化進行中
3. 暗号化プロセス実行中

**調査継続可能な状況：**
1. 暗号化停止済み
2. 感染範囲限定的
3. バックアップ確保済み

この判断材料により、ランサムウェア感染の確実な特定と適切な初動対応が可能になります。
