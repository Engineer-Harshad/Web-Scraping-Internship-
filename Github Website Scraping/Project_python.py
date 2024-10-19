import requests
import pandas as pd
from bs4 import BeautifulSoup
listing = [] 
for i in range(1,21):
    url = "https://github.com/topics/projects?l=python&page=" + str(i)
    r = requests.get(url).text
    soup = BeautifulSoup(r,'lxml') 
    div2 =soup.find('div',class_="col-md-8 col-lg-9")
    articles = div2.find_all('article',class_="border rounded color-shadow-small color-bg-subtle my-4")
    for projects in articles:
        a1 = projects.find('div',class_="px-3").div.div.h3.a.get_text(strip=True)
        a2 = projects.find('a',class_="text-bold wb-break-word").get_text(strip=True)
        half_a3 = projects.find('a',class_="text-bold wb-break-word").get("href")
        full_a3 = "https://github.com" + half_a3 
        span1 = projects.find('span',class_="Counter js-social-count").get_text(strip=True)
        date = projects.find('relative-time',class_="no-wrap").text
        dictionary = {"username":a1, "Repo name":a2,"Repo_link": full_a3,"Reviews":span1, "Date":date}
        listing.append(dictionary)
data = pd.DataFrame(listing)
print(data)
data.to_excel("python.xlsx")