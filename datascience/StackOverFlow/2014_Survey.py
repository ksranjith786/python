# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import pandas as pd

data_frame = pd.read_csv('C:\\Users\\rk185212\\Google Drive\\Learning\\Git\\python\\survey\\stackoverflow\\2014 Stack Overflow Survey Responses\\2014 Stack Overflow Survey Responses.csv'
                         , usecols=[ 'C', 'C++', 'C#', 'Java', 'JavaScript', 'Node.js', 'Objective-C', 'PHP', 'Python', 'Ruby', 'SQL']
                         , header=1
                         )

print(data_frame)
print(data_frame.get(data_frame.columns[2]))
rows_count = data_frame.values
#plt.plot()
#print(rows_count)

