# ワードクラウド

## 環境構築

* python 3.11.3
* poetry 1.5.1
* MeCab M1 Macはソースビルドしてインストールが必要

```
# python3のパッケージ管理ツール(poetry)のインストール

curl -sSL https://install.python-poetry.org | python3 -

poetry install

poetry run python word-cloud.py
```

