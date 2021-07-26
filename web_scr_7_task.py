import json
from  pprint import pprint

f=open("imdb_list_5.json","r")
load_of_json=json.load(f)
f.close()
def director_movies_language(movies):
    director_dic = {}
    for i in movies:
        for j in i["director"]:
            if(j not in director_dic):
                director_dic[j] = 0     
    for j in director_dic:  
        for a in movies:   
            for b in a['director']: 
                if(b == j):
                    director_dic[j]+=1
    return languagedict

# # """ Now I am going to dump my data in JSON files"""

    # f=open('imdb_list_7.json','w')
    # json.dump(director_dic,f,indent=4)
    # f.close()
task7=director_movies_language(load_of_json)
# pprint(task7)







