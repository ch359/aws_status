import requests
from bs4 import BeautifulSoup

page = requests.get('http://status.aws.amazon.com/')
soup = BeautifulSoup(page.content, 'html.parser')
body = soup.contents[2]
body = body.find(id='NA_block')
# print(body.prettify)
thead = body.thead
print(thead)
thead.decompose()
thead = body.thead
print(thead)
thead.decompose()
tbody = body.tbody
print(tbody)
tbody.decompose()
table = body.table
print(table)
table.decompose()

print('The revised body: ', body.contents)
# print('The get text version: ', body.get_text)
print('After find ID ', type(body))
body = body.find_all('td')
print('After find_all ', type(body))



# new_body = [body.find_all('bb top pad8', 'bb pad8') for b in body]
# body = body.find_all('td')
print(type(body))
# print(new_body)

# print(body)
# for b in body:
#     print('printing, biatches ', b)
