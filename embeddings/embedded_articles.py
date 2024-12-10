from sentence_transformers import SentenceTransformer
from pymilvus import Collection
from crawler.crawler import scrape_articles
from crawler.utils import save_to_milvus, save_to_mysql
from database.init_mysql import initialize_mysql
from database.init_milvus import initialize_milvus
import pymysql
import configparser

# Load config.ini
config = configparser.ConfigParser()
config.read('config/config.ini')


def generate_and_store_embeddings():
    """Scrapes articles, generates embeddings, and stores them in Milvus."""
    articles = scrape_articles()

    # Connect to MySQL
    initialize_mysql()
    mysql_connection = pymysql.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password'],
        database=config['mysql']['database']
    )

    save_to_mysql(articles, mysql_connection)
    mysql_connection.close()

    # Connect to Milvus
    initialize_milvus()
    collection = Collection(config['milvus']['collection_name'])
    model = SentenceTransformer('all-MiniLM-L6-v2')
    save_to_milvus(articles, collection, model)


if __name__ == "__main__":
    generate_and_store_embeddings()
