from datetime import datetime
import pandas as pd
from os import listdir
from os.path import isfile, join
import datetime

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





#creating array with pandas
df = {
"file_name" : file_names(),
"hex_time" : hex_times(),
"unix_time" : unix_times(),
"date_time" : date_times()
}


df = pd.DataFrame(df, columns=["file_name","hex_time","unix_time","date_time"])
