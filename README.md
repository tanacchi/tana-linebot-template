# tana-linebot-template
Template of LINE Bot

## Requirements

- Docker & docker-compose
- Heroku CLI

## Getting started

### 初期設定

1. LINE Developers で Messaging API のチャネルを作成
2. Heroku でアプリケーションを作成
3. Heroku の環境変数に `CHANNEL_ACCESS_TOKEN` と `CHANNEL_SECRET` を設定
4. プロジェクト直下に `linebot.env` を置く．内容は以下の通り．
   ```
   CHANNEL_ACCESS_TOKEN=XXXXXXXXX
   CHANNEL_SECRET=XXXXXXXXX
   ```
5. `docker-compose.yml` の subdomain の設定を変更（内容は何でも OK）
6. git の remote に Heroku リポジトリを追加
7. `heroku stack:set container` を実行


### ローカルで実行

1. LINE の webhook を有効にし，Webhook URL に `https://<subdomain>.loca.lt/line` を設定
2. `make up` で起動

### Heroku にデプロイ

1. `make deploy` を実行
2. Webhook URL に Heroku のデプロイ先を設定

## Commands

アプリケーションの操作が大体 `make` で完結するようにしました．
ターミナルで `make 〇〇` と打つと対応するコマンドが実行されます．
`make` まで打って TAB キーを連打すると候補が出ます．

1. `make deploy`
   現在のブランチの最後のコミットの状態を Heroku にデプロイします．
   `main` ブランチにいなくても実行できます．
   デプロイが環境したら自動的にブラウザでアプリケーションにアクセスします．

2. `make up`
   ローカルでアプリケーションを起動します．
   起動したら自動的にブラウザでアクセスします．
   手元でファイルを編集すると自動で反映されます．
   ただし，**ブラウザはリロードする必要があります**．

3. `make log`
   log をターミナル上で流します．

4. `make kill`
   ローカルで起動しているアプリケーションを終了します．

5. `make restart`
   サーバーを再起動します．
   
