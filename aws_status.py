import requests
from bs4 import BeautifulSoup

"""Alert when North Virginia server on AWS has a status other than nominal."""


def scraping():
    """Scrape the relevant part of page and format accordingly."""
    page = requests.get('http://status.aws.amazon.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.contents[2]
    body = body.find(id='NA_block').get_text()
    body = body.split(sep="\n")
    for b in body:
        if b == 'Amazon API Gateway (N. Virginia)':
            index = body.index(b)
            server = body[index]
            status = body[index + 1]
            return server, status


def alert(arg):
    """Taking the scraped page as input, print an alert if status is anything other than nominal."""
    server, status = arg
    if status != 'Service is operating normally':
        print(server, ' - Shit be going down! The detailed status is: ', status)
    else:
        print(server, ' - ', status)


alert(scraping())
