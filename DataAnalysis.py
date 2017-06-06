import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import csv

'''
Bay Area bike sharing data dump analysis file. 
CONTRIBUTORS:
			Henry Guerra
			Shan Hanadige
			Aarcon C. Gabriel
TODO:
	.....
'''

year1_weatherData = "~/Documents/2017/Documents/2017/babs_open_data_year_1/201402_babs_open_data/201402_weather_data.csv"

year1_weatherData_list = []
with open(year1_weatherData, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	year1_weatherData_list = [row for row in reader]
for row in range(24):
	print year1_weatherData_list[row]
