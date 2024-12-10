import requests
from bs4 import BeautifulSoup


def scrape_articles():
    """Scrapes articles from the Nature Oncology page."""
    url = "https://www.nature.com/subjects/oncology"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for article in soup.find_all("article"):
        title = article.find("h3").text.strip()
        author = article.find("a", class_="c-author-list__link").text.strip(
        ) if article.find("a", class_="c-author-list__link") else None
        date = article.find("time")["datetime"] if article.find(
            "time") else None
        abstract = article.find("p", class_="c-card__summary").text.strip(
        ) if article.find("p", class_="c-card__summary") else None
        articles.append({"title": title, "author": author,
                        "date": date, "abstract": abstract})

    return articles
