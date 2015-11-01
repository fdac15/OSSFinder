from pymongo import MongoClient
import re
import requests
import json
import base64
import time
def retrieve_readme(url1,suffix,dest_folder):
    r = requests.get(url1+'/readme',auth=('inthesunset','333369xm'))
    t = r.text
    dic = json.loads(t)
#    print(dic)
#    print(str(base64.b64decode(dic['content']).decode('UTF8')))
    with open(dest_folder+suffix+'.md','a') as f:
        if 'content' in dic.keys():
            f.write(str(base64.b64decode(dic['content']).decode('UTF8','ignore')))

def data_retrieve(url,full_name,_id,dest_folder): 
    full_name = re.sub(r'/',r'____',full_name)
    retrieve_readme(url,str(_id)+'____'+full_name,dest_folder)
    
def data_retrieve_in_file(file):
    number_retrieve = 0
    set_id = ['./Readme_set1/','./Readme_set2/','./Readme_set3/','./Readme_set4/','./Readme_set5/']
    with open(file,'r') as f:
        for line in f:
            _idlist = line.strip().split(',')
            data_retrieve(_idlist[0],_idlist[1],_idlist[2],set_id[int(number_retrieve/4512)])
            number_retrieve = number_retrieve + 1
            if number_retrieve%4513 == 0:
                time.sleep(3600)
                
data_retrieve_in_file('./data_need_for_readme_retrieve.csv')
