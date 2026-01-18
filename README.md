# Benchlet
## 1. コンセプト

### サービス概要

Benchletは、作業用ツールをまとめて動かす“ローカル運用ポータル”です。
外部公開はNGINXの1ポートに集約し、内部はDocker Composeの同一ネットワークで連携します。

### 背景（短い版）

* レガシー機器の手順・根拠・再現性が散らばりやすい
* 自動化は進んだが、実行・ログ確認・品質切り分けが依然重い
* オフライン前提の現場では、持ち運べて確実に回る仕組みが必要

詳細は `docs/CONCEPT.md` を参照してください。

### できること

* marimoで手順書/ノートブックを実行（`notebooks/` 配下のみ参照）
* NocoDBでデータ管理（UIとAPI）
* Filebrowserで成果物/ファイル共有
* ポータルページから各ツールへ導線を提供

### まだやっていないこと

* Ansibleの実行管理、job_id整理、差分比較などの運用機能は未実装
* 成果物の自動収集・証跡化・判定の仕組みは今後の課題

## 2. 利用コンポーネント

* NGINX: リバースプロキシ + ポータルページ
* NocoDB: データ管理（UI/API）
* Filebrowser: ファイル共有
* marimo: 手順書/ノートブックの実行環境
* Docker Compose: 起動/停止のオーケストレーション

---
# Docker Compose
```shell
docker compose up -d --build
```

## 停止
```shell
docker compose down
```

## アクセス
- Portal: http://localhost/
- NocoDB: http://localhost/nocodb/
- Filebrowser: http://localhost/filebrowser/
- marimo: http://localhost/marimo/

## notebooks配置
- `notebooks/` 配下のみを marimo から参照できます。

## OSSライセンスについて
- このリポジトリは設定ファイルと自作スクリプトのみで構成しています。
- 利用しているOSS（NocoDB / marimo / Filebrowser / nginx）はそれぞれライセンスが別です。
- 公開・配布・商用利用の前に、各公式ドキュメントのライセンス条件を確認してください。

## リバプロの注意
- サブパス運用のため、NGINX側で `X-Forwarded-Prefix` と `proxy_redirect` を付与しています。
