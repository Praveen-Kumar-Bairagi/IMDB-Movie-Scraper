import json
from pprint import pprint
file=open('imdb_list_5.json','r')
moviedettail_file=json.load(file)
file.close()
main_data_list=[]
dic={}
moviecast_file=open('imdb_list_12.json','r')
movie_cast=json.load(moviecast_file)
def get_movie_list_details():
    for i,j in zip(moviedettail_file,movie_cast):
        dic['movie Name']=i
        dic['cast']=j
        main_data_list.append(dic.copy())
    f=open('imdb_list_13.json','w')
    json.dump(main_data_list,f,indent=4)
    f.close()
    # return main_data_list
get_movie_list_details()


# import os,json,time,random
# from pprint import pprint
# from web_scr_1_task import *
# from web_scr_12_task import *
# def cach():
#     movies=scrape_top_list()
#     all_data=[]
#     for i in movies:
#         url=i["movie_links"][-10:-1]
#         with open(url+".json","r") as file:
#         		data=json.load(file)
#         j_url=url+".json"
#         if not(os.path.exists(j_url)):
#             print ("hi")
#             url2="https://www.imdb.com/title/"+url
#             data["cast"]=scrape_movie_cast(url2)
#             with open(j_url,"w+") as file:
#                 d_data=json.dumps(data)
#                 file.write(d_data)
#         all_data.append(data)
#     return all_data
# pprint(cach())