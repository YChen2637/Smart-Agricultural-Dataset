# @Descripttion ：
# -*- codeing: utf-8 -*-
# @time ：2024/12/14 23:07
# @Author : Ruifeng Xu
# @Site : 
# @file : chart-type-sensor-data.py
# @Sofeware : PyCharm




import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt


# ----------------------------------------Wheat sensor data-------------------------
file_path="Wheat_sensor"
Wheat=pd.read_excel(file_path,engine="openpyxl",sheet_name='OverView',skiprows=4)
Wheat_sensor=Wheat.loc[:,["名称（EN）","数量"]]
Wheat_sensor.columns=["传感器名称","数量"]
Wheat_sensor=pd.DataFrame(Wheat_sensor)
Wheat_sensor = Wheat_sensor.iloc[1:-1].reset_index(drop=True)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(Wheat_sensor["传感器名称"], Wheat_sensor["数量"], color='skyblue')
ax.set_title('Sensor Data in Wheat',fontsize=15)
ax.set_xlabel('Sensor Type',fontsize=15)
ax.set_ylabel('Data Size',fontsize=15)


for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')
plt.savefig('fig_5_Wheat_sensor.pdf', format='pdf')
plt.show()

# ----------------------------------------Maize sensor data-------------------------
file_path="Maize_sensor"
Maize=pd.read_excel(file_path,engine="openpyxl",sheet_name='OverView',skiprows=4)
Maize_sensor=Maize.loc[:,["名称（EN）","数量"]]
Maize_sensor.columns=["传感器名称","数量"]
Maize_sensor=pd.DataFrame(Maize_sensor)
Maize_sensor = Maize_sensor.iloc[3:9].reset_index(drop=True)
fig, ax = plt.subplots(figsize=(10, 6))  # 设置图形大小
bars = ax.bar(Maize_sensor["传感器名称"], Maize_sensor["数量"], color='skyblue')
ax.set_title('Sensor Data in Maize',fontsize=15)
ax.set_xlabel('Sensor Type',fontsize=15)
ax.set_ylabel('Data Size',fontsize=15)
for bar in bars:
    height = bar.get_height()
    ax.annotate('{}'.format(height),
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

plt.savefig('fig_5_Maize_sensor.pdf', format='pdf')
plt.show()

# ----------------------------------------Cotton sensor data-------------------------
file_path="Cotton_sensor"
Cotton = pd.read_excel(file_path,engine='openpyxl',sheet_name='OverView',skiprows=4)
x_val=[sensor.replace("Sensor", "") for sensor in Cotton.iloc[3:,2].tolist()]
del x_val[3]
y_val=[data for data in Cotton.iloc[3:,6].tolist()]
del y_val[3]
plt.figure(figsize=(15, 10))

fig, ax = plt.subplots()
bars = ax.bar(x_val, y_val, color=cm.Blues(0.5))
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom',fontsize=8)
plt.title('Sensor Data in Cotton', fontsize=20)
plt.xlabel('Sensor Type', fontsize=15,labelpad=10)
plt.ylabel('data Size', fontsize=15)

plt.subplots_adjust(bottom=0.20,top=0.85)
# 设置刻度字体大小
plt.tick_params(axis='x', labelsize=8)
plt.tick_params(axis='y', labelsize=8)
plt.savefig('flg_5_Cotton_Sensor.pdf', format='pdf')
plt.show()
