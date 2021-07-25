import requests
import bs4
import lxml

result = requests.get("http://www.example.com")
print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)
print(soup.select('title'))

print(soup.select("p")[0].getText())
print(soup.select('h1'))