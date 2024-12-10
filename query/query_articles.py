from pymilvus import Collection
from sentence_transformers import SentenceTransformer
import configparser

# Load config
config = configparser.ConfigParser()
config.read('config/config.ini')


def query_articles(query_text):
    """Queries Milvus for relevant articles based on input text."""
    collection = Collection(config['milvus']['collection_name'])
    model = SentenceTransformer('all-MiniLM-L6-v2')

    query_embedding = model.encode([query_text])
    results = collection.search(query_embedding, "journal_title", limit=10)

    for result in results:
        print(f"ID: {result.id}, Score: {result.distance}, Metadata: {result}")
