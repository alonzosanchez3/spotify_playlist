import datetime as dt
from bs4 import BeautifulSoup
import requests

URL = 'https://www.billboard.com/charts/hot-100/'
date = input("Which year do you want to travel to? Type the date in this format dd/mm/YYYY: ")
print(date)
formatted_date = dt.datetime.strptime(date, '%d/%m/%Y')
string_date = formatted_date.strftime('%Y-%m-%d')
print(string_date)
response = requests.get(url=f"{URL}{string_date}")
soup = BeautifulSoup(response.text, 'html.parser')
chart_results = soup.select('.chart-results-list li h3')
songs_list = [song.text.strip() for song in chart_results]
print(songs_list[0])


