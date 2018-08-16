from bs4 import BeautifulSoup
import requests

response = requests.get("https://mafudge.github.io/web-scraping/empweb.html")
soup = BeautifulSoup(response.text, "lxml")
print(soup)
