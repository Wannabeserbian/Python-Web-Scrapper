import requests
import csv
import time

from bs4 import BeautifulSoup as bs


url = requests.get('https://tradingeconomics.com/country-list/rating')
soup = bs(url.content,"html.parser")
timestr = time.strftime("%Y%m%d-%H%M%S")
filename = 'scraped-data.csv'
csv_writer = csv.writer(open(filename,'w'))
heading = soup.find('h1')

print(heading.text)


for table_row in soup.find(id="country-ratings").find_all('tr'):
    table_data = []

    for table_header in table_row.find_all('th'):
        table_data.append(table_header.text)

    if(table_data):
        print("Inserting table headers: {}".format(','.join(table_data)))
        csv_writer.writerow(table_data)
        continue

    for table_row_data in table_row.find_all('td'):
        table_data.append(table_row_data.text.strip())

    if (table_data):
        print("Inserting table row data: {}".format(','.join(table_data)))
        csv_writer.writerow(table_data)
        continue