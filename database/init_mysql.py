import pymysql
import configparser

# Load config
config = configparser.ConfigParser()
config.read('config/config.ini')


def initialize_mysql():
    """Creates the MySQL database and table schema if not exists."""
    connection = pymysql.connect(
        host=config['mysql']['host'],
        user=config['mysql']['user'],
        password=config['mysql']['password']
    )
    cursor = connection.cursor()
    # Create database
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {config['mysql']['database']}")
    connection.select_db(config['mysql']['database'])
    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title TEXT NOT NULL,
            author VARCHAR(255),
            publication_date DATE,
            abstract TEXT
        )
    """)
    connection.commit()
    connection.close()


if __name__ == '__main__':
    initialize_mysql()
