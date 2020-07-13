import os
import sys
import csv
from datetime import datetime


def main():
    mx_tmp = 0
    mx_hum = 0
    mn_tmp = 100
    months =[]
    os.chdir(r'C:\Som\Personal Projects\weatherdata')
    for f in os.listdir():
        #fname = str(f.split('_'))
        #print(fname[2])
        #months.append(f)
        if f.__contains__(sys.argv[1]):
            months.append(f)
    #print(len(months))
    for month in months:
        with open (f'C:\Som\Personal Projects\weatherdata\{month}','r') as data_file:
            #with open (r'C:\Som\Personal Projects\weatherdata\lahore_weather_1996_Dec.txt','r') as data_file:
            csv_data = csv.reader(data_file, delimiter=',')
            csv_data.__next__()
            csv_data.__next__()
            for line in csv_data:
                if line[0].__contains__('<!'):
                    break
                else:
                    if line[1] == '' or line[3] == '' :
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


    def convert_list_to_date(dt, seperator=''):
        seperator.join(dt)
        dt_obj = datetime.strptime(dt,'%Y-%m-%d')
        c_dt = dt_obj.strftime("%b %d")
        return seperator.join(c_dt)

    # converted_dt = convert_list_to_string(mx_dt)
    # dt_obj = datetime.strptime(converted_dt,'%Y-%m-%d')
    # c_dt = dt_obj.strftime("%b %d")
    cmx_dt = convert_list_to_date(mx_dt)
    cmn_dt = convert_list_to_date(mn_dt)
    chum_dt = convert_list_to_date(hum_dt)

    print(f"Highest: {mx_tmp}C on {cmx_dt}")
    print(f"Lowest: {mn_tmp}C on {cmn_dt}")
    print(f"Humidity: {mx_hum}% on {chum_dt}")

if __name__ == '__main__':
    main()


