from selenium import webdriver
from selenium.webdriver.edge.options import Options
import requests
from lxml import etree

url = 'http://book.sbkk8.com/xiandai/liucixinzuopinji/qiuzhuangshandian/'
edge_option = Options()
edge_option.add_argument("--headless")
edge_option.add_argument("--disable-gpu")
bro = webdriver.Edge(executable_path='D:/Python310/msedgedriver.exe',options=edge_option)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
tree1 = etree.HTML(page_text)
li_list = tree1.xpath('//*[@id="left"]/div[2]/ul/li')
for li in li_list:
    content_url = 'http://book.sbkk8.com'+li.xpath('./a/@href')[0]
    bro.get(url=content_url)
    content_page_text = bro.page_source
    tree2 = etree.HTML(content_page_text)
    title = tree2.xpath('//*[@id="maincontent1"]/h1/text()')[0]
    content_page = bro.find_element('xpath', '//*[@id="content"]/p').text
    with open('./球状闪电.txt','a', encoding='utf-8') as fp:
        fp.write(title+'\n'+content_page)
        print(title+'爬取完成!!!')
