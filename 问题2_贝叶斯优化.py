from audioop import cross
from re import X
import networkx as nx
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import matplotlib as mpl
# 贝叶斯优化
from bayes_opt import BayesianOptimization
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']

# 第三张表，包含每个区的小区及小区的虚拟坐标
data_3 = pd.read_excel('./附件3：长春市9个区交通网络数据和主要小区相关数据.xlsx', header=0, sheet_name=2, usecols=[4, 5, 7])
# 小区横坐标，小区纵坐标
village_x, village_y = list(data_3['小区横坐标'].values), list(data_3['小区纵坐标'].values)
village_pos_1 = np.array([list(pos) for pos in zip(village_x, village_y)])


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
# KMeans聚类
def rf_cv(n_clusters, n_init, max_iter):
    model = KMeans(n_clusters=int(n_clusters), n_init=int(n_init), max_iter=int(max_iter))
    model.fit(village_pos_1)
    label = model.labels_
    val = silhouette_score(village_pos_1, label)
    return val


pbounds = {
    'n_clusters':(70, 140),
    'n_init':(10, 50),
    'max_iter':(300, 1000)
}
optimizer = BayesianOptimization(
    f=rf_cv,  # 黑盒目标函数
    pbounds=pbounds,  # 取值空间
    verbose=2,  # verbose = 2 时打印全部，verbose = 1 时打印运行中发现的最大值，verbose = 0 将什么都不打印
    random_state=1,
)
optimizer.maximize(  # 运行
    init_points=5,  # 随机搜索的步数
    n_iter=1000,  # 执行贝叶斯优化迭代次数
)
print(optimizer.max)




