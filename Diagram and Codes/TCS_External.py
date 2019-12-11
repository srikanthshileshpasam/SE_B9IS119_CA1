#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas
from pandas import DataFrame
from datetime import datetime



import_csv = pandas.read_csv(r'/Users/srikanthshileshpasam/OneDrive - Dublin Business School (DBS)/Python/untitled.csv')
print(import_csv)
signal_data = import_csv.columns.tolist()
# print(signal_data)
date_time = datetime.now()
# print(date_time)

if signal_data[4] == 'TRUE':
    #Emergency vehicle operation mode:
    print('\nAlert!\nEVAS override of traffic signals!\nChanging all lanes to RED except for oncoming emergency vehicle.')

elif signal_data[5] == 'TRUE.1':
    #Pedestrian operation mode:
    print('\nPedestrian Crossing the lane.')

else:
    #Normal vehicle operation mode from red to green:
    if signal_data[2] == 'RED' and signal_data[3] == 'GREEN':
        print('\nChanging lane to green.')
        
    #Normal vehicle operation mode from green to red:
    elif signal_data[2] == 'GREEN' and signal_data[3] == 'RED':
        print('\nChanging lane to red.')
        
    else:
        #In case an error, creating an error log file for reference:
        print('\nInvalid code.\nError!\nCreating error log.')
        signal_data[1] = date_time
        error_log = pandas.DataFrame(signal_data, columns = ['Error logged at signal.'])
        print(error_log)


# In[ ]:





# In[ ]:




