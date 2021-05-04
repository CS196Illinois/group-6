import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




csv_path = r"C:\Users\Denny\group-6\activity_over_time.csv"
df = pd.read_csv(csv_path)


df['time'] = df['time'].apply(lambda x: x/1000)
df.groupby('time').mean()

x = df['time']
y_lounging = df['lounging']
y_activity = df['activity']
y_traversing = df['traversing']


# just getting all of the x,y pairs we'll need

# older versions of matplotlib require us to do some weird stuff with Axes. newer versions (2.1 and maybe some before) make it easier
# folloiwng https://stackoverflow.com/questions/4270301/matplotlib-multiple-datasets-on-the-same-scatter-plot
plt.scatter(x, y_lounging, c="r", label="lounging", s=10) # c is for 'color', options here https://matplotlib.org/2.0.2/api/colors_api.html
plt.scatter(x, y_activity, c="g", label="activity", s=10)
plt.scatter(x, y_traversing , c="b", label="traversing", s=10)

plt.title('Activity over time')
plt.xlabel('Time (unix)')
plt.ylabel('Number of people')
plt.legend(['Lounging','Activity','Traversing'])

plt.show()
