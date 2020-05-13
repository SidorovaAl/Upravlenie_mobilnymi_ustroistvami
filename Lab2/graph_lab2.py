import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import csv


IP = '217.15.20.194'
bytes = []
times = []
bam = 0

with open ('data_internet.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		if (row['sa'] == IP) or (row['da'] == IP):
			bam += (int(row['ibyt'])+int(row['obyt']))/1000000
			bytes.append(bam)
			times.append(datetime.strptime(row['ts'], '%Y-%m-%d %H:%M:%S'))

fig, ax = plt.subplots()
ax.plot(times, bytes, linewidth=0.6, color='navy')
ax.set_xlabel ('Time')
ax.set_ylabel ('Data, MB')
timestart = times[0].strftime('%d %b %Y, %H:%M:%S')
timestop = times[-1].strftime('%d %b %Y, %H:%M:%S')
title = 'Data transmitted by ' + IP + ' over time period\n' + timestart +' to '+ timestop
ax.set_title (title)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.grid(which='major', axis='both', color='silver', linestyle='dashed')

plt.savefig(fname='graph.png', dpi=1000, format='png')
