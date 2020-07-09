import json
import requests
import csv
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache

## What do I want this project to do:


url = "https://www.poetryfoundation.org/poems/48636/the-glass-essay"
poem_page = requests.get(url)

print(type(poem_page))

