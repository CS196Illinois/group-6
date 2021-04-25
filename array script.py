from datetime import datetime
import pandas as pd
from os import listdir
import datetime
import requests

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#path to labels
path = (r"C:\Users\Denny\Desktop\cs196 project\labels")

#functions to create lists of data
def file_names():
    file_list = []
    for file in listdir(path):
        file_list.append(file)
    return file_list

def hex_times():
    hex_list = []
    for file in file_names():
        hex_list.append(file.replace("quadcam_","").replace(".txt",""))
    return hex_list

def unix_times():
    unix_list = []
    for hex_time in hex_times():
        unix_list.append(int(hex_time,16))
    return unix_list

def date_times():
    date_list = []
    for unix_time in unix_times():
        date = datetime.datetime.fromtimestamp(int(str(unix_time)[:10])).strftime('%Y-%m-%d %H:%M:%S')
        date_list.append(date)
    return date_list

def activity(type):
    return_list = []
    for file in listdir(path):
        count = 0
        with open(r"C:\Users\Denny\Desktop\cs196 project\labels\\" + file, "r") as fl:
            for line in fl.readlines():
                if line[0] == type:
                    count += 1
            return_list.append(count)
    return return_list

def total_activity():
    return_list = []
    for file in listdir(path):
        with open(r"C:\Users\Denny\Desktop\cs196 project\labels\\" + file, "r") as fl:
            return_list.append(len(fl.readlines()))
    return return_list

def weather():
    pass


#not sure why requests are not working, getting a respose of 401 (error with api key)
"""
payload = {"x-api-key": "rIp4xQb45wMKhFJg6ELrYECBiVTIlz3M", "lat" : "40.1020", "lon" : "88.2272", "start" : "2021-04-23", "end" : "2021-04-24"}
r = requests.get('https://api.meteostat.net/v2/point/hourly', params=payload)
print(r)
"""

#creating array with pandas
df = {
"file_name" : file_names(),
"hex_time" : hex_times(),
"unix_time" : unix_times(),
"date_time" : date_times(),
"activity 0" : activity("0"),
"activity 1" : activity("1"),
"activity 2" : activity("2"),
"total_activity" : total_activity()
}


df = pd.DataFrame(df, columns=["file_name","hex_time","unix_time","date_time","activity 0","activity 1","activity 2","total_activity"])


#example seaborn plot with total activity over time on the quad
ax = sns.lineplot(x = "date_time", y= "total_activity", data = df)
plt.show()
