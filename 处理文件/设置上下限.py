import pandas as pd

# 固定的路径
base_path = 'E:/大四（下）/毕设/处理文件/output/'

# 获取用户输入的Excel文件名（不含扩展名）
excel_file_name = input("请输入要读取的Excel文件名（不含扩展名）: ")

# 添加默认的扩展名
excel_file_path = f'{base_path}{excel_file_name}.xlsx'

# 读取整个数据框
df = pd.read_excel(excel_file_path)

# 获取用户输入的指定列名
column_of_interest = 'text'  # 替换为感兴趣的列名

# 获取用户输入的最大字符限制和最小字符限制
max_character_limit = 1000
min_character_limit = 20

# 筛选出长度超过最大值且不低于最小值的行
filtered_rows = df[(df[column_of_interest].apply(lambda x: len(str(x)) > max_character_limit)) | 
                   (df[column_of_interest].apply(lambda x: len(str(x)) < min_character_limit))].copy()

# 添加默认的扩展名
output_file_path = f'E:/大四（下）/毕设/处理文件/异常数据/异常数据（上下限均设）/{excel_file_name}.xlsx'
filtered_rows.to_excel(output_file_path, index=False)
print(f"已将超过最大长度或低于最小长度的行保存到文件: {output_file_path}")

# 筛选出指定列下不超过最大值但不低于最小值的行，计算平均、最小、最大长度
df_filtered = df[(df[column_of_interest].apply(lambda x: len(str(x)) <= max_character_limit)) & 
                 (df[column_of_interest].apply(lambda x: len(str(x)) >= min_character_limit))].copy()  # 复制一份以免修改原始数据

# 添加默认的扩展名
output_filtered_file_path = f'E:/大四（下）/毕设/处理文件/筛选后数据/筛选后的数据（上下限）/{excel_file_name}.xlsx'
df_filtered.to_excel(output_filtered_file_path, index=False)
print(f"已将不超过最大长度但不低于最小长度的行保存到文件: {output_filtered_file_path}")

# 计算
average_length = df_filtered[column_of_interest].apply(lambda x: len(str(x))).mean()
max_length = df_filtered[column_of_interest].apply(lambda x: len(str(x))).max()
min_length = df_filtered[column_of_interest].apply(lambda x: len(str(x))).min()
# 打印结果
print(f" {column_of_interest} 中有效行的平均长度为: {average_length}")
print(f" {column_of_interest} 中有效行的最大长度为: {max_length}")
print(f" {column_of_interest} 中有效行的最小长度为: {min_length}")
