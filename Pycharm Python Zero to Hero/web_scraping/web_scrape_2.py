import requests, bs4, lxml
res = requests.get("https://en.wikipedia.org/wiki/Elon_Musk")
soup = bs4.BeautifulSoup(res.text, "lxml")
# Table of contents text
print(list(map(lambda l: l.text, soup.select(".toctext"))))
# Grabbing an image
images = soup.select(".thumbimage")

image_num = 1
for image in images:
    print(image["src"])
    image_link = requests.get("https:"+image["src"])
    with open("new_image_"+str(image_num)+".jpg", "wb") as f:
        f.write(image_link.content)
    image_num += 1
