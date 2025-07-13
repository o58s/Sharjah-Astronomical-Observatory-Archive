# Sharjah-Astronomical-Observatory-Archive


This repository contains the backend and database structure for the **Astronomical Image Archive** built during my internship. The goal of the project is to organize, store, and access a decade's worth of celestial image data captured by the Sharjah Astronomical Observatory.

---

## 📂 Repository Structure

```
Sharjah-Astronomical-Observatory-Archive/
│
├── backend/
│   └── insert_images.py           # Script to insert image metadata into MySQL database (⚠️ Do not commit sensitive data)
│
├── database/
│   ├── script.sql                 # MySQL script for creating the database schema
│   └── database structure.png     # Visual diagram of the database structure
│
|
│   
│
├── LICENSE                        # MIT License information
├── README.md                      # You are here
|
```

---

## 🗃️ Database Overview

The database is designed to store and retrieve astronomical images categorized by:

* **Category**: Solar System or Deep Sky
* **Subcategory**: Specific types like Planets, Stars, Nebulae, etc.
* **Object**: The name of the celestial body (e.g., Mars, Sun, M57)
* **Image**: File path, file name, and date of observation

### 💾 Tables Defined:

* `category` — Main category like "Solar System"
* `subcategory` — Subcategory like "Planet"
* `object` — Name of the object (e.g., Jupiter)
* `image` — Contains the image file path, name, and observation date

---

## 🛠️ How to Use

1. **Create the Database:**

```bash
mysql -u your_username -p < database/script.sql
```

2. **Run the Insert Script:**

> ⚠️ **Important:** Before running, make sure you update the `insert_images.py` script with your **local file paths** and **DO NOT commit your actual database credentials** to GitHub.

```bash
python backend/insert_images.py
```

---

## 📸 Database Diagram

![Database Structure](database/database_structure.png)

---

## 🙌 Credits

This project was built as part of my internship at **Sharjah Academy for Astronomy, Space Sciences, and Technology (SAASST)**, supervised by **Dr. Mohammed Talafha**.

---

## 🔐 Disclaimer

This repository only contains the structural and metadata components of the project. No private data or credentials are stored here.

For security:

* ✅ Replace any real credentials or paths in scripts with placeholders (e.g., `YOUR_HOST`, `YOUR_PASSWORD`)
* ✅ Add `.gitignore` entries for sensitive files if needed

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📧 Contact

**Fahad Mohammed**
Computer Science Student @ University of Sharjah
Email: \[fahadmoha2006@gmail.com]
GitHub: \[github.com/o58s]
