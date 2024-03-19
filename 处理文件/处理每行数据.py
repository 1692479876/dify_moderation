import pandas as pd
import re
# 读取Excel文件
# 固定的路径
base_path = 'E:/大四（下）/毕设/处理文件/output/'

# 获取用户输入的Excel文件名
excel_file_name = input("请输入要读取的Excel文件名（不包括扩展名）: ")

# 拼接完整的文件路径
excel_file_path = f'{base_path}{excel_file_name}.xlsx'
df = pd.read_excel(excel_file_path)

# 指定要删除的特定信息所在的列
target_column_1 = 'text'
target_column_2 = 'source'

# 转义要删除的特定信息中的特殊字符
escaped_target_1 = re.escape('*****')
escaped_target_2 = re.escape('local/')


# 使用正则表达式替换包含要删除信息的内容
df[target_column_1] = df[target_column_1].replace(escaped_target_1, ':', regex=True)
df[target_column_2] = df[target_column_2].replace(escaped_target_2, '', regex=True)


# 将修改后的数据框写回Excel文件
df.to_excel(excel_file_path, index=False)