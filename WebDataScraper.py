import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# -----------------------------
# WebDataScraper - News Scraper
# -----------------------------

URL = "https://news.yahoo.co.jp/topics/top-picks"  # 取得先（例：Yahooニュース）
HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_news():
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select("a.sc-dRFtgE")  # Yahooニュースのタイトル要素（2026年時点）

    news_list = []
    for item in items:
        title = item.get_text(strip=True)
        link = item.get("href")
        news_list.append([title, link])

    return news_list


def save_to_csv(news_list):
    filename = f"news_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "URL"])
        writer.writerows(news_list)

    print(f"Saved: {filename}")


def main():
    print("Fetching latest news...")
    news = fetch_news()
    save_to_csv(news)
    print("Done.")


if __name__ == "__main__":
    main()
