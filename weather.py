import os
import sys
import csv
from datetime import datetime
from pathlib import Path

data_folder = os.path.dirname(os.path.abspath(__file__))

def main():
    if str.upper(sys.argv[1]) == 'YEAR':
        yr = sys.argv[2]
        yr_data = year_calculator(yr)
        yearly_report(yr_data)
    elif str.upper(sys.argv[1]) == 'MONTH':
        mo = sys.argv[2].split('/')
        mo_data = month_calculator(mo)
        monthly_report(mo_data)
    else:
        print("Please check input parameters")
        exit


def year_calculator(yr):
    max_tmp = 0
    max_hum = 0
    min_tmp = 100
    os.chdir(data_folder)
    for file in os.listdir():
        if yr in file:
            with open (f'{data_folder}/{file}','r') as data_file:
                csv_data = csv.reader(data_file, delimiter=',')
                next(csv_data)
                next(csv_data)
                # csv_data.__next__()
                # csv_data.__next__()
                for line in csv_data:
                    if line[0].startswith("<!"):
                        break
                    else:
                        if line[1] == '' and line[3] == '' and line[7] == '':
                            continue
                        else:
                            if int(line[1]) >= max_tmp:
                                max_tmp = int(line[1])
                                maxtmp_dt = line[0]
                            if int(line[3]) <= min_tmp:
                                min_tmp = int(line[3]) 
                                mintmp_dt = line[0]
                            if int(line[7]) >= max_hum:
                                max_hum = int(line[7]) 
                                maxhum_dt = line[0]

    c_maxtmp_dt = string_to_date(maxtmp_dt)
    c_mintmp_dt = string_to_date(mintmp_dt)
    c_maxhum_dt = string_to_date(maxhum_dt)

    return [max_tmp,c_maxtmp_dt,min_tmp,c_mintmp_dt,max_hum,c_maxhum_dt]

def string_to_date(dt):
    dt_obj = datetime.strptime(dt,'%Y-%m-%d')
    c_dt = dt_obj.strftime("%b %d")
    return c_dt


def month_calculator(mo):
    sum_high_tmp = 0
    sum_low_tmp = 0
    sum_mean_hum = 0
    count = 0
    str_mo = ''.join(mo)
    dt = datetime.strptime(str_mo, "%Y%m")
    c_dt = str(dt.strftime("%Y_%b"))
    os.chdir(data_folder)
    for file in os.listdir():
        if c_dt in file:
            with open (f'{data_folder}/{file}','r') as data_file:
                csv_data = csv.reader(data_file, delimiter=',')
                next(csv_data)
                next(csv_data)
                for line in csv_data:
                    if line[0].startswith("<!"):
                        break
                    else:
                        if line[1] == '' and line[3] == '' and line[7] == '':
                            continue
                        else:
                            sum_high_tmp += int(line[1])
                            sum_low_tmp += int(line[3])
                            sum_mean_hum += int(line[8])
                            count += 1
            avg_high = sum_high_tmp/count
            avg_low = sum_low_tmp/count
            avg_hum = sum_mean_hum/ count
            return [avg_high,avg_low,avg_hum]
    
def yearly_report(data_year):
    print(f"Highest: {data_year[0]}C on {data_year[1]}")
    print(f"Lowest: {data_year[2]}C on {data_year[3]}")
    print(f"Humidity: {data_year[4]}% on {data_year[5]}")

def monthly_report(data_mo):
    print(f"Highest Aerage: {data_mo[0]}C")
    print(f"Lowest Average: {data_mo[1]}C")
    print(f"Average Mean Humidity: {data_mo[2]}%")

if __name__ == '__main__':
    main()

