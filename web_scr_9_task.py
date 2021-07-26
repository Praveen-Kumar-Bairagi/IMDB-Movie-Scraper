import os,json,time,random
from web_scr_1_task import *
# from web_scr_4_task import *
movies=task_1_file
for i in movies:
	url=i["movie_links"][-10:-1]+".json"
	time.sleep(random.randint(2,3))
	if not(os.path.exists(url)):
		f=open(url,"w+")
		data=json.dumps(i)
		f.write(data)
		f.close()
		print ("nahi thi")
	else:
		print("hai")

