import os,json
from web_scr_1_task import *

f=open("imdb_list_1.json","r")
load_of_json=json.load(f)
f.close()
movies=load_of_json
movies=task_1_file
for i in movies:
	url=i["movie_links"][-10:-1]+".json"
	if not(os.path.exists(url)): #Checks whether JSON file already exists or not
# # """ Now I am going to convert my data in JSON files"""
		f=open(f"{url}","w+")
		json.dump(i,f,indent=4)
		f.close()
		print ("nahi thi")
	else:
		print("hai")





