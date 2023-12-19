import requests
from bs4 import BeautifulSoup as bs
import time
from rich.console import Console
from rich.table import Table

start_time = time.time()
table1 = Table(show_header=True, header_style='bold')
table1.add_column('Financial instrument')
table1.add_column('Current price')
table1.add_column('Change(%)')
table1.add_column('Open')
table1.add_column('High')
table1.add_column('Low')
table1.add_column('Volume')

pages=[]

for page_number in range(1,50):
    url_start = 'https://www.centralcharts.com/en/price-list-ranking/'
    url_end = 'ALL/asc/ts_19-us-nasdaq-stocks--qc_1-alphabetical-order?p='
    url = url_start + url_end + str(page_number)
    pages.append(url)

values_list = []
for page in pages:
    webpage = requests.get(page)
    soup = bs(webpage.text,'html.parser')

    stock_table  = soup.find('table',class_='tabMini tabQuotes')
    tr_tag_list = stock_table.find_all('tr')

    for tr_tag in tr_tag_list:
        td_tag_list = tr_tag.find_all('td')
        row_values = [] 
        
        for td_tag in td_tag_list[0:7]:
            new_value = td_tag.text.strip()
            row_values.append(new_value)
        table1.add_row(*row_values)
        values_list.append(row_values)
console = Console()
console.print(table1)
print('%s seconds'%(time.time()-start_time))