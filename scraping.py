import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.bps.go.id/id/statistics-table/1/MTUyNSMx/indikator-pendidikan-1994-2023.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table data
rows = soup.find('table').find_all('tr')
data = []
for row in rows:
    cols = row.find_all('td')
    data.append([col.text.strip() for col in cols])

df = pd.DataFrame(data[1:], columns=data[0], dtype=str)

df.to_csv('Indikator Pendidikan, 1994-2023.csv', index=False)