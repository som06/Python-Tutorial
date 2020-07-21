import os
import sys
import csv
from datetime import datetime
from pathlib import Path

DATA_FOLDER = os.path.dirname(os.path.abspath(__file__))

def main():
    if str.upper(sys.argv[1]) == 'YEAR':
        year = sys.argv[2]
        year_data = year_calculator(year)
        yearly_report(year_data)
    elif str.upper(sys.argv[1]) == 'MONTH':
        month = sys.argv[2].split('/')
        month_data = month_calculator(month)
        monthly_report(month_data)
    else:
        print("Please check input parameters")
        exit

'''Calculation based on year input'''

def year_calculator(year):
    max_tmp = 0
    max_hum = 0
    min_tmp = 100

    with os.scandir(DATA_FOLDER) as data_files:
        for file in data_files:
            if year in file.name:
                with open (f'{file.name}','r') as data_f:
                        data_f.readline()    
                        reader = csv.DictReader(data_f, restkey=None, restval=None)
                        for line in reader:
                            if line["Max TemperatureC"] is None or line["Max TemperatureC"] == '':
                                continue
                            else:
                                if int(line["Max TemperatureC"]) >= max_tmp:
                                    max_tmp = int(line["Max TemperatureC"])
                                    maxtmp_dt = line["PKT"]
                                if int(line["Min TemperatureC"]) <= min_tmp:
                                    min_tmp = int(line["Min TemperatureC"]) 
                                    mintmp_dt = line["PKT"]
                                if int(line["Max Humidity"]) >= max_hum:
                                    max_hum = int(line["Max Humidity"]) 
                                    maxhum_dt = line["PKT"]
            else:
                pass
    c_maxtmp_dt = string_to_date(maxtmp_dt)
    c_mintmp_dt = string_to_date(mintmp_dt)
    c_maxhum_dt = string_to_date(maxhum_dt)

    return [max_tmp,c_maxtmp_dt,min_tmp,c_mintmp_dt,max_hum,c_maxhum_dt]

def string_to_date(dt):
    dt_obj = datetime.strptime(dt,'%Y-%m-%d')
    return dt_obj.strftime("%b %d")

'''Calculation based on year input'''
def month_calculator(month):
    sum_high_tmp = 0
    sum_low_tmp = 0
    sum_mean_hum = 0
    count = 0
    str_month = ''.join(month)
    dt = datetime.strptime(str_month, "%Y%m")
    c_dt = str(dt.strftime("%Y_%b"))
    with os.scandir(DATA_FOLDER) as data_files:
        for file in data_files:
            if c_dt in file.name:
                with open (f'{file.name}','r') as data_f:
                        data_f.readline()    
                        reader = csv.DictReader(data_f, restkey=None, restval=None)
                        for line in reader:
                            if line["Max TemperatureC"] is None or line["Max TemperatureC"] is '':
                                continue
                            else:
                                sum_high_tmp += int(line["Max TemperatureC"])
                                sum_low_tmp += int(line["Min TemperatureC"])
                                sum_mean_hum += int(line[" Mean Humidity"])
                                count += 1
                avg_high = sum_high_tmp/count
                avg_low = sum_low_tmp/count
                avg_hum = sum_mean_hum/ count
                return [avg_high,avg_low,avg_hum]
'''Report-1'''    
def yearly_report(data_year):
    print(f"Highest: {data_year[0]}C on {data_year[1]}")
    print(f"Lowest: {data_year[2]}C on {data_year[3]}")
    print(f"Humidity: {data_year[4]}% on {data_year[5]}")
'''Report-2'''    
def monthly_report(data_month):
    print(f"Highest Aerage: {data_month[0]}C")
    print(f"Lowest Average: {data_month[1]}C")
    print(f"Average Mean Humidity: {data_month[2]}%")

if __name__ == '__main__':
    main()