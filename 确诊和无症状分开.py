import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
sns.set_style("darkgrid")
sns.set_context("paper")
plt.rcParams["font.sans-serif"]='SimHei'   #解决中文乱码问题
plt.rcParams['axes.unicode_minus']=False   #解决负号无法显示的问题

pd.set_option('display.max_columns',40)    # 最多显示40列
pd.set_option('display.max_rows',20)       # 最多显示20行
warnings.filterwarnings("ignore")

df1 = pd.read_excel('./新冠疫情人数变化.xlsx', sheet_name=0)

plt.figure(figsize=(12,6))
plt.plot(df1['感染人数'], '-+',label='感染人数')   
plt.plot(df1['无症状感染者'], '-o',label='无症状感染者')
plt.plot(df1['总计感染人数'], '-^',label='总计感染人数')
plt.legend(fontsize=13,framealpha=0)
plt.xlabel('时间',fontsize=18)
plt.ylabel('感染人数',fontsize=18)
plt.xticks(fontsize=17)
plt.yticks(fontsize=17)
plt.savefig('./images/全市感染人数趋势图.png')
plt.show()