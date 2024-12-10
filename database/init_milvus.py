from pymilvus import connections, FieldSchema, CollectionSchema, Collection, DataType
import configparser

# Load config
config = configparser.ConfigParser()
config.read('config/config.ini')


def initialize_milvus():
    """Initializes the Milvus collection schema."""
    connections.connect(host=config['milvus']
                        ['host'], port=config['milvus']['port'])

    fields = [
        FieldSchema(name="journal_title",
                    dtype=DataType.FLOAT_VECTOR, dim=384),
        FieldSchema(name="journal_id", dtype=DataType.INT64,
                    is_primary=True, auto_id=True)
    ]
    schema = CollectionSchema(fields, "Articles collection schema")
    collection_name = config['milvus']['collection_name']

    if not Collection.exists(collection_name):
        Collection(name=collection_name, schema=schema)
        print(f"Collection '{collection_name}' created.")
    else:
        print(f"Collection '{collection_name}' already exists.")


if __name__ == '__main__':
    initialize_milvus()
