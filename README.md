# WebDataScraper

Yahooニュースの最新トピック（タイトルとURL）を取得し、CSVファイルとして保存するPython製のスクレイピングツールです。

## 機能
- YahooニュースのトップピックからタイトルとURLを取得
- タイムスタンプ付きのCSVファイルとして保存
- `requests` と `BeautifulSoup` を使用
- 他サイトへの拡張が容易

## 必要なライブラリ
以下をインストールしてください。

pip install requests beautifulsoup4

## 使い方
Pythonスクリプトを実行します。

python main.py

実行すると、以下のようなCSVファイルが生成されます。

news_20260611_094500.csv

## ファイル構成
WebDataScraper/
├── main.py
├── README.md
└── (生成されたCSVファイル)

## 注意事項
- 本ツールは **ニュース本文の取得は行わず、タイトルとURLのみ** を取得します。
- 学習目的・個人利用を想定しています。
