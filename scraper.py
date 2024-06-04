import requests
from bs4 import BeautifulSoup

def fetch_auction_data():
    url = 'YOUR_AUCTION_WEBSITE_URL'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 根據網站的結構解析需要的數據
    data = []
    for item in soup.select('CSS_SELECTOR_FOR_EACH_ITEM'):
        title = item.select_one('CSS_SELECTOR_FOR_TITLE').text
        price = item.select_one('CSS_SELECTOR_FOR_PRICE').text
        data.append(f"{title}: {price}")

    return data
