<!-- Banner -->
<p align="center">
  <img src="https://img.shields.io/badge/Book%20Store%20Web%20Scraper-Python-blueviolet?style=for-the-badge&logo=python&logoColor=white" />
</p>

<h1 align="center">📚 Book Store Web Scraper</h1>

<p align="center">
  <b>Automated Data Extraction from BooksToScrape ⚙️📊</b> <br>
  <i>Developed by Prabjot Singh | Python & DSA Enthusiast</i>
</p>

---

## 🚀 Project Overview  
This project automatically extracts data from a book-selling website  
and stores it in **CSV** and **Excel** format using Python.

📌 Extracted Information:
- 📘 Book Titles  
- 💷 Price  
- ⭐ Ratings  
- 🖼 Image URLs  

This automation helps avoid **time-consuming manual data collection** and is useful for  
market analysis, academic research & data analytics.

---

## 🧠 Technologies Used  
| Tool | Purpose |
|------|---------|
| Python | Main programming language |
| Requests | Fetch webpage |
| BeautifulSoup | Web Scraping & HTML Parsing |
| Pandas | Excel Output |
| CSV | Structured Storage |
| VS Code | IDE |

---

## 📂 Output Files
✔ books_data.csv  
✔ books_data.xlsx  
✔ Web Scraper Code (book_scraper.py)  
✔ Internship Report (PDF + DOCX)

---

## 🧩 Code Demonstration

```python
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://books.toscrape.com/"
base_url = "https://books.toscrape.com/catalogue/"
all_books = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.find("p", class_="star-rating")["class"][1]
        img = book.find("img")["src"].replace("../", "")
        img_link = "https://books.toscrape.com/" + img
        all_books.append([title, price, rating, img_link])

    nxt = soup.find("li", class_="next")
    if nxt:
        next_page = nxt.find("a")["href"]
        url = base_url + next_page
    else:
        break

csv_file = "books_data.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Rating", "Image URL"])
    writer.writerows(all_books)

excel_file = "books_data.xlsx"
df = pd.DataFrame(all_books, columns=["Title", "Price", "Rating", "Image URL"])
df.to_excel(excel_file, index=False)
