import os
import pandas as pd

def split_long_strings(input_path, output_path, column_name, max_characters):
    # 读取Excel文件
    df = pd.read_excel(input_path)
    
    # 检查是否有指定列
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the file '{input_path}'")
        return
    
    # 创建一个空的DataFrame来存储结果
    new_rows = []
    
    # 遍历原始DataFrame的每一行
    for index, row in df.iterrows():
        # 检查指定列的字符串长度是否超过最大字符上限
        if len(str(row[column_name])) > max_characters:
            # 如果超过最大字符上限，分割字符串
            long_string = str(row[column_name])
            splitted_strings = [long_string[i:i+max_characters] for i in range(0, len(long_string), max_characters)]
            
            # 创建新行，并添加到新的DataFrame中
            for split_string in splitted_strings:
                new_row = row.copy()
                new_row[column_name] = split_string
                new_rows.append(new_row)
        else:
            # 如果字符串长度没有超过最大字符上限，直接添加到新的DataFrame中
            new_rows.append(row)
    
    # 创建新的DataFrame
    new_df = pd.DataFrame(new_rows)
    
    # 导出新的Excel文件
    new_df.to_excel(output_path, index=False)
    print(f"Splitting completed. Result saved to '{output_path}'")

# 文件夹路径
folder_path = "F:\\大四（下）\\毕设\\处理文件\\data"

# 输出文件夹路径
output_folder = "F:\\大四（下）\\毕设\\处理文件\\分析"

# 最大字符上限
max_characters = 500

# 遍历文件夹下的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        input_path = os.path.join(folder_path, filename)
        output_path = os.path.join(output_folder, f"split_{filename}")
        split_long_strings(input_path, output_path, "text", max_characters)
