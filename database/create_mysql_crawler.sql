CREATE TABLE articles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT NOT NULL,
    author VARCHAR(255),
    publication_date DATE,
    abstract TEXT
);
