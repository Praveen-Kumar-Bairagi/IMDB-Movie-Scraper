import json
from pprint import pprint
from web_scr_4_task import *
file=open("imdb_list_1.json","r")
movies=json.load(file)	
print ("loding....")
def get_movie_list_details(movies):
    data_list=[]
    for movie in movies:
        url=(movie["movie_links"])
        data_list.append(scrape_movie_details(url))

# # """ Now I am going to dump my data in JSON files"""

    # file=open('imdb_list_5.json','w')
    # json.dump(data_list,file,indent=4)
    # file.close()
    return data_list
task_5_file=get_movie_list_details(movies)
print("done....")
# pprint(task_5_file)


