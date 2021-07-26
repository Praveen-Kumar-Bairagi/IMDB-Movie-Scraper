import json
from  pprint import pprint

file=open("imdb_list_5.json","r")
load_of_json=json.load(file)
file.close()

def analyse_movies_language(movies):
    languagedict = {}
    for i in movies:
        for j in i["language"]:
            if(j not in languagedict):
                languagedict[j] = 0     
    for j in languagedict:  
        for k in movies:    
            for m in k['language']: 
                if(m == j):
                    languagedict[j]+=1    
    return languagedict

# # """ Now I am going to dump my data in JSON files"""

    # file=open('imdb_list_6.json','w')
    # json.dump(languagedict,file,indent=4)
    # file.close()
task6=analyse_movies_language(load_of_json)
# pprint(task6)

                                                                    

