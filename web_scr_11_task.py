# from web_scr_5_task import *
import json
f=open("imdb_list_5.json","r")
load_of_json=json.load(f)
f.close()
def  analyse_movies_genre(movie_data):
    list1=[]
    genre_dic={}
    for i in movie_data:
        for j in i['gerne']:
            list1.append(j)
    for f in list1:
        count=0
        for j in list1:
            if f==j:
                count+=1
        genre_dic[f]=count
    f=open('imdb_list_11.json','w')
    json.dump(genre_dic,f,indent=4)
    f.close()
    # return genre_dic
task_11=analyse_movies_genre(load_of_json)
# print(task_11)

# return_directors(task_5_file)
