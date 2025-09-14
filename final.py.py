import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.mumbaionlineflorists.com/flowers/rose.asp"

r = requests.get(url)

with open ("test.html","w", encoding='utf-8') as f:
    f.write(r.text)
    
htmlcontent = r.content

soup = BeautifulSoup(htmlcontent,'html.parser')

product_divs = soup.find_all("div",class_="single-product")

descriptions = []

for div in product_divs:
    desc_tag = div.find('li', class_="desc")
    description = desc_tag.get_text(strip=True) if desc_tag else "N/A"
    descriptions.append(description)
    
print(descriptions)
    
prices = []

for div in product_divs:
    price_tag = div.find('li',class_="price")
    price = price_tag.get_text(strip=True) if price_tag else "N/A"
    prices.append(price)
    
print(prices)

links = []
for div in product_divs:
    link_tag = div.find('a', href=True) 
    link = link_tag['href'] if link_tag else "N/A"
    links.append(link)
    
print(links)

df = pd.DataFrame({"Product Description":descriptions, "Prices":prices,"Product Links":links})
print(df)


df.to_csv("Product_deatils.csv")
    
