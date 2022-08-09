from lxml import etree
import os
import requests
from selenium import webdriver
bro = webdriver.Edge(executable_path='C:/Users/hwh6688/OneDrive/桌面/edgedriver_win64/msedgedriver.exe')
if not os.path.exists('./歌曲'):
    os.mkdir('./歌曲')

url = 'https://www.kugou.com/yy/singer/home/776661.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="song_container"]/li')
for li in li_list:
    detail_url = li.xpath('./a/@href')[0]
    detail_title = li.xpath('./a/span[4]/i/text()')[0]
    bro.get(url=detail_url)
    detail_page_text = bro.page_source
    tree2 = etree.HTML(detail_page_text)
    song_url = tree2.xpath('//*[@id="myAudio"]/@src')[0]
    song = requests.get(url=song_url, headers=headers).content
    filename = './歌曲/'+detail_title+'.mp3'
    with open(filename, 'wb') as fp:
        fp.write(song)
        print(detail_title+'爬取完成!!!')