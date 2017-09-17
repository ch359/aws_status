import sys
import time

import requests
from bs4 import BeautifulSoup
from termcolor import colored

"""Alert when North Virginia server on AWS has a status other than nominal."""


def scraping():
    """Scrape the relevant part of page and format accordingly."""
    page = requests.get('http://status.aws.amazon.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.contents[2]
    body = body.find(id='NA_block').get_text()
    body = body.split(sep="\n")
    status = [(body[body.index(b)], body[body.index(b) + 1]) for b in body if '(N. Virginia)' in b]
    return status


def alert(status):
    """Taking the scraped page as input, print an alert if status is anything other than nominal."""
    if not status:
        sys.exit("Cannot find N. Virginia status. Perhaps the page format has changed?")
    errors = [row for row in status if 'Service is operating normally' not in row[1]]
    if not errors:
        print('\n', time.strftime('%H:%M:%S'), 'All services are operating normally.')
    elif errors:
        print('\n', colored(time.strftime('%H:%M:%S'), 'red'), colored('Errors have been detected with the following '
                                                                       'services: ', 'red'))
        for row in errors:
            print(' ', row[0], ' - ', row[1])


while True:
    alert(scraping())
    time.sleep(120)

# soup = BeautifulSoup(open('aws.htm'), 'html.parser') <-- This code can be used to test against a local and editable
# copy of the page to simulate failing services. Comment out the requests.get line above to avoid pointlessly calling
# the live page.
