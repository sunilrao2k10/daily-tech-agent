import requests
import json
import xml.etree.ElementTree as ET
from urllib.parse import quote

def search_news(query): 
    url = (
        "https://news.google.com/rss/search?"
        f"q={quote(query)}&hl=en-IN&gl=IN&ceid=IN:en"
    )
    response = requests.get(url, timeout =10)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    articles = []
    for item in root.findall(".//item"):
        title = item.findtext("title")
        link = item.findtext("link")
        pub_date = item.findtext("pubDate")
        description = item.findtext("description")

        articles.append({
            "title": title,
            "link": link,
            "published": pub_date,
        })
    return articles

if __name__ == '__main__':

    queries = [
        "India AI companies",
        "India semiconductor",
        "India cybersecurity"
    ] 

    for query in queries:
        articles = search_news(query)
        print("\n==============================")
        print("SEARCH:", query)
        print("==============================")
        for article in articles[:3]:
            print("\n", article["title"])
            print(article["published"])