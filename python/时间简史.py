import requests
from lxml import etree
from selenium import webdriver

bro1 = webdriver.Edge(executable_path='C:/Users/hwh6688/OneDrive/桌面/edgedriver_win64/msedgedriver.exe')
url = 'https://99csw.com/book/1655/index.htm'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

response  = requests.get(url,headers=headers)
response.encoding = 'utf-8'
page_text = response.text
tree = etree.HTML(page_text)
dd_list = tree.xpath('//*[@id="dir"]/dd')
for dd in dd_list:
    content_url = 'https://99csw.com/'+dd.xpath('./a/@href')[0]
    content_name = dd.xpath('./a/text()')[0]
    bro1.get(url=content_url)
    detail_page_text = bro1.page_source
    tree2 = etree.HTML(detail_page_text)
    content_title = tree2.xpath('//*[@id="content"]/h2/text()')[0]
    div_list = tree2.xpath('//*[@id="content"]/div/text()')
    fp = open('./时间简史.txt', 'a', encoding='utf-8')
    fp.write(content_title+'\n')
    for div in div_list:
        fp.write(div+'\n')
    print(content_name+'爬取完成')
fp.close()
