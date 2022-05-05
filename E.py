# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:53:58 2022

@author: Weigel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:\data.txt', delimiter = "\t")


dff = df

datetimes = pd.to_datetime(dff['timeStamp '])

dff['timeStamp '] = datetimes


start_date1 = pd.to_datetime("2021-05-06 13:50:40")
end_date1 = pd.to_datetime("2021-05-06 14:02:37")
start_date2 = pd.to_datetime("2021-05-06 14:10:40")
end_date2 = pd.to_datetime("2021-05-06 14:43:37")

f =  df[(df['timeStamp '] > start_date1) & (df['timeStamp '] < end_date1)]
f2 =  df[(df['timeStamp '] > start_date2) & (df['timeStamp '] < end_date2)]



plt.figure()
plt.plot(f[' temp2 '])

fig = plt.figure()
fig.subplots_adjust(hspace = 0.5)

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.grid()
ax2.grid()

ax1.set_title("Sensor 2 - Ohne Sitzbezug")
ax2.set_title("Sensor 2 - Ohne Sitzbezug")

ax1.plot( f[' temp2 '].reset_index(drop=True))
ax2.plot( f2[' temp2 '].reset_index(drop=True))


plt.show()
