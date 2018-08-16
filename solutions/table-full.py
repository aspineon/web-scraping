import pandas as pd

data = pd.read_html("https://mafudge.github.io/web-scraping/emptable.html")
answer = data[0] # read_html returns a list of all tables on the page.
print(answer)