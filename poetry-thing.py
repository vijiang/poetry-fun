import requests, json, csv
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache

## What do I want this project to do:

# ------ code for caching ------
FILENAME = "glass_essay_text.json"
PROGRAM_CACHE = Cache(FILENAME)

url = "https://www.poetryfoundation.org/poems/48636/the-glass-essay"
# this url holds anne carson's poem

def access_page_data(url):
    page_data = PROGRAM_CACHE.get(url)
    if not page_data:
        # if page_data does not exist, request to grab its content in text form
        page_data = requests.get(url).text
        PROGRAM_CACHE.set(url, page_data, expire_in_days=60)
    return page_data

poem_page = access_page_data(url)
soup = BeautifulSoup(poem_page, "html.parser")
poem_text = soup.find('div', {'class': 'o-poem'})

all_poem_text = ""
for line in poem_text.strings:
    # print(line)
    all_poem_text+=line

tokenized_poem = all_poem_text.split()
print(tokenized_poem)

count = 0
for item in tokenized_poem:
    if item == " ":
        count+=1
print(count)



