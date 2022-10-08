import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline

df = pd.read_excel('./附件1：长春市COVID-19疫情期间病毒感染人数数据.xlsx', sheet_name=0, header=0, usecols=[0]+list(range(11, 27)))
data = df.iloc[:41, :].values

location = ['九台区', '长春新区', '净月区', '绿园区',	'朝阳区', '经开区','双阳区', '宽城区','南关区','汽开区','二道区','莲花山区', '公主岭市','德惠市','榆树市','农安县']

tl = Timeline()

for i in range(data.shape[0]):
      map_min=int(np.min(data[i, 1:]))
      map_max=int(np.max(data[i, 1:]))
      maps = (
            Map()
            .add("人数",[list(z) for z in zip(location, list(data[i, 1:]))], "长春")
            .set_global_opts(title_opts=opts.TitleOpts(title="长春感染人数分布图"), visualmap_opts=opts.VisualMapOpts(type_='color',min_=map_min,max_=map_max))
      )
      tl.add(maps, data[i, 0])
tl.add_schema(is_auto_play=True, play_interval=500)
tl.render(path='./images/2.html')
