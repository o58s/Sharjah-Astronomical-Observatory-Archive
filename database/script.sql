CREATE DATABASE IF NOT EXISTS website_data;
USE website_data;

CREATE TABLE category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE subcategory (
    subcategory_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (category_id, name)
);

CREATE TABLE object (
    object_id INT AUTO_INCREMENT PRIMARY KEY,
    subcategory_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    UNIQUE (subcategory_id, name)
);

CREATE TABLE image (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    object_id INT NOT NULL,
    file_path TEXT NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    date_taken DATE,
    FOREIGN KEY (object_id) REFERENCES object(object_id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

