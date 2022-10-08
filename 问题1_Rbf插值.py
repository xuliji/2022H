import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, UnivariateSpline, Rbf, splev, splrep, lagrange

df_1 = pd.read_excel('./附件1：长春市COVID-19疫情期间病毒感染人数数据.xlsx', sheet_name=0, header=0, usecols=range(10, 27))
df_2 = pd.read_excel('./附件1：长春市COVID-19疫情期间病毒感染人数数据.xlsx', sheet_name=1, header=0, usecols=range(1, 18))
df_sum = df_1 + df_2
# 所有区都归零前的数据
real_data = df_sum.iloc[:41, :].values
# 26号之前的数据
data = df_sum.iloc[:23, :].values
order = np.arange(23)
x_new = np.arange(41)
for i in range(17):
    
    inter_func = Rbf(order, data[:, i], k=4)
    y_new = inter_func(x_new)

    plt.figure()
    plt.plot(x_new, y_new, label='interpolate')
    plt.plot(x_new, real_data[:, i], label='real')
    plt.legend()
    plt.savefig('./images/插值效果图/{}.png'.format(i))
    plt.show()

