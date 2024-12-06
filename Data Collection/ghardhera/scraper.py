#importing basic libaries for website scraping and acessing.
import requests
from bs4 import BeautifulSoup

baseurl='https://www.gharghaderi.com/'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

links=[]

#this loop will run and generat the href file that content site link to acess the more detials.
for i in range(50):
    response=requests.get(f'https://www.gharghaderi.com/nepal-houses/?page={i}',headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')

    listing_links=soup.find_all('div',class_='grid-thirds2 grid-thirds')

    for list in listing_links:
        for link in list.find_all('a',href=True):
            link=link['href']

            links.append(baseurl+link)



test='https://www.gharghaderi.com/house/6547-House-On-Sale-at-Gothatar-Kathmandu/'

alldet=[]
for link in links:
    response=requests.get(link,headers=headers)

    soup=BeautifulSoup(response.content,'html.parser')
    try:
        price_raw=soup.find_all('td',class_='lower')[0].text.split() #this code will give you prices_tag
        price="".join(price_raw[:-1])  #this code will shape the result
    except:
        price=""

    try:
        road=soup.find_all('td',class_='lower')[2].text.split()  #this code will give you road_size
        road_size="".join(road[:-1])   #this code will shape the result
    except:
        road_size=''

    
    locater=soup.find_all('div',class_='right')  #this code will give you acess to more detials card
    try:
        location=locater[0].find_all('td',class_='test1')[3].text.split()[0]  #this code will use locater and give you the location
    except:
        location=""
    try:
        facing=locater[1].find_all('td',class_='test1')[0].text.split()[0]    #this code will use locater and give you the property facing
    except:
        facing=''

    try:
        bedroom=locater[1].find_all('td',class_='test1')[1].text.split()[0]   #this code will use locater and give you the no of bedroom
    except:
        bedroom=''
    try:    
        bathroom=locater[1].find_all('td',class_='test1')[2].text.split()[0]  #this code will use locater and give you the no of bathroom
    except:
            bathroom=''
    try:
        livingroom=locater[1].find_all('td',class_='test1')[3].text.split()[0]   #this code will use locater and give you the no of living-room 
    except:
        livingroom=''

    try:
        kitchen=locater[1].find_all('td',class_='test1')[4].text.split()[0]   #this code will use locater and give you the no of kitchen
    except:
        kitchen=''

    try:
        parking=locater[1].find_all('td',class_='test1')[5].text.split()[0]   #this code will use locater and give you the parking space
    except:
        parking=""
    
    locater_b=soup.find_all('div',class_='left')  #this code will give you acess to more detials card
    try:
        floors=locater_b[1].find_all('td',class_='test1')[3].text.split()[0]
    except:
        floors=''

    try:
        land=locater_b[1].find_all('td',class_='test1')[2].text.split() #this code will give you land_area
        land_area=" ".join(land) #this code will shape the result
    except:
        land_area=""

    try:
        road_size=locater_b[1].find_all('td',class_='test1')[4].text.split()[0]
    except:
        road_size=""
    

    # this detials dict will store all the above detials
    detials={
        'price':price,
        'location':location,
        'area':land_area,
        'facing':facing,
        'no_of_bedroom':bedroom,
        'no_of_bathroom':bathroom,
        'no_of_livingroom':livingroom,
        'no_of_kitchen':kitchen,
        'parking':parking,
        'road_size':road_size,
        'floors':floors

    }

    alldet.append(detials) #this code will apped all the detial dict into alldet 

    
     

import pandas as pd
dataset=pd.DataFrame(alldet)  #convert alldet into dataset
dataset.to_csv('added_raw_gharghaderi.csv')  #save dataset into csv 

