from bs4 import BeautifulSoup
import requests

source = requests.get("https://jamesclear.com/3-2-1/june-11-2020").text
soup = BeautifulSoup(source, "lxml")

body = soup.find("body")

# Printing Heading
headline = body.div.h2.text
print(headline)

# Print all paragraphs
for words in soup.find_all('p'):
    print(words.text)