#!/bin/bash

# Step 1: Initialize MySQL database
echo "Initializing MySQL database..."
python3 database/init_mysql.py
if [ $? -ne 0 ]; then
  echo "MySQL initialization failed. Exiting."
  exit 1
fi

# Step 2: Initialize Milvus collection
echo "Initializing Milvus collection..."
python3 database/init_milvus.py
if [ $? -ne 0 ]; then
  echo "Milvus initialization failed. Exiting."
  exit 1
fi

# Step 3: Scrape articles and store data
echo "Scraping articles and storing data in MySQL and Milvus..."
python3 embeddings/embed_articles.py
if [ $? -ne 0 ]; then
  echo "Article scraping and storage failed. Exiting."
  exit 1
fi

# Step 4: Query Milvus for testing
echo "Querying Milvus for articles..."
python3 query/query_articles.py "Give me the journals published last week"
if [ $? -ne 0 ]; then
  echo "Querying failed. Exiting."
  exit 1
fi

echo "All tasks completed successfully!"
