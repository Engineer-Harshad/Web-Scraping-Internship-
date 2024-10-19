import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
trustpilot = pd.DataFrame()
for i in range(1,4):
    url = "https://www.trustpilot.com/categories/energy_heating?page={}".format(i)
    webpage = requests.get(url).text
    soup = BeautifulSoup(webpage,'lxml')
    name = []
    website = []
    score = []
    reviews = []
    services = []
    companies = soup.find_all('div',class_="paper_paper__1PY90 paper_outline__lwsUX card_card__lQWDv card_noPadding__D8PcU styles_wrapper__2JOo2")
    for company in companies:
        try:
            name.append(company.find('p',class_="typography_heading-xs__jSwUz typography_appearance-default__AAY17").text.strip())
            website.append(company.find('p', class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_websiteUrlDisplayed__QqkCT").text.strip())
            rev_score = company.find('p', class_="typography_body-m__xgxZ_ typography_appearance-subtle__8_H2l styles_ratingText__yQ5S7").text.strip()
            s1 = slice(11,14)
            s2 = slice(15,35)
            score.append(rev_score[s1])
            reviews.append(rev_score[s2])
            services.append(company.find('div', class_="styles_wrapper___E6__ styles_categoriesLabels__FiWQ4 styles_desktop__U5iWw").text.strip()) 
        except:
            name.append(np.nan)
            website.append(np.nan)
            score.append(np.nan)
            reviews.append(np.nan)
            services.append(np.nan)    
    d = {'Name':name, 'Website':website, 'Score':score, 'Reviews':reviews, 'Services':services}
    df = pd.DataFrame(d)
    trustpilot = trustpilot.append(df, ignore_index=True)
    trustpilot.to_excel("trustpilot.xlsx")
