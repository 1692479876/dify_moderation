import os
import jsonlines
root_path=r'.\\test'

file_list = os.listdir(root_path) #获取root_path中的所有文件名
content_list = []  #声明列表，存储从json文件中读取的字典
for item in file_list:
    file_path = os.path.join(root_path,item) #拼接文件路径
    with jsonlines.open(file_path,'r') as f:
        for data in f:
            content_list.append(data)
        
import pandas as pd
df = pd.DataFrame(content_list)
df.to_excel(os.path.join(root_path,'output.xlsx'),encoding='utf8')