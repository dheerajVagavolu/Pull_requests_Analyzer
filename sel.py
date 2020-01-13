import requests
from bs4 import BeautifulSoup
import sys
#change link and num of pages

link = sys.argv[1]
PAGES = int(sys.argv[2]) 

print(link)
name = link.split('/')[1]

DATASET = []
f = open(name+'_logs_new.txt','w')
for num in range(PAGES):

    r = requests.get('https://github.com/'+link+'/pulls?q=is%3Apr+is%3Aclosed&page='+str(num+1))
    soup = BeautifulSoup(r.content, 'html.parser')
    files = soup.find_all('a', class_='link-gray-dark v-align-middle no-underline h4 js-navigation-open')
    dates = soup.find_all('relative-time', class_='no-wrap')
    markers = soup.find_all('span', class_='tooltipped tooltipped-e')
    

    for i in range(len(files)):

        DATA_ELE = {}

        print(files[i].text)
        
        f.write(files[i].text+' |-\|/-| ')
        DATA_ELE['title'] = files[i].text

        #Datetime

        print(dates[i].get('datetime'))
        
        f.write(str(dates[i].get('datetime'))+' ')
        DATA_ELE['date'] = dates[i].get('datetime')
        
        #Link

        print(files[i].get('href'))

        print(markers[i].get('aria-label'))

        f.write(markers[i].get('aria-label') + ' |-\|/-| ')
        
        f.write(files[i].get('href').split('/')[-1]+' ')
        git_files = 'https://github.com'+files[i].get('href')+'/files'
        print(git_files)
        change = requests.get(git_files)

        #Files changed

        file_change = BeautifulSoup(change.content, 'html.parser')
        diff_add = file_change.find_all('span' ,class_='text-green')
        diff_del = file_change.find_all('span' ,class_='text-red')
        print('\n')
        print(diff_add[0].text.strip())
        
        f.write(diff_add[0].text.strip()+' ')
        print(diff_del[0].text.strip())
        
        f.write(diff_del[0].text.strip()+' ')
        print('\n')


        #Which files changed
        
        
        extensions = []
        count = 0

        changed_names = file_change.find_all('div', class_='file-info flex-auto')
        for file_names in changed_names:
            real_name = file_names.find_all('a', class_='link-gray-dark')
            extension = real_name[0].get('title').split('.')[-1]
            if extension not in ['md','txt']:
                count = count + 1
            if extension not in extensions:
                extensions.append(extension)
                f.write(extension+' ')
        
        f.write(str(count)+'|-\|/-| \n')
        
        DATA_ELE['file_ext'] = extensions
        DATASET.append(DATA_ELE)
        print(extensions)

# print(DATASET)
print(len(DATASET))

f.close()