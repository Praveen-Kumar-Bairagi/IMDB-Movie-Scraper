# from web_scr_5_task import *
import json
f=open("imdb_list_5.json","r")
load_data=json.load(f)
f.close()
def analyse_language_and_directors(movies):
    Lang_Direc_dic={}
    for movie in movies:
        for director in movie['director']:
            Lang_Direc_dic[director]={}
    for i in range(len(movies)):
        for director in Lang_Direc_dic:
            if director in movies[i]['director']:
                for language in movies[i]['language']:
                    Lang_Direc_dic[director][language]=0
    for i in range(len(movies)):
        for director in Lang_Direc_dic:
            if director in movies[i]['director']:
                for language in movies[i]['language']:
                    Lang_Direc_dic[director][language]+=1
    # return Lang_Direc_dic
    # file=open('imdb_list_10.json','w')
    # json.dump(Lang_Direc_dic,file,indent=4)
    # file.close()
task10=analyse_language_and_directors(load_data)
# pprint(task10)
# analyse_language_and_directors(task_5_file)
