import requests
from bs4 import BeautifulSoup

def get_links(url='https://nuro-lab.com/東京都/'):
    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    links = [link['href'] for link in soup.select('ul.nav > li > a')]
    return links

districts = get_links()

for district in districts:
    areas = get_links('https://nuro-lab.com/' + district)
    for area in areas:
        buildings = get_links('https://nuro-lab.com/' + area)
        for building in buildings:
            print(building)
