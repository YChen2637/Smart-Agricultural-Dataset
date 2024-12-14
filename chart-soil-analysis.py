# @Descripttion ：
# -*- codeing: utf-8 -*-
# @time ：2024/12/14 23:23
# @Author : Ruifeng Xu
# @Site : 
# @file : chart-soil-analysis.py
# @Sofeware : PyCharm


import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------soil data analysis.-----------------------------------------------------------

def soil_data_analysis(file_path):
    # ------------------------------------soil conduct------------------------------------------------
    Cotton_conduct = pd.read_excel(file_path,engine='openpyxl',sheet_name='ConductSensor',skiprows=1)
    Time_conduct=Cotton_conduct.loc[:,['数据采集时间','土壤电导率']]
    Time_conduct = pd.DataFrame(Time_conduct)
    Time_conduct['数据采集时间']=pd.to_datetime(Time_conduct['数据采集时间'], format='%m/%d/%y %H:%M:%S')
    Time_conduct.set_index('数据采集时间',inplace=True)
    group_day_conduct = Time_conduct.resample('D').agg(['sum', 'mean','std']).dropna()

    # --------------------------------------soil heatflux------------------------------------------------
    Cotton_heatflux = pd.read_excel(file_path,engine='openpyxl',sheet_name='HeatFluxSensor',skiprows=1)
    Time_heatflux=Cotton_heatflux.loc[:,['数据采集时间','土壤热通量']]
    Time_heatflux = pd.DataFrame(Time_heatflux)
    Time_heatflux["数据采集时间"]=pd.to_datetime(Time_heatflux['数据采集时间'], format='%m/%d/%y %H:%M:%S')
    Time_heatflux.set_index("数据采集时间",inplace=True)
    group_day_heatflux =Time_heatflux.resample("D").agg(['sum', 'mean','std']).dropna()
    group_day_heatflux.drop(group_day_heatflux[group_day_heatflux[('土壤热通量','sum')] > 5000].index, inplace=True)

    # -------------------------------------soil PH-------------------------------------------------------
    Cotton_PH = pd.read_excel(file_path,engine='openpyxl',sheet_name='PHSensor',skiprows=1)
    Time_PH=Cotton_PH.loc[:,['数据采集时间','土壤酸碱度']]
    Time_PH = pd.DataFrame(Time_PH)
    Time_PH["数据采集时间"]=pd.to_datetime(Time_PH['数据采集时间'], format='%m/%d/%y %H:%M:%S')
    Time_PH.set_index("数据采集时间",inplace=True)
    group_day_PH =Time_PH.resample("D").agg(['sum', 'mean','std']).dropna()

    # --------------------------------------soil Humidity------------------------------------------------
    Cotton_Humidity = pd.read_excel(file_path,engine='openpyxl',sheet_name='HumiditySensor',skiprows=1)
    Time_Humidity=Cotton_Humidity.loc[:,['数据采集时间','土壤湿度']]
    Time_Humidity = pd.DataFrame(Time_Humidity)
    Time_Humidity["数据采集时间"]=pd.to_datetime(Time_Humidity['数据采集时间'], format='%m/%d/%y %H:%M:%S')
    Time_Humidity.set_index("数据采集时间",inplace=True)
    group_day_Humidity =Time_Humidity.resample("D").agg(['sum', 'mean','std']).dropna()
    return group_day_conduct,group_day_heatflux,group_day_PH,group_day_Humidity




# -------------------------------------------Visualization of crop soil analysis-----------------------------------------------------------
file_path="Cotton or Wheat or Maize soil data"
group_day_conduct,group_day_heatflux,group_day_PH,group_day_Humidity=soil_data_analysis(file_path)
plt.figure(figsize=(14, 8))
plt.plot(group_day_conduct.index, group_day_conduct[('土壤电导率', 'mean')], linestyle=':', markersize=5, linewidth=2, color='blue', label='Soil Conductivity')
plt.plot(group_day_Humidity.index, group_day_Humidity[('土壤湿度', 'mean')],linestyle='-', markersize=5, linewidth=2, color='green', label='Soil Humidity')
plt.plot(group_day_PH.index, group_day_PH[('土壤酸碱度', 'mean')],  linestyle='--', markersize=5, linewidth=2, color='red', label='Soil PH')
plt.plot(group_day_heatflux.index, group_day_heatflux[('土壤热通量', 'mean')],  linestyle='-.', markersize=5, linewidth=2, color='purple', label='Soil Heatflux')
plt.legend(loc='best', fontsize='large')
plt.title('Soil Parameters Over Time', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Mean Value', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.savefig('flg_6_wheat_time_data_correct.pdf', format='pdf')


