import json,pprint
file=open("imdb_list_12.json",'r')
movie_list = json.load(file)

def analyse_co_actors():
    movies_cast_list = []
    for cast_list in movie_list:
        cast_dict={}
        for i in range(len(cast_list)-1):
            actors_list=[]
            actors_dict={}
            actors_dict['Imdb_Id'] = cast_list[i+1]["Imdb_Id"]
            actors_dict["Name"] = cast_list[i+1]['Name']
            Count = 0
            for Movies in movie_list :
                if cast_list[i] in Movies and cast_list[i+1] in Movies:
                    Count+=1
            actors_dict['count_movies'] = Count
            actors_list.append(actors_dict)
            cast_dict[cast_list[i]['Imdb_Id']]={"Name":cast_list[i]['Name'],'frequent_co_actors':actors_dict}
        movies_cast_list.append(cast_dict)
    f=open('imdb_list_14.json','w')
    json.dump(movies_cast_list,f,indent=4)
    f.close()
    # return movies_cast_list
task_14=analyse_co_actors()
# pprint.pprint(task_14)

