import mysql.connector
import os
from datetime import datetime

# IDs should be fetched dynamically in production, hardcoded here for simplicity
category_id = 1
subcategory_id = 1
object_id = 1

# 📂 Define the paths to your image folders
# IMPORTANT: Replace these with your actual local paths (but don't commit them to GitHub)
images_folder_path = r"/path/to/your/images_folder"
base_folder_path = r"/path/to/your/base_folder"

# 🔐 Connect to the MySQL database
# NEVER upload real credentials to public repositories
conn = mysql.connector.connect(
    host = "your_host",        # e.g., "localhost"
    user = "your_username",    # e.g., "root"
    password = "your_password",
    database = "website_data"
)

# Initialize cursor to interact with the database
cursor = conn.cursor()

# 🔄 Loop through each image in the folder
for file in os.listdir(images_folder_path):
    full_path = os.path.join(images_folder_path, file)

    # Get relative path to store in DB
    image_path = os.path.relpath(full_path, base_folder_path)

    # Extract last modified time of file and convert it to a date
    modified_time = os.path.getmtime(full_path)
    date_taken = datetime.fromtimestamp(modified_time).date()

    # 📥 Insert image metadata into the `image` table
    cursor.execute(
        "INSERT INTO image (object_id, file_path, file_name, date_taken) VALUES (%s, %s, %s, %s)",
        (object_id, image_path, file, date_taken)
    )

# ✅ Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()

print("Image inserted successfully!")
