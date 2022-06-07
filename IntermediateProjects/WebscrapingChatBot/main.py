from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.ebay.com/globaldeals'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

list = soup.find_all('div', class_='dne-itemtile-detail')

with open('EbayDataSet.csv', mode='w', encoding='utf8', newline='') as f:
    writer = writer(f)
    fields_rows = ['ItemName', 'Price', 'OriginalPrice', 'DiscountPercent'] #headings for the excel sheet/csv file
    writer.writerow(fields_rows) # will write the rows into the csv file

    for item in list:
        item_name = item.find('span', attrs={'class': 'ebayui-ellipsis-2'})
        prices = item.find('span', attrs={'class': 'first'})
        original_price = item.find('span', attrs={'class': 'itemtile-price-strikethrough'})
        discount_percent = item.find('span', attrs={'class': 'itemtile-price-bold'})

        if item_name is not None:
            nodes_name = item_name.text
        else:
            nodes_name = "SPOT LIGHT DEAL"

        if original_price is not None:
            nodes_original_price = original_price.text
        else:
            nodes_original_price = "Cannot find Original Price"

        if prices is not None:
            nodes_price = prices.text
        else:
            nodes_price = "Cannot find Price"

        if discount_percent is not None:
            nodes_discount_percent = discount_percent.text
        else:
            nodes_discount_percent = "No Discounts"

        products_info = [nodes_name,nodes_price, nodes_original_price, nodes_discount_percent]
        writer.writerow(products_info)
