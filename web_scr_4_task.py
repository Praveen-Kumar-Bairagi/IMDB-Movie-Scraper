import json
from bs4 import BeautifulSoup
import requests
from web_scr_1_task import *

def scrape_movie_details(movie_url):
    data_dic={}
    page=requests.get(movie_url) 
    soup=BeautifulSoup(page.text,"html.parser")
    body_of_web=soup.find("body")
    data_dic['Name']=body_of_web.find("h1").text[:-8] 
    data_dic['Year']=int(body_of_web.h1.span.a.text)
    director_list=body_of_web.find("div",class_="credit_summary_item").findAll('a')
    data_dic['director']=[i.text.strip() for i in director_list]
    data_dic['bio'] = body_of_web.find("div",class_="summary_text").text.strip()    
    genre_list=body_of_web.find('div', class_ = 'subtext').findAll('a')
    data_dic['gerne']=[i.text for i in genre_list[:-1]]
    country_more=body_of_web.find("div",attrs={"class":'article','id':'titleDetails'}).findAll("div")
    for i in country_more:
        tag=i.findAll("h4")
        for text in tag:
            if 'Language:' in text:
                tag2=i.findAll('a')
                data_dic['language']=[language.text for language in tag2] 
            elif "Country:" in text:
                tag2=i.findAll('a')
                data_dic['country']=[''.join(country.text) for country in tag2]  
    data_dic['img link']='https://www.imdb.com/'+(body_of_web.find_all("div",class_="poster")[0].a['href'])
    time=body_of_web.find("div",class_='subtext').time.text.strip()
    time2=int(time[0])*60
    if 'min' in time:
        a=time.strip('min').split('h')
        data_dic['run time']=str(time2+int(a[1]))+' minutes'
    return data_dic

# # """ Now I am going to dump my data in JSON files"""
   
    # f=open('imdb_list__4.json','w')
    # json.dump(data_dic,f,indent=4)
    # f.close()
link=task_1_file[0]['movie_links']
scrape_movie_details(link)
# pprint(scrape_movie_details(task))



