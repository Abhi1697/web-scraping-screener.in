from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.screener.in/screens/357649/all-listed-companies/'
source = requests.get(url)
soup = BeautifulSoup(source.text, "lxml")
#print(soup)


table = soup.find('table')
headers = table.find_all('th')[0:11] #table had headers after each 11 inputs
table_headers = [" ".join(title.text.replace('\n', '').split()) for title in headers]
#print(table_headers)

df = pd.DataFrame(columns=table_headers)

#total number of pages are 193
for i in range(2,194):
    column_data = table.find_all('tr')
    for cdata in column_data:
        row_data = cdata.find_all('td')
        individual_row_data = [data.text.strip() for data in row_data]
        try:
            length = len(df)
            df.loc[length] = individual_row_data
        except Exception:
            pass

    np = 'https://www.screener.in/screens/357649/all-listed-companies/?page=' + str(i)
    url = np
    source = requests.get(url)
    soup = BeautifulSoup(source.text, "lxml")

df.to_csv(r'C:\Users\abhir\PycharmProjects\WebScraping\MarketListedCompaniesIndia.csv')