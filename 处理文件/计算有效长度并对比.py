import pandas as pd

# 固定的路径
base_path = 'E:/大四（下）/毕设/处理文件/output/'

# 获取用户输入的Excel文件名
excel_file_name = input("请输入要读取的Excel文件名（不包括扩展名）: ")

# 拼接完整的文件路径
excel_file_path = f'{base_path}{excel_file_name}.xlsx'
column_of_interest = 'text'  # 替换为感兴趣的列名
max_character_limit = 1000  # 替换为你想要的最大字符数限制

# 读取整个数据框
df = pd.read_excel(excel_file_path)

# 筛选出长度超过最大值的行并保存到新的Excel文件
filtered_rows = df[df[column_of_interest].apply(lambda x: len(str(x)) > max_character_limit)]
output_filtered_path = f'E:/大四（下）/毕设/处理文件/异常数据（上限）/{excel_file_name}.xlsx'
filtered_rows.to_excel(output_filtered_path, index=False)
print(f"已将超过最大字符数限制的行保存到文件: {output_filtered_path}")

# 筛选出不超过最大值的行，保存为新文件
not_filtered_rows = df[df[column_of_interest].apply(lambda x: len(str(x)) <= max_character_limit)].copy()
output_not_filtered_rows_path = f'E:/大四（下）/毕设/处理文件/筛选后的数据（上限）/{excel_file_name}.xlsx'
not_filtered_rows.to_excel(output_not_filtered_rows_path, index=False)
print(f"已将不超过最大长度的行保存到文件: {output_not_filtered_rows_path}")

# 计算指定列下所有行的平均长度、最大长度和最小长度
average_length = df[column_of_interest].apply(lambda x: len(str(x))).mean()
max_length = df[column_of_interest].apply(lambda x: len(str(x))).max()
min_length = df[column_of_interest].apply(lambda x: len(str(x))).min()

# 打印结果
print(f" {column_of_interest} 下所有行的平均长度为: {average_length}")
print(f" {column_of_interest} 下所有行的最大长度为: {max_length}")
print(f" {column_of_interest} 下所有行的最小长度为: {min_length}")

# 计算平均、最小、最大长度（不包括超过最大字符数限制的行）
valid_rows = df[df[column_of_interest].apply(lambda x: len(str(x)) <= max_character_limit)]
average_length = valid_rows[column_of_interest].apply(lambda x: len(str(x))).mean()
max_length = valid_rows[column_of_interest].apply(lambda x: len(str(x))).max()
min_length = valid_rows[column_of_interest].apply(lambda x: len(str(x))).min()

# 打印结果
print(f" {column_of_interest} 下有效行的平均长度为: {average_length}")
print(f" {column_of_interest} 下有效行的最大长度为: {max_length}")
print(f" {column_of_interest} 下有效行的最小长度为: {min_length}")
