#GOAL: Get title of every book with a 2 star rating
import requests, bs4

two_star_titles = []

for page_num in range(1,51):
    print(f"Scraping page {page_num}...")
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    new_url = base_url.format(page_num)
    res = requests.get(new_url)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    products = soup.select(".product_pod")
    for p in products:
        if p.select(".star-rating.Two"):
            title = p.select("a")[1]["title"]
            two_star_titles.append(title)
print("{} 2 star books".format(len(two_star_titles)))
print("The books:", two_star_titles)