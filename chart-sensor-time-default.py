# @Descripttion ：
# -*- codeing: utf-8 -*-
# @time ：2024/12/14 23:38
# @Author : Ruifeng Xu
# @Site : 
# @file : chart-sensor-time-default.py
# @Sofeware : PyCharm




import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.pyplot as plt




# -----------------------------------------------sensor time default analysis-------------------------------

def sensor_data_analysis(file_path):
    ConductSensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='ConductSensor', skiprows=1)
    HeatFluxSensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='HeatFluxSensor', skiprows=1)
    HumiditySensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='HumiditySensor', skiprows=1)
    InsectSensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='InsectSensor', skiprows=1)
    PHSensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='PHSensor', skiprows=1)
    SoilNutSensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='SoilNutSensor', skiprows=1)
    SporeSensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='SporeSensor', skiprows=1)
    TemSensor = pd.read_excel(file_path, engine='openpyxl', sheet_name='TemSensor', skiprows=1)


    date_range = pd.date_range(start='2024-07-01', end='2024-09-20', freq='D').date
    sensors =['Conduct','HeatFlux',
              'Humidity','Insect','PH','SoilNut','Spore','Tem']
    continuous_data = pd.DataFrame(index=date_range,columns=[sensor for sensor in sensors])

    Cotton_ConductSensor_default = ConductSensor.loc[:, ["数据采集时间"]]
    Cotton_HeatFluxSensor_default = HeatFluxSensor.loc[:, ["数据采集时间"]]
    Cotton_HumiditySensor_default = HumiditySensor.loc[:, ["数据采集时间"]]
    Cotton_InsectSensor_default = InsectSensor.loc[:, ["数据采集时间"]]


    Cotton_PHSensor_default = PHSensor.loc[:, ["数据采集时间"]]
    Cotton_SoilNutSensor_default = SoilNutSensor.loc[:, ["数据采集时间"]]
    Cotton_SporeSensor_default = SporeSensor.loc[:, ["数据采集时间"]]
    Cotton_TemSensor_default = TemSensor.loc[:, ["数据采集时间"]]
    Cotton_ConductSensor_default['数据采集时间'] = pd.to_datetime(Cotton_ConductSensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date
    Cotton_HeatFluxSensor_default['数据采集时间'] = pd.to_datetime(Cotton_HeatFluxSensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date
    Cotton_HumiditySensor_default['数据采集时间'] = pd.to_datetime(Cotton_HumiditySensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date
    Cotton_InsectSensor_default['数据采集时间'] = pd.to_datetime(Cotton_InsectSensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date
    Cotton_PHSensor_default['数据采集时间'] = pd.to_datetime(Cotton_PHSensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date
    Cotton_SoilNutSensor_default['数据采集时间'] = pd.to_datetime(Cotton_SoilNutSensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date
    Cotton_SporeSensor_default['数据采集时间'] = pd.to_datetime(Cotton_SporeSensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date
    Cotton_TemSensor_default['数据采集时间'] = pd.to_datetime(Cotton_TemSensor_default['数据采集时间'], format='%Y-%m-%d %H:%M:%S').dt.date


    sensors_default=[Cotton_ConductSensor_default,Cotton_HeatFluxSensor_default,
                     Cotton_HumiditySensor_default,Cotton_InsectSensor_default,
                     Cotton_PHSensor_default,Cotton_SoilNutSensor_default,Cotton_SporeSensor_default,Cotton_TemSensor_default]

    for sensor ,sensor_default in zip(continuous_data.columns,sensors_default):
        for date in continuous_data.index:

            matched_rows = sensor_default[sensor_default['数据采集时间'] == date]
            if not matched_rows.empty:
                continuous_data.at[date, sensor] = matched_rows['数据采集时间'].iloc[0]

    return  continuous_data,sensors


# -----------------------------------------------Visualization of sensor time default analysis-------------------------------

file_path="Cotton or Wheat or Maize time default analysis"

continuous_data,sensors=sensor_data_analysis(file_path)
width_ratios = [1] * len(sensors)
sensors = continuous_data.columns
dates = continuous_data.index
fig, axes = plt.subplots(nrows=1, ncols=len(sensors), figsize=(12, 6), sharey=True,width_ratios=width_ratios)

colors =[cm.Blues(np.random.normal(loc=0.9, scale=0.3, size=1)[0]) for _ in sensors]
if len(sensors) == 1:
    axes = [axes]

datetime_index = pd.DatetimeIndex(continuous_data.index)
formatted_dates = datetime_index.strftime('%Y-%m-%d')

for i,(ax, sensor,color1) in enumerate(zip(axes, sensors,colors)):
    data_presence = np.where(continuous_data[sensor].notnull(), 1, 0)
    percentage_present = int(np.mean(data_presence)*100)
    ax.barh(dates,data_presence,label=sensor, height=1, align='center', color=color1)
    ax.set_xlabel(f'{sensor}:{percentage_present}% ',fontsize=12)
    ax.set_yticks([])
    ax.set_xticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)




num_ticks = 10
tick_interval = len(dates) // (num_ticks - 1) if len(dates) > num_ticks else 1
ticks = np.arange(0, len(dates), tick_interval)
plt.yticks(dates[ticks], fontsize=10)
fig.suptitle("Maize_default", fontsize=16)
plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
plt.tight_layout()
plt.savefig('flg_4_Maize_0701~0920_default.pdf', bbox_inches='tight',format='pdf')
plt.show()



