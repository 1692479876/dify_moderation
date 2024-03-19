import pandas as pd
import matplotlib.pyplot as plt

# 固定的路径f
base_path = 'F:\\大四（下）\\毕设\\处理文件\\out\\'

# 获取用户输入的Excel文件名
excel_file_name = input("请输入要读取的Excel文件名（不包括扩展名）: ")

# 拼接完整的文件路径
excel_file_path = f'{base_path}{excel_file_name}.xlsx'
column_of_interest = 'text'  # 替换为感兴趣的列名

# 读取整个数据框
df = pd.read_excel(excel_file_path)

# 计算指定列下所有行的平均长度、最大长度和最小长度
average_length = df[column_of_interest].apply(lambda x: len(str(x))).mean()
max_length = df[column_of_interest].apply(lambda x: len(str(x))).max()
min_length = df[column_of_interest].apply(lambda x: len(str(x))).min()

# 打印结果
print(f"指定列 {column_of_interest} 下所有行的平均长度为: {average_length}")
print(f"指定列 {column_of_interest} 下所有行的最大长度为: {max_length}")
print(f"指定列 {column_of_interest} 下所有行的最小长度为: {min_length}")
