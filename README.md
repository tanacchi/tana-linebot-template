# tana-linebot-template
Template of LINE Bot

## Requirements

- Docker & docker-compose
- Heroku CLI

## Getting started

プロジェクト直下に `linebot.env` を置くこと

```
CHANNEL_ACCESS_TOKEN=XXXXXXXXX
CHANNEL_SECRET=XXXXXXXXX
```

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
   
