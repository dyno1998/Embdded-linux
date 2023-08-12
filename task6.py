import requests
from bs4 import BeautifulSoup
url = 'https://www.coindesk.com/price/bitcoin'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
price_element = soup.find(class_='price-large')
bitcoin_price = price_element.text.strip()
print(f"Current Bitcoin Price: {bitcoin_price}")
