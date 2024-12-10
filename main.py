from crawler.crawler import scrape_articles
from embeddings.embedded_articles import generate_and_store_embeddings
from query.query_articles import query_articles

if __name__ == "__main__":
    print("Scraping articles...")
    generate_and_store_embeddings()
    print("Querying articles...")
    query_articles("Give me the journals published last week")
