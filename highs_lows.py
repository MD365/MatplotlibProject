import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #读取了第0行

    dates,highs,lows=[], [],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")

            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,'mising data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


    # print(highs)
#根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates, highs,c='red')
plt.plot(dates,lows,c='blue')
plt.fill_between(dates,highs,lows,facecolor='blue')

#设置图形格式
plt.title("daily high temperatures",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdata()
plt.ylabel('temperature',fontsize=16)
plt.tick_params(axis='both',which='major', labelsize=16)

plt.show()