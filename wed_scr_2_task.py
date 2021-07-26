from web_scr_1_task import *
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i['movie_years']
        if year not in years:
            years.append(year)
    movies_dict={i:[]for i in years}
    for i in movies:
        year=i['movie_years']
        for j in movies_dict:
            if str(j)==str(year):
                movies_dict[j].append(i)
                
# # """ Now I am going to convert my data in JSON files"""

#     f=open('imdb_list_2.json','w')
#     json.dump(movies_dict,f,indent=4)
#     f.close()
    return movies_dict
task_2_file=group_by_year(task_1_file)
# pprint(task_2_file)
