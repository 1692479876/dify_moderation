import os
import pandas as pd
from openpyxl import load_workbook

def process_excel_files(input_folder, output_folder, column_to_search, column_to_move, search_string):
    # 遍历输入文件夹下的所有Excel文件
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            # 读取Excel文件
            input_file = os.path.join(input_folder, file_name)
            df = pd.read_excel(input_file)

            # 查找指定列中包含特定字符串的行
            rows_to_process = df[df[column_to_search].str.contains(search_string)]

            # 将指定列中特定字符串之前的所有字符移动到另一指定列末尾
            for index, row in rows_to_process.iterrows():
                value = row[column_to_search]
                new_value = value.split(search_string)[0]
                df.at[index, column_to_move] = df.at[index, column_to_move] + "/" + new_value
                df.at[index, column_to_search] = str(row[column_to_search]).replace(new_value + search_string, "")
            # 保存新的Excel文件
            output_file = os.path.join(output_folder, file_name)
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)

# 示例用法
input_folder = "F:\\大四（下）\\毕设\\处理文件\\raw"
output_folder = "F:\\大四（下）\\毕设\\处理文件\\data"
column_to_search = "text"
column_to_move = "source"
search_string = ":"

process_excel_files(input_folder, output_folder, column_to_search, column_to_move, search_string)