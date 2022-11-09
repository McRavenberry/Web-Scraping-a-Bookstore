import requests
from bs4 import BeautifulSoup

catalog = {"title" : " (price)"}

# Loops through the first 50 pages of the books catalog,
# finds the names and prices for all the books under £15
# and adds the information to a dictionary
for page in range(1, 51):
    link = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html")
    
    coffee = BeautifulSoup(link.content, "html.parser")
    books = coffee.find_all(class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")
    
    for i in range(len(books)):
        book = books[i]
        img = book.find("img")
        title = img["alt"]
        price = book.find(class_ = "price_color").get_text()
        price = float(price[1:])
        if price < 15:
            catalog[title] = price


# Takes the dictionary of book titles and prices
# and adds them to a csv file
with open("cheap_books.csv", "w+") as b:
    for i in catalog:
        b.write(f"{i}, £{catalog[i]}\n")
    print("File created")