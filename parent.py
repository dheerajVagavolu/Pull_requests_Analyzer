
import os
import sys

f = open('rapid.txt').readlines()

cur = os.getcwd()

for i in f:
    line = i.split(' ')
    cmd1 = 'python3 sel.py '+line[0]+' '+line[1]
    os.system(cmd1)
    cmd2 = 'git clone '+line[2]
    os.system(cmd2)
    dire = cur+'/'+line[0].split('/')[1]
    print(dire)
    os.chdir(dire)
    cmd4 = 'git log --tags --simplify-by-decoration --pretty="format:%ai %d" > tags_dates_'+line[0].split('/')[1]+'.txt'
    print(cmd4)
    os.system(cmd4)
    cmd5 = 'cp tags_dates_'+line[0].split('/')[1]+'.txt ../'
    os.system(cmd5)
    os.chdir(cur)
    cmd5 = 'python3 dates_plot.py '+ line[0].split('/')[1] +'_logs_new.txt tags_dates_'+line[0].split('/')[1]+'.txt'
    print(cmd5)
    os.system(cmd5)

# cmd_tags = 'git tag --sort=creatordate > tagnames.txt'
# os.system(cmd_tags)