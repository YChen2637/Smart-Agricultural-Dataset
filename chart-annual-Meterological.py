# @Descripttion ：
# -*- codeing: utf-8 -*-
# @time ：2024/12/14 23:00
# @Author : Ruifeng Xu
# @Site :
# @file : chart-annual-Meterological.py
# @Sofeware : PyCharm
#
#


import numpy as np
import matplotlib.pyplot as plt




# -----------------------------------data_processing----------------------------------
file_path="Meterological dataset"
Rain_year=[]
max_temp_year=[]
min_temp_year=[]
SRAD_year=[]
year=[]
for  a in range(1981,2025):
    Rain=[]
    max_temp=[]
    min_temp=[]
    SRAD=[]
    year.append(a)
    if a!=2024:
       file_path_1=file_path+"DSWL"+str(a)+".WTH"
    else:
        file_path_1=file_path+"QXWL"+str(a)+".WTH"
    with open(file_path_1, 'r',encoding='utf-8') as file:
        for i in  range (5):
            next(file)
        for line in file.readlines():
            line=line.strip()
            if not line:
                print("遇到空行，停止读取")
                break
            if line[0:1]!="!":
                try:
                    if float(line[8:11].strip())==-99:
                        continue
                    SRAD.append(float(line[8:11].strip()))
                    if float(line[12:17].strip()) == -99:
                        continue
                    max_temp.append(float(line[12:17].strip()))
                    if float(line[18:23].strip()) == -99:
                        continue
                    min_temp.append(float(line[18:23].strip()))
                    if float(line[24:29].strip()) == -99:
                        continue
                    Rain.append(float(line[24:29].strip()))
                except:
                    print("遇到错误，停止读取"+str(a)+line[0:1])
        SRAD_sum=sum(SRAD)
        max_temp_sum=sum(max_temp)
        min_temp_sum=sum(min_temp)
        Rain_sum=sum(Rain)
        SRAD_len=len(SRAD)
        max_temp_len=len(max_temp)
        min_temp_len=len(min_temp)
        Rain_len=len(Rain)
        SRAD_avg=SRAD_sum/SRAD_len
        SRAD_avg=round(SRAD_avg,2)
        max_temp_avg=max_temp_sum/max_temp_len
        max_temp_avg=round(max_temp_avg,2)
        min_temp_avg=min_temp_sum/min_temp_len
        min_temp_avg=round(min_temp_avg,2)
        Rain_avg=Rain_sum/Rain_len
        Rain_avg=round(Rain_avg,2)
        SRAD_year.append(SRAD_avg)
        max_temp_year.append(max_temp_avg)
        min_temp_year.append(min_temp_avg)
        Rain_year.append(Rain_avg)

# -------------------------------------annual_solar_radiation--------------------------------------------
fig, ax = plt.subplots()
colors = [plt.cm.Blues(i / len(SRAD_year)) for i in range(len(SRAD_year))]
bars = ax.bar(year, SRAD_year, color=colors)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 1), ha='center', va='bottom', fontsize=8)
colors = np.linspace(0, 1, len(year))
cmap = ['lightgreen', 'darkgreen']
plt.plot(year, SRAD_year, color='darkgreen', linestyle=':', linewidth=2, markersize=8)  # 自定义颜色和线宽
ax.set_title('Average annual solar radiation')
ax.set_xlabel('Years', fontsize=15)
ax.set_ylabel('SRAD(MJ/m² day)', fontsize=15)
ax.tick_params(axis='both', labelsize=12)
ax.fill_between(year, max_temp_year, color='red', alpha=0.3)

plt.title('Average annual solar radiation', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('SRAD(MJ/m² day)', fontsize=12)
plt.xticks(year[::6],)
plt.savefig('fig_8_annual_solar_radiation.pdf', format='pdf')
plt.show()

# -------------------------------------annual_maximum_temperature--------------------------------------------
fig, ax = plt.subplots()
plt.plot(year, max_temp_year ,color='red', linestyle='-.', linewidth=2, )  # 自定义颜色和线宽
ax.fill_between(year, max_temp_year, color='red', alpha=0.3)
plt.title('Average annual maximum temperature', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('TMAX(℃)', fontsize=12)
plt.xticks(year[::6],)
plt.savefig('fig_8_annual_maximum_temperature.pdf', format='pdf')
plt.show()

# -------------------------------------annual_maximum_temperature--------------------------------------------
fig, ax = plt.subplots()
plt.plot(year, min_temp_year ,color='red', linestyle='-.', linewidth=2, )  # 自定义颜色和线宽
ax.fill_between(year, min_temp_year, color='red', alpha=0.3)
plt.title('Average annual minimum temperature', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('Tmin(℃)', fontsize=12)
plt.xticks(year[::6],)
plt.savefig('fig_8_annual_minimum_temperature.pdf', format='pdf')
plt.show()

# -------------------------------------annual_Rainfall--------------------------------------------
fig, ax = plt.subplots()
plt.plot(year, Rain_year ,color='dodgerblue',linestyle='-.', linewidth=2, )  # 自定义颜色和线宽
ax.fill_between(year, Rain_year, color='blue',alpha=0.3 )
plt.title('Average annual Rainfall', fontsize=16, fontweight='bold')
plt.xlabel('Years', fontsize=12)
plt.ylabel('Rain(mm)', fontsize=12)
plt.xticks(year[::6],)
plt.savefig('fig_8_annual_Rainfall.pdf', format='pdf')
plt.show()