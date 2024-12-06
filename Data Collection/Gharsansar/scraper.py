#importing libaries to scess and read website data,
import requests
from bs4 import BeautifulSoup

links=[]   #this list will carry all the href links for htje property of earch page.
for i in range(50):    #this runs forloop across all pages 
    url='https://gharsansarnepal.com/category/home-for-sale-in-kathmandu/buy?page={i}'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    response=requests.get(url,headers=headers)

    soup=BeautifulSoup(response.content,'html.parser')

    listing=soup('div',class_='col-lg-4 col-md-6 col-sm-6 col-12')

    for list in listing:
        for link in list.find_all('a',href=True):
            links.append(link['href'])



alldet=[]  
test='https://gharsansarnepal.com/house-in-kathmandu/1165'  #test link 

for link in links:    #this runs the forloop across all the link that are stored in links list. 

    response=requests.get(link,headers=headers)

    soup=BeautifulSoup(response.content,'html.parser')

    try:          #try scraping price data if not found return missing data
        price=soup.find('div',class_='banner-sub-title').text.split()[-1]
    except:
        price=''

    try:          #try scraping location data if not found return missing data
        location=soup.find('div',class_='overview-sub-title').text.split()[-1]
    except:
        location=''
    locater=soup.find_all('div',class_='contact-list')[1]
    try:          #try scraping land size data if not found return missing data
        land=locater.find_all('li')[6].text.split()
        land_area=" ".join(land[3:])
    except:
        land_area=""

    try:            #try scraping house size data if not found return missing data
        house_size=locater.find_all('li')[7].text.split()
        area=" ".join(house_size[-2:])
    except:
        area=''
    try:             #try scraping property facing data if not found return missing data
        facing=locater.find_all('li')[-2].text.split()[-1]
    except:
        facing=''
    try:             #try scraping no of bedroom data if not found return missing data
        bedroom=locater.find_all('li')[-6].text.split()[-1]
    except:
        bedroom=''
    try:             #try scraping no of bedroom data if not found return missing data
        bathroom=locater.find_all('li')[-3].text.split()[-1]
    except:
        bathroom=''
    try:              #try scraping no of bathroom data if not found return missing data
        livingroom=locater.find_all('li')[-5].text.split()[-1]
    except:
        livingroom=''
    try:               #try scraping no of living room data if not found return missing data
        kitchen=locater.find_all('li')[-4].text.split()[-1]
    except:
        kitchen=''
    try:               #try scraping praking space data if not found return missing data
        parking_tag=locater.find_all('li')[-1].text.split()[3:]
        parking=" ".join(parking_tag)
    except:
        parking=''

    try:               #try scraping road type data if not found return missing data
        road_type=locater.find_all('li')[4].text.split()[-1]
    except:
        road_type=''

    try:               #try scraping road size data if not found return missing data
        road_size=locater.find_all('li')[3].text.split()[-2]
    except:
        road_size=''

    det={                            #this dict will collect the above scraped data into dict
        'price':price,
        'location':location,
        'area':area,
        'facing':facing,
        'no_of_bedroom':bedroom,
        "no_of_bathroom":bathroom,
        "no_of_livingroom":livingroom,
        "no_of_kitchen":kitchen,
        "parking":parking,
        "road_size":road_size,
        "road_type":road_type,
        "land_size":land_area
    }
    alldet.append(det)            # apending all det into all dict list

import pandas as pd          
dataset=pd.DataFrame(alldet)          # convers list into dataframe
dataset.to_csv('Ghar_sansar_raw.csv',index=False)        # save dataset as csv filetype