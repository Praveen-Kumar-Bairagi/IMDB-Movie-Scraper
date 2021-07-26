import requests
from bs4 import BeautifulSoup
import json
from  pprint import pprint

f=open("imdb_list_1.json","r")
read_json=f.read()
load_data=json.loads(read_json)
f.close()
url_list=[]
for i in load_data:
    url_list.append(i['movie_links'])
print("loding....")
# #Task 12
# #This function returns a list of full cast of a movie
def scrape_movie_cast(url_list):
    main_list=[]
    for url in url_list:
        res = requests.get(url)
        soup = BeautifulSoup(res.text,"html.parser")
        actors = soup.find("table",class_="cast_list").findAll("td",class_="")
        loop=0
        data_list=[]
        for a_tags in actors:
            dic={}
            dic["Imdb_Id"]=actors[loop].find("a").get("href")[6:15]
            dic["Name"]=actors[loop].get_text().strip()
            loop+=1
            data_list.append(dic)
        main_list.append(data_list)
    f=open('imdb_list_12.json','w')
    json.dump(main_list,f,indent=4)
    f.close()
    # return main_list
scrape_movie_cast(url_list)
# pprint(scrape_movie_cast(list_of_links(load_of_json)))
print("done...")






