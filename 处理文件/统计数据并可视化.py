import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 固定的路径f
base_path = 'F:\\大四（下）\\毕设\\处理文件\\out\\'

# 获取用户输入的Excel文件名
excel_file_name = input("请输入要读取的Excel文件名（不包括扩展名）: ")

# 拼接完整的文件路径
excel_file_path = f'{base_path}{excel_file_name}.xlsx'

# 读取整个数据框
df = pd.read_excel(excel_file_path)

# 指定列的名称
column_name = 'text'

# 统计指定列的字符数
char_lengths = df[column_name].astype(str).apply(len)

# 计算最小长度、最大长度、平均长度和中位数
min_length = char_lengths.min()
max_length = char_lengths.max()
mean_length = char_lengths.mean()
median_length = char_lengths.median()

# 打印统计结果
print(f"最小长度: {min_length}")
print(f"最大长度: {max_length}")
print(f"平均长度: {mean_length}")
print(f"中位长度: {median_length}")

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 计算直方图
hist, bins = np.histogram(char_lengths, bins=np.arange(0, char_lengths.max()+10, 10))

# 找到最大和最小频率的字符数
max_freq_char_length = bins[np.argmax(hist)]
min_freq_char_length = bins[np.argmin(hist)]

# 打印结果
print(f"最多频率的字符数: {max_freq_char_length}")
print(f"最少频率的字符数: {min_freq_char_length}")

# 绘制直方图
plt.hist(char_lengths, bins=np.arange(0, char_lengths.max()+10, 10), edgecolor='black')
plt.xticks(np.arange(0, char_lengths.max()+50, 50))
plt.title('字符长度分布图')
plt.xlabel('字符长度')
plt.ylabel('频率')
plt.show()

# 绘制散点图
plt.scatter(df.index, char_lengths, s=1)  # 缩小点的大小为1
plt.title('字符长度散点图')
plt.xlabel('索引')
plt.ylabel('字符长度')
plt.show()