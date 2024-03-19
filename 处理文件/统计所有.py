import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 定义文件夹路径
folder_path = 'F:\\大四（下）\\毕设\\处理文件\\data\\'

# 获取文件夹中所有Excel文件的文件名列表
excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 初始化DataFrame
data = {'文件名': [], '最大长度': [], '最小长度': [], '平均长度': []}
all_char_lengths = []  # 用于存储所有文件的字符长度

# 遍历每个Excel文件
for file in excel_files:
    # 读取Excel文件
    df = pd.read_excel(os.path.join(folder_path, file))
    
    # 指定列的名称
    column_name = 'text'  # 请替换为实际的列名称
    
    # 统计指定列的字符数
    char_lengths = df[column_name].astype(str).apply(len)
    
    # 将当前文件的字符长度添加到总长度列表中
    all_char_lengths.extend(char_lengths)
    
    # 计算直方图
    hist, bins = np.histogram(char_lengths, bins=np.arange(0, char_lengths.max()+10, 10))
    
    # 找到最大和最小频率的字符数
    max_freq_char_length = bins[np.argmax(hist)]
    min_freq_char_length = bins[np.argmin(hist)]
    
    # 添加到DataFrame中
    data['文件名'].append(file)
    data['最大长度'].append(max_freq_char_length)
    data['最小长度'].append(min_freq_char_length)
    data['平均长度'].append(np.mean(char_lengths))  # 添加平均长度
    
    # 打印直方图中最大和最小频率的字符数
    print(f"{file} 中最多频率的字符数: {max_freq_char_length}")
    print(f"{file} 中最少频率的字符数: {min_freq_char_length}")
    
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
    # 绘制直方图
    plt.hist(char_lengths, bins=np.arange(0, char_lengths.max()+10, 10), edgecolor='black')
    plt.xticks(np.arange(0, char_lengths.max()+50, 50))
    plt.title(f'{file} - 字符长度分布图')
    plt.xlabel('字符长度')
    plt.ylabel('频率')
    plt.show()
    
    # 绘制散点图
    plt.scatter(df.index, char_lengths, s=1)  # 缩小点的大小为1
    plt.title(f'{file} - 字符长度散点图')
    plt.xlabel('索引')
    plt.ylabel('字符长度')
    plt.show()

# 计算所有文件的最大、最小和平均长度
max_length = max(all_char_lengths)
min_length = min(all_char_lengths)
mean_length = np.mean(all_char_lengths)

# 打印所有文件的统计结果
print(f"所有文件中的最大长度: {max_length}")
print(f"所有文件中的最小长度: {min_length}")
print(f"所有文件中的平均长度: {mean_length}")

# 绘制总体直方图
plt.hist(all_char_lengths, bins=np.arange(0, max(all_char_lengths)+10, 10), edgecolor='black')
plt.xticks(np.arange(0, max(all_char_lengths)+50, 50))
plt.title('总体字符长度分布图')
plt.xlabel('字符长度')
plt.ylabel('频率')
plt.show()

# 绘制总体散点图
plt.scatter(range(len(all_char_lengths)), all_char_lengths, s=1)
plt.title('总体字符长度散点图')
plt.xlabel('索引')
plt.ylabel('字符长度')
plt.show()

# 创建DataFrame
df_result = pd.DataFrame(data)

# 打印结果表格
print(df_result)