# Docker本番環境デプロイメント完全ガイド：セキュリティとパフォーマンスを両立する実践手法

## はじめに

Docker本番環境でのデプロイメントは、開発環境とは全く異なる課題と要求があります。本記事では、企業レベルでのDocker本番運用において必要不可欠なセキュリティ対策、パフォーマンス最適化、監視体制について、実際の運用経験に基づいた実践的な手法を詳しく解説します。

## 本番環境Docker運用の基本原則

### セキュリティファーストの設計思想

本番環境では、セキュリティが最優先事項となります。以下の原則を必ず守る必要があります：

**最小権限の原則**
```dockerfile
# 悪い例：rootユーザーでの実行
FROM node:18
COPY . /app
WORKDIR /app
RUN npm install
CMD ["npm", "start"]

# 良い例：非特権ユーザーでの実行
FROM node:18-alpine
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001
COPY --chown=nextjs:nodejs . /app
WORKDIR /app
USER nextjs
RUN npm ci --only=production
CMD ["npm", "start"]
```

**イメージの脆弱性スキャン**
```bash
# Trivyを使用した脆弱性スキャン
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image your-app:latest

# 重要度HIGH以上の脆弱性のみ表示
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy image --severity HIGH,CRITICAL your-app:latest
```

### マルチステージビルドによる最適化

本番環境では、イメージサイズとセキュリティ面積の最小化が重要です：

```dockerfile
# マルチステージビルドの実装例
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

FROM node:18-alpine AS runtime
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nextjs -u 1001

WORKDIR /app
COPY --from=builder --chown=nextjs:nodejs /app/node_modules ./node_modules
COPY --chown=nextjs:nodejs . .

USER nextjs
EXPOSE 3000
CMD ["npm", "start"]
```

## 本番環境でのDocker Compose設定

### 環境変数とシークレット管理

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  web:
    image: your-app:${APP_VERSION}
    environment:
      - NODE_ENV=production
      - DATABASE_URL_FILE=/run/secrets/db_url
    secrets:
      - db_url
      - api_key
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
      restart_policy:
        condition: on-failure
        delay: 5s
        max_attempts: 3

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - web

secrets:
  db_url:
    external: true
  api_key:
    external: true

networks:
  default:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16
```

### リバースプロキシとSSL終端

```nginx
# nginx.conf
events {
    worker_connections 1024;
}

http {
    upstream app {
        server web:3000;
        keepalive 32;
    }

    server {
        listen 80;
        server_name your-domain.com;
        return 301 https://$server_name$request_uri;
    }

    server {
        listen 443 ssl http2;
        server_name your-domain.com;

        ssl_certificate /etc/nginx/ssl/cert.pem;
        ssl_certificate_key /etc/nginx/ssl/key.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;

        location / {
            proxy_pass http://app;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_cache_bypass $http_upgrade;
        }
    }
}
```

## パフォーマンス最適化戦略

### リソース制限とモニタリング

```yaml
# リソース制限の詳細設定
services:
  web:
    deploy:
      resources:
        limits:
          cpus: '1.0'
          memory: 1G
          pids: 100
        reservations:
          cpus: '0.5'
          memory: 512M
    ulimits:
      nofile:
        soft: 65536
        hard: 65536
    sysctls:
      - net.core.somaxconn=1024
```

### ヘルスチェックの実装

```dockerfile
# Dockerfileでのヘルスチェック
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1
```

```yaml
# Docker Composeでのヘルスチェック
services:
  web:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### ログ管理とローテーション

```yaml
services:
  web:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
        labels: "production,web"
```

## 監視とアラート体制

### Prometheusメトリクス収集

```yaml
# monitoring/docker-compose.yml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--web.console.libraries=/etc/prometheus/console_libraries'
      - '--web.console.templates=/etc/prometheus/consoles'

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=secure_password
    volumes:
      - grafana_data:/var/lib/grafana

  node-exporter:
    image: prom/node-exporter:latest
    ports:
      - "9100:9100"
    volumes:
      - /proc:/host/proc:ro
      - /sys:/host/sys:ro
      - /:/rootfs:ro
    command:
      - '--path.procfs=/host/proc'
      - '--path.rootfs=/rootfs'
      - '--path.sysfs=/host/sys'

volumes:
  prometheus_data:
  grafana_data:
```

### アプリケーションメトリクスの実装

```javascript
// Node.js アプリケーションでのメトリクス実装
const express = require('express');
const promClient = require('prom-client');

const app = express();

// デフォルトメトリクスを有効化
promClient.collectDefaultMetrics();

// カスタムメトリクス
const httpRequestDuration = new promClient.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code']
});

const httpRequestTotal = new promClient.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code']
});

// ミドルウェア
app.use((req, res, next) => {
  const start = Date.now();
  
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    const labels = {
      method: req.method,
      route: req.route?.path || req.path,
      status_code: res.statusCode
    };
    
    httpRequestDuration.observe(labels, duration);
    httpRequestTotal.inc(labels);
  });
  
  next();
});

// メトリクスエンドポイント
app.get('/metrics', (req, res) => {
  res.set('Content-Type', promClient.register.contentType);
  res.end(promClient.register.metrics());
});

// ヘルスチェックエンドポイント
app.get('/health', (req, res) => {
  res.json({ status: 'healthy', timestamp: new Date().toISOString() });
});
```

## CI/CDパイプラインとの統合

### GitHub Actionsでの自動デプロイ

```yaml
# .github/workflows/deploy.yml
name: Deploy to Production

on:
  push:
    branches: [main]
    tags: ['v*']

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Tests
        run: |
          docker build -t app:test .
          docker run --rm app:test npm test

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Image
        run: docker build -t app:${{ github.sha }} .
      
      - name: Security Scan
        run: |
          docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
            aquasec/trivy image --exit-code 1 --severity HIGH,CRITICAL app:${{ github.sha }}

  deploy:
    needs: [test, security-scan]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Deploy to Production
        env:
          DOCKER_HOST: ${{ secrets.PRODUCTION_DOCKER_HOST }}
          APP_VERSION: ${{ github.sha }}
        run: |
          docker build -t your-registry/app:${{ github.sha }} .
          docker push your-registry/app:${{ github.sha }}
          
          # Blue-Green デプロイメント
          docker-compose -f docker-compose.prod.yml up -d --scale web=6
          sleep 30
          docker-compose -f docker-compose.prod.yml up -d --scale web=3
```

## 災害復旧とバックアップ戦略

### データベースバックアップの自動化

```bash
#!/bin/bash
# backup.sh - データベースバックアップスクリプト

BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
DB_CONTAINER="production_db_1"

# PostgreSQLバックアップ
docker exec $DB_CONTAINER pg_dump -U postgres -d myapp > \
  "$BACKUP_DIR/db_backup_$DATE.sql"

# 古いバックアップの削除（7日以上前）
find $BACKUP_DIR -name "db_backup_*.sql" -mtime +7 -delete

# S3へのアップロード
aws s3 cp "$BACKUP_DIR/db_backup_$DATE.sql" \
  "s3://your-backup-bucket/database/"
```

### 設定ファイルのバージョン管理

```yaml
# docker-compose.backup.yml
version: '3.8'

services:
  backup:
    image: alpine:latest
    volumes:
      - /var/lib/docker/volumes:/backup/volumes:ro
      - ./backups:/backup/output
    command: |
      sh -c "
        tar -czf /backup/output/volumes_$(date +%Y%m%d_%H%M%S).tar.gz \
          -C /backup/volumes .
      "
    deploy:
      restart_policy:
        condition: none
```

## セキュリティ強化策

### ネットワークセグメンテーション

```yaml
# セキュアなネットワーク設定
networks:
  frontend:
    driver: bridge
    internal: false
  backend:
    driver: bridge
    internal: true
  database:
    driver: bridge
    internal: true

services:
  nginx:
    networks:
      - frontend
      - backend
  
  web:
    networks:
      - backend
      - database
  
  db:
    networks:
      - database
```

### シークレット管理の実装

```bash
# Docker Swarmでのシークレット管理
echo "your-secret-value" | docker secret create db_password -
echo "your-api-key" | docker secret create api_key -

# 使用例
docker service create \
  --name web \
  --secret db_password \
  --secret api_key \
  your-app:latest
```

## パフォーマンスチューニング

### カーネルパラメータの最適化

```bash
# /etc/sysctl.conf
net.core.somaxconn = 65535
net.core.netdev_max_backlog = 5000
net.ipv4.tcp_max_syn_backlog = 65535
net.ipv4.tcp_keepalive_time = 600
vm.swappiness = 1
```

### Dockerデーモンの最適化

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ],
  "default-ulimits": {
    "nofile": {
      "Name": "nofile",
      "Hard": 65536,
      "Soft": 65536
    }
  }
}
```

## まとめ

Docker本番環境での運用は、開発環境とは全く異なる複雑さと責任を伴います。本記事で紹介した手法を実践することで：

- **セキュリティリスクの最小化**
- **高可用性の実現**
- **パフォーマンスの最適化**
- **運用コストの削減**

これらを同時に達成できます。特に重要なのは、セキュリティファーストの設計思想と、継続的な監視・改善のサイクルです。

本番環境でのDocker運用は一朝一夕には習得できませんが、段階的に実装していくことで、堅牢で効率的なシステムを構築できます。まずは小規模な環境から始めて、徐々に本格的な本番運用に移行することをお勧めします。

---

*企業レベルでのDocker本番運用には、継続的な学習と改善が不可欠です。最新のベストプラクティスを常にキャッチアップし、セキュリティアップデートを欠かさず適用することが成功の鍵となります。*
