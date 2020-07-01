import requests
from requests_html import HTMLSession
import os

session = HTMLSession()
r = session.get('https://www.qomu.ge/')
links = r.html.links



p = os.getcwd()+'\qomu_ge'
os.mkdir(p)

for i in links:
    if not str(i).startswith('https'):
        try:
            full = requests.get('https://qomu.ge/' + i)
        except:
            print("shit")
        i = i.replace("/", "_").replace(".", "_").replace("?", "_")
        print(i)
        if full.status_code == 200:
            full = full.text
            with open(r'qomu_ge/{}.html'.format(i), 'w', encoding='utf-8') as f:
                f.write(full)

# def writeing(scraped_already):
#     desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#     file = desktop + r'\qomu_ge.txt'
#     to_write = open(file, 'w', encoding='utf-8')
#     to_write.write(scraped_already)
#     to_write.close()
