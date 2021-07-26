# from web_scr_13_task import *
import json,pprint

f=open("imdb_list_13.json","r")
load_data=json.load(f)
f.close()

def analyse_actors(movie_list):
    dic={}
    dic2={}
    for movie in movie_list:
        cast= (movie["cast"])
        for i in cast:
            name=(i["Imdb_Id"])
            if name in dic:
                dic[name]+=1
            else:
                dic[name]=1
    for i in dic:
        for movie in movie_list:
            cast=movie["cast"]
            for j in cast:
                if i== (j["Imdb_Id"]) and i not in dic2:
                    dic2[i]={"Name":j["Name"],"num_movies":dic[i]}
    # f=open('imdb_list_15.json','w')
    # json.dump(dic2,f,indent=4)
    # f.close()
    return dic2
task15=analyse_actors(load_data)
# pprint.pprint(task15)








    