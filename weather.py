import os
import sys
import csv
from datetime import datetime


months =[]

def main():
    if str.upper(sys.argv[1]) == 'YEAR':
        yr = sys.argv[2]
        val1 = yearcalc(yr)
        reportone(val1)
    elif str.upper(sys.argv[1]) == 'MONTH':
        mn = sys.argv[2].split('/')
        val2 = monthcalc(mn)
        reporttwo(val2)
    else:
        print("Please check input parameters")
        exit


def yearcalc(y):
    mx_tmp = 0
    mx_hum = 0
    mn_tmp = 100
    os.chdir(r'C:\Som\Personal Projects\weatherdata')
    for f in os.listdir():
        if f.__contains__(y):
            months.append(f)
    for month in months:
        with open (f'C:\\Som\\Personal Projects\\weatherdata\\{month}','r') as data_file:
            #with open (r'C:\Som\Personal Projects\weatherdata\lahore_weather_1996_Dec.txt','r') as data_file:
            csv_data = csv.reader(data_file, delimiter=',')
            csv_data.__next__()
            csv_data.__next__()
            for line in csv_data:
                if line[0].__contains__('<!'):
                    break
                else:
                    if line[1] == '' and line[3] == '' and line[7] == '':
                        continue
                    else:
                        if int(line[1]) >= mx_tmp:
                            mx_tmp = int(line[1])
                            mx_dt = line[0]
                        if int(line[3]) <= mn_tmp:
                            mn_tmp = int(line[3]) 
                            mn_dt = line[0]
                        if int(line[7]) >= mx_hum:
                            mx_hum = int(line[7]) 
                            hum_dt = line[0]


    def convert_list_to_date(dt):
        ''.join(dt)
        dt_obj = datetime.strptime(dt,'%Y-%m-%d')
        c_dt = dt_obj.strftime("%b %d")
        return c_dt

    # converted_dt = convert_list_to_string(mx_dt)
    # dt_obj = datetime.strptime(converted_dt,'%Y-%m-%d')
    # c_dt = dt_obj.strftime("%b %d")
    cmx_dt = convert_list_to_date(mx_dt)
    cmn_dt = convert_list_to_date(mn_dt)
    chum_dt = convert_list_to_date(hum_dt)

    # print(f"Highest: {mx_tmp}C on {cmx_dt}")
    # print(f"Lowest: {mn_tmp}C on {cmn_dt}")
    # print(f"Humidity: {mx_hum}% on {chum_dt}")
    return [mx_tmp,cmx_dt,mn_tmp,cmn_dt,mx_hum,chum_dt]

def monthcalc(m):
    highest_tmp = 0
    lowest_tmp = 0
    mean_hum = 0
    cnt = 0
    str_mn = ''.join(m)
    dt = datetime.strptime(str_mn, "%Y%m")
    c_dt = str(dt.strftime("%Y_%b"))
    os.chdir(r'C:\Som\Personal Projects\weatherdata')
    for f in os.listdir():
        #print(f)
        if f.__contains__(c_dt):
            with open (f'C:\\Som\\Personal Projects\\weatherdata\\{f}','r') as data_file:

                csv_data = csv.reader(data_file, delimiter=',')
                csv_data.__next__()
                csv_data.__next__()
                for line in csv_data:
                    if line[0].__contains__('<!'):
                        break
                    else:
                        if line[1] == '' and line[3] == '' and line[7] == '':
                            continue
                        else:
                            highest_tmp += int(line[1])
                            lowest_tmp += int(line[3])
                            mean_hum += int(line[8])
                            cnt += 1
            avg_high = highest_tmp/cnt
            avg_low = lowest_tmp/cnt
            avg_hum = mean_hum/ cnt
            return [avg_high,avg_low,avg_hum]
    
def reportone(v1):
    print(f"Highest: {v1[0]}C on {v1[1]}")
    print(f"Lowest: {v1[2]}C on {v1[3]}")
    print(f"Humidity: {v1[4]}% on {v1[5]}")

def reporttwo(v2):
    print(f"Highest Aerage: {v2[0]}C")
    print(f"Lowest Average: {v2[1]}C")
    print(f"Average Mean Humidity: {v2[2]}%")

if __name__ == '__main__':
    main()

