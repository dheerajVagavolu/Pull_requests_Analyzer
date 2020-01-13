import datetime
import random
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

###########################################
#for vertical_lines
#git log --tags --simplify-by-decoration --pretty="format:%ai %d"


logs = sys.argv[1]
tags = sys.argv[2]

f_da = open(tags).readlines()
lines = []
for j in f_da:
    j_ar = j.split(' ')
    dd = j_ar[0].split('-')
    tt = j_ar[1].split(':')

    ele = datetime.datetime(int(dd[0]),int(dd[1]),int(dd[2]),int(tt[0]),int(tt[1]),int(tt[2]))
    lines.append(ele)

###########################################

f_op = open(logs).readlines()

info = [] 

for i in f_op:
    data = i.split('|-\|/-|')
    print(data)
    date_sent = data[1]
    print(date_sent)
    date_sent = date_sent.split(' ')
    date = date_sent[1]
    print(date)
    sent = data[2].split(' ')
    flag = 0
    
    if date_sent[2]=='Merged':
        print('merged')
        flag = 1

    add = sent[2][1:]
    dele = sent[3][1:]
    files = sent[-1]
    # print(date)
    zero = date
    date = zero.split('T')
    date[-1] = date[-1][:-1]
    #yy/mm/dd
    dd = date[0].split('-')
    #hh/mm/ss
    time = date[1].split(':')
    d1 = datetime.datetime(int(dd[0]),int(dd[1]),int(dd[2]), int(time[0]), int(time[1]), int(time[2]))
    arr = [d1, int(add.replace(',','')), int(dele.replace(',','')), int(files.replace(',',''))]
    if flag==1:
        info.append(arr)

# print(len(info))    

info.sort(key = lambda x: x[0])

# print(info)

x = []
add = []
dele = []
files = []

for i in range(len(info)):
    x.append(info[i][0])
    add.append(info[i][1])
    dele.append(info[i][2])
    files.append(info[i][3])



fig, (ax1,ax2,ax3) = plt.subplots(nrows = 3, ncols = 1)




ax1.plot(x,files, linewidth=0.4)
ax1.fill_between(x, 0, files)
# ax1.set_xticklabels(x, fontsize = 3) 


ax2.plot(x,add, color='green', linewidth=0.4)
ax2.fill_between(x, 0, add, facecolor='green')
# ax2.set_xticklabels(x, fontsize = 3) 


ax3.plot(x,dele, color='red', linewidth=0.4)
ax3.fill_between(x, 0, dele, facecolor='red')
# ax3.set_xticklabels([k.strftime("%x") for k in x], fontsize = 3) 


ax1.set_xlabel('File changes across releases', fontsize = 5)
ax2.set_xlabel('Lines added across releases',fontsize = 5)
ax3.set_xlabel('Lines deleted across releases',fontsize = 5)

ax1.set_yticks(np.arange(0, max(files), step=int((max(files)-min(files))/5)))
ax2.set_yticks(np.arange(0, max(add), step=int((max(add)-min(files))/5)))
ax3.set_yticks(np.arange(0, max(dele), step=int((max(dele)-min(files))/5)))

ax1.tick_params(axis='both', which='major', labelsize=4)
ax1.tick_params(axis='both', which='minor', labelsize=4)

ax2.tick_params(axis='both', which='major', labelsize=4)
ax2.tick_params(axis='both', which='minor', labelsize=4)

ax3.tick_params(axis='both', which='major', labelsize=4)
ax3.tick_params(axis='both', which='minor', labelsize=4)

for i in range(len(lines)):
    ax1.axvline(lines[i], color = 'black', linewidth=0.1)
    ax2.axvline(lines[i], color = 'black', linewidth=0.1)
    ax3.axvline(lines[i], color = 'black', linewidth=0.1)

for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(0.1)
    ax2.spines[axis].set_linewidth(0.1)
    ax3.spines[axis].set_linewidth(0.1)

fig.suptitle(logs.split('_')[0])

fig.tight_layout(pad=2.0)
plt.savefig(logs.split('_')[0]+'_pull_new.png', dpi = 1200)
