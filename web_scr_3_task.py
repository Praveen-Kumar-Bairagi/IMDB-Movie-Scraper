from wed_scr_2_task import *

def group_by_decade(movies):
    movie_dict={}
    movie_lists=[]
    for i in movies:
        mod=i%10
        decade=i-mod 
        if decade not in movie_lists:
            movie_lists.append(decade)
    movie_lists.sort()
    for i in movie_lists:
        movie_dict[i]=[]
    for i in movie_lists:
        dec10=i+9 
        for j in movies:
            if j <= dec10 and j >= i: 
                for v in movies[j]:
                    movie_dict[i].append(v)

# # """ Now I am going to dump my data in JSON files"""

    # f=open('imdb_list_3.json','w')
    # json.dump(movie_dict,f,indent=4)
    # f.close()
    return movie_dict
task_3_file=group_by_decade(task_2_file)
# pprint(task_3_file)




