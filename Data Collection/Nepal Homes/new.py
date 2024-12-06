import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

baseurl="https://www.nepalhomes.com"
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

lisiting_links=[]
for i in range(330):
    response=requests.get(f'https://www.nepalhomes.com/search?find_property_purpose=5db2bdb42485621618ecdae6&find_property_category=5d660cb27682d03f547a6c4a&page={i}&sort=1',
                                 headers=headers)

    soup=BeautifulSoup(response.content,'html.parser')
    lisitng=soup.find_all('div',class_='property__card property__card-type-sd property__card-type-sd-xl')

    for list in lisitng:
        for link in list.find_all('a',target='_blank',href=True):
            lisiting_links.append(baseurl+link["href"])

print(lisiting_links)

test='https://www.nepalhomes.com/detail/bungalow-house-for-sale-NH24455'

alldet=[]

for link in tqdm(lisiting_links, desc="Processing Listings", unit="link"):
    response=requests.get(link,headers=headers)

    soup=BeautifulSoup(response.content,'html.parser')

    try:
        price=soup.find('p',class_='price m-0').text
    except:
        price="Missing"
    try:
        location=soup.find('p',class_='location').text
    except:
        location="error"
    overview=[]

    #we are searcing for all the <ul> with class'list-overview'
    list_overview=soup.find('ul',class_='list-overview')
        #this will find the all <li> from thet page.

    if list_overview:
        list_features=list_overview.find_all('li')

        for feature in list_features:
            a=feature.find('div',class_='excerpt')

            h3_tag=a.find('h3') #this will capture the heading of feature with H3 tag
            h5_tag=a.find('h5') #this will capture the result  of heading with H5 tag

            head=h3_tag.text  #this will convert h3 tag into text
            result=h5_tag.text #this will convert h5 tag into text

            overview.append(f'{head}-{result}')

        det={
            'price':price,
            'location':location,
            'features':overview
        }

        alldet.append(det)
    else:
        overview='error'

print('half way done.')
import pandas as pd

dataset=pd.DataFrame(alldet)
dataset.to_csv("nepal_homes.csv")