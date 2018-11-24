import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    events_html = requests.get('https://www.python.org/events/')
    html = BeautifulSoup(events_html.content, 'html.parser')
    locations = html.select('.event-location')
    for l in locations:
        print(l.text)

