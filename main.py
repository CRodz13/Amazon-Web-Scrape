# Import libraries
from bs4 import BeautifulSoup
import requests
import time
import csv
import datetime
import pandas as pd


# Connect to Website and pull in data

# URL = 'https://www.amazon.com/DAYDAYUP-Carrying-Compatible-Cartridges-Protective-Accessories/dp/B0711K97BS/ref=sr_1_8?crid=26JEONR0EY45P&keywords=nintendo+switch+case&qid=1640791298&sprefix=nintendo+switch+case%2Caps%2C61&sr=8-8'
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
#            "Accept-Encoding": "gzip, deflate, br",
#            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#            "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
# page = requests.get(URL, headers=headers)
# soup1 = BeautifulSoup(page.content, "html.parser")
# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
# title = soup2.find(id='productTitle').get_text(strip=True)
# price = soup2.find(id='priceblock_saleprice').get_text(strip=True)
#
# print(title)
# print(price[1:])
#
# # Create timestamp for your output to track when data was collected
# today = datetime.date.today()
# print(today)
#
# # Create CSV and write headers and data into the file
# header = ['Title', 'Price', 'Date']
# data = [title, price, today]
# #
# with open('AmazonWebScrapeDataset.csv', 'w', newline='', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     writer.writerow(data)
#
# # Pandas Dataframe
# df = pd.read_csv(r'C:\Users\Crod\desktop\amazon-web-scrape\amazonwebscrapedataset.csv')
# print(df)
#
# # Appending data to the csv
# with open('AmazonWebScrapedataset.csv', 'a+', newline='', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(data)

def check_price():
    URL = 'https://www.amazon.com/DAYDAYUP-Carrying-Compatible-Cartridges-Protective-Accessories/dp/B0711K97BS/ref=sr_1_8?crid=26JEONR0EY45P&keywords=nintendo+switch+case&qid=1640791298&sprefix=nintendo+switch+case%2Caps%2C61&sr=8-8'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
               "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').get_text(strip=True)
    price = soup2.find(id='priceblock_saleprice').get_text(strip=True)

    # print(title)
    # print(price[1:])

    # Create timestamp for your output to track when data was collected
    today = datetime.date.today()

    # Create CSV and write headers and data into the file
    header = ['Title', 'Price', 'Date']
    data = [title, price, today]
    #
    # with open('AmazonWebScrapeDataset.csv', 'w', newline='', encoding='UTF8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     writer.writerow(data)

    with open('AmazonWebScrapeDataset.csv', 'a', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)



while(True):
    check_price()
    time.sleep(5)

    df = pd.read_csv(r'C:\Users\crod\desktop\Amazon-Web-Scrape\AmazonWebScrapeDataset.csv')

    print(df)
    check_price()

