import pandas as pd
from os import listdir
import datetime
import requests
import json
import time



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

def temperature():
    return_list = []
    day = date_times()[0]
    day = str(day)[:10]
    current_temp = get_avg_temp(day)


    for date in date_times():
        if date[:10] == day:
            return_list.append(float(current_temp))
        else:
            current_temp = get_avg_temp(date[:10])
            day = date[:10]
            return_list.append(current_temp)

    return return_list


def get_avg_temp(d):
    time.sleep(0.5)
    header = {"x-api-key": "rIp4xQb45wMKhFJg6ELrYECBiVTIlz3M"}
    payload = {"lat" : "40.1020", "lon" : "-88.2272", "start" : d, "end" : d}
    r = requests.get('https://api.meteostat.net/v2/point/daily', params=payload, headers=header)
    json_data = json.loads(r.text)
    data = json_data["data"]
    return data[0]["tavg"]





#creating array with pandas
df = {
"date_time" : date_times(),
"activity 0" : activity("0"),
"activity 1" : activity("1"),
"activity 2" : activity("2"),
"total_activity" : total_activity(),
"temperature" : temperature()
}


df = pd.DataFrame(df, columns=["date_time","activity 0","activity 1","activity 2","total_activity","temperature"])
df.to_csv('cs196_dataframe.csv',index=False)
