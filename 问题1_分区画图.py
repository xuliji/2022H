from threading import local
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("paper")
plt.rcParams["font.sans-serif"]='KaiTi'   #解决中文乱码问题
plt.rcParams['axes.unicode_minus']=False   #解决负号无法显示的问题

df_1 = pd.read_excel('./附件1：长春市COVID-19疫情期间病毒感染人数数据.xlsx', sheet_name=0, header=0, usecols=[0]+list(range(10, 27)))
df_3 = df_1.iloc[:, 1:]
print(df_3)

df_2 = pd.read_excel('./附件1：长春市COVID-19疫情期间病毒感染人数数据.xlsx', sheet_name=1, header=0)
df_4 = df_2.iloc[:, 1:]


df_sum = df_3+df_4
df_time = df_1.iloc[:, 0]
data = pd.concat([df_time,df_sum],axis=1).values
# data.to_excel('./sum_data.xlsx')
location = ['全市总计','九台区','长春新区','净月区','绿园区','朝阳区','经开区','双阳区','宽城区','南关区','汽开区','二道区','莲花山区','公主岭市','德惠市','榆树市','农安县']


plt.figure(figsize=(12, 6))
plt.title('长春市疫情发展总体趋势图', fontsize=16)
plt.xlabel("日期", fontsize=16)
plt.ylabel("总感染人数", fontsize=16)
markers = ['-*', '-o', '-^', '-+', '-x', '-+', '-o', '-^', '-p', '-d']
for i in range(1, data.shape[1]):
    marker = markers[i%len(markers)]
    plt.plot(data[:, 0], data[:, i], marker,label=location[i-1])

plt.legend()
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig('./images/分区图.png')
plt.show()
