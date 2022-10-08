'''
用附件3中的数据可视化出长春市的路网图和小区分布。
'''
from audioop import cross
from re import X
import networkx as nx
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']

# 第一张表，包含路口的虚拟坐标
data_1 = pd.read_excel('./附件3：长春市9个区交通网络数据和主要小区相关数据.xlsx', header=0, sheet_name=0, usecols=[0, 1, 2])


# 第二张表，包含两个路口间的连接情况和距离
data_2 = pd.read_excel('./附件3：长春市9个区交通网络数据和主要小区相关数据.xlsx', header=0, sheet_name=1, usecols=[1, 2, 3])


# 第三张表，包含每个区的小区及小区的虚拟坐标
data_3 = pd.read_excel('./附件3：长春市9个区交通网络数据和主要小区相关数据.xlsx', header=0, sheet_name=2, usecols=[4, 5, 7])


# 路口编号，路口横坐标，路口纵坐标
cross_list, cross_x, cross_y = list(data_1['节点编号'].values), list(data_1['路口横坐标'].values), list(data_1['路口纵坐标'].values)
cross_pos = [pos for pos in zip(cross_x, cross_y)]

# 路线起点， 路线终点， 路线距离
start, end, length = list(data_2['路线起点'].values), list(data_2['路线终点'].values), list(data_2['路线距离(m)'].values)
edges = [z for z in zip(start, end)]

# 小区横坐标，小区纵坐标
village_x, village_y = list(data_3['小区横坐标'].values), list(data_3['小区纵坐标'].values)
village_pos = [pos for pos in zip(village_x, village_y)]

# 创建无向图
roads = nx.Graph()

# # 添加路口点
# for i in cross_order:
#     roads.add_node(i, pos=(cross_x[i-1], cross_y[i-1]))

# # 添加道路
# for j in range(len(edges)):
#     roads.add_edge(edges[j][0], edges[j][1], length=length[j])

village_list = list(np.arange(len(cross_pos), len(cross_pos)+len(village_pos)))

# 十字路口节点坐标
c_pos = dict(zip(cross_list, cross_pos))
# 小区坐标点
v_pos = dict(zip(village_list, village_pos))

pos={}
pos=c_pos.copy()
pos.update(v_pos)
plt.figure(figsize=(15, 15))
plt.xlim(0, 100)
plt.ylim(0, 100)
# 绘制点
# nx.draw_networkx_nodes(roads,c_pos,cross_list,node_size=10,node_color='#FF8A23')
nx.draw_networkx_nodes(roads,v_pos,village_list,node_size=10,node_color='#9FC3E4')

# 绘制边
nx.draw_networkx_edges(roads, pos, edges, width=0.3, edge_color='#FF8A23')

# 显示节点标签
clabels = dict(zip(cross_list,cross_list))
vlabels = dict(zip(village_list,village_list))
plt.title("长春市路网图", fontsize=20)
plt.savefig('./images/路网图.png')
plt.show()

