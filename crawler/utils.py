import pymysql
from pymilvus import Collection


def save_to_mysql(articles, connection):
    """Saves scraped articles to MySQL database."""
    cursor = connection.cursor()
    for article in articles:
        cursor.execute("""
            INSERT INTO articles (title, author, publication_date, abstract)
            VALUES (%s, %s, %s, %s)
        """, (article['title'], article['author'], article['date'], article['abstract']))
    connection.commit()


def save_to_milvus(articles, collection, model):
    """Saves article title embeddings to Milvus."""
    titles = [article['title'] for article in articles]
    embeddings = model.encode(titles)
    data = [embeddings, list(range(len(embeddings)))]
    collection.insert(data)
