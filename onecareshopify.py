import requests
from bs4 import BeautifulSoup
from telegram import Bot

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# URL of the store page
url = "https://www.onecare.store/store"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

products = []

# TODO: update these class names after inspecting the page
for card in soup.find_all("div", class_="product-card"):
    title = card.find("h2", class_="product-title").text.strip()
    price = card.find("span", class_="price").text.strip()
    link = card.find("a")["href"]
    products.append(f"{title} — {price} — {link}")

bot = Bot(token=BOT_TOKEN)
for p in products:
    bot.send_message(chat_id=CHAT_ID, text=p)
