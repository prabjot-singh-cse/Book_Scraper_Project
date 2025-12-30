import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://books.toscrape.com/"
base_url = "https://books.toscrape.com/catalogue/"
all_books = []
while (True):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    print("Books With there prices")
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
        url = base_url+next_page
    else:
        break


file_csv = "books_data.csv"
with open(file_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "Rating", "Image URL"])
    writer.writerows(all_books)


excel_file = "books_data.xlsx"
df = pd.DataFrame(all_books, columns=["Title", "Price", "Rating", "Image URL"])
df.to_excel(excel_file, index=False)

print("DATA SCRAPING COMPLETED SUCCESSFULLY!")
print("CSV file saved as:", file_csv)
print("Excel file saved as:", excel_file)
