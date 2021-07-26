import requests                # Importing requests to get request data from a Web URL
import json                    # Importing JSON module to load and dump from json file and dump dictionary in json respectively
from bs4 import BeautifulSoup  # Importing BeautifulSoup from BS4, BeautifulSoup is a scraping tool
from  pprint import pprint
'''
This program scrape list and details of Top 250 rated movies of India according to IMDB and analyse them
categorically in different aspects like, language, directors, genre etc.
'''
def scrape_top_list():
    url ="https://www.imdb.com/india/top-rated-indian-movies/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    trs = soup.find("tbody",class_="lister-list").findAll("tr")
    movies , rateing , years , position ,links= [],[],[],[],[]
    d={}
    top_250_movieas = []
    for movie in trs:
        movies.append(movie.find("td",class_="titleColumn").find("a").get_text())
        rateing.append(float(movie.find("td",class_="ratingColumn imdbRating").text.strip()))
        years.append(int(movie.find("span",class_="secondaryInfo").text[1:5]))
        position.append(int(movie.text.strip().split('.')[0]))
        links.append('https://www.imdb.com'+movie.find('a').get('href'))
    for i,j,k,l,m in zip(movies,rateing,links,years,position):
        d['movie_name'] = i
        d['movie_rating'] = j
        d['movie_links'] = k
        d['movie_years'] = l
        d['movie_postion'] = m
        top_250_movieas.append(d.copy())
    
## """ Now I am going to convert my data in JSON files"""

    return top_250_movieas
    # f=open('imdb_list_1.json','w')
    # json.dump(top_250_movieas,f,indent=4)
    # f.close()
task_1_file = scrape_top_list()
# pprint(task_1_file)   





