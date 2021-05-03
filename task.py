# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:49:44 2021

@author: asus
"""

import pandas as pd
fire_and_ambulance=pd.read_csv('FireBrigadeAndAmbulanceCallOuts.csv')
num_of_rows=fire_and_ambulance.shape[0]
num_of_cols=fire_and_ambulance.shape[1]
print("\nNumber of rows:" ,num_of_rows)
print("Number of columns:" ,num_of_cols)
non_null_rows_count=fire_and_ambulance.notnull().sum()
print("\nNumber of non-null values (by column):\n" ,non_null_rows_count)
null_rows_count=fire_and_ambulance.isnull().sum()
print("\nNumber of null values (by column):\n" ,null_rows_count)
total_null_count=fire_and_ambulance.isnull().sum().sum()
print("\nNumber of null values for all columns:\n" ,total_null_count)
call_out_by_stationarea = pd.DataFrame(fire_and_ambulance.groupby('Station Area').size())
print("\nTotal number of call outs by Station Area:\n", call_out_by_stationarea)
call_out_by_stationarea_and_date = pd.DataFrame(fire_and_ambulance.groupby(by=['Date','Station Area']).size())
print("\nTotal number of call outs by Date and Station Area:\n", call_out_by_stationarea_and_date)
filter=['Fire CAR','Fire ALARM']
fire_data=fire_and_ambulance.loc[fire_and_ambulance['Description'].isin(filter)]
fire_callout = pd.DataFrame(fire_data.groupby(by=['Station Area','Date']).size())
print("\nTotal number of call outs by Station Area and Date where the description is either Fire Car or Fire Alarm:\n",fire_callout)
replace_comma_and_dash=fire_and_ambulance.replace(',',' ', regex=True)
replace_comma_and_dash=replace_comma_and_dash.replace('-',' ', regex=True)
drop_null_rows=replace_comma_and_dash.dropna(subset=['AH','MAV','CD'])
drop_duplicate_rows=drop_null_rows.drop_duplicates()
min_time_diff= pd.DataFrame(pd.to_datetime(fire_and_ambulance.ORD)-pd.to_datetime(fire_and_ambulance.TOC))
print("\nminimum time difference between TOC and ORD:" ,min_time_diff)
cleaned_data= pd.DataFrame(drop_duplicate_rows)
print("\nCleaned final data:" ,cleaned_data)
