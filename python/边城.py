import requests
from lxml import etree
from selenium import webdriver

url = 'https://www.zhonghuadiancang.com/wenxueyishu/11112/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
bro = webdriver.Edge(executable_path='D:/Python310/msedgedriver.exe')
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
page_text = response.text
tree = etree.HTML(page_text)
content_introduce = tree.xpath('/html/body/div[2]/div[2]/div[1]/div/div[3]/p/text()')[0]
li_list = tree.xpath('//*[@id="booklist"]/li')
fp = open('./边城.txt','a',encoding='utf-8')
for li in li_list:
    title = li.xpath('./a/text()')[0]
    fp.write(title+'\n')
    detail_url = li.xpath('./a/@href')[0]
    bro.get(detail_url)
    detail_page_text = bro.page_source
    tree2 = etree.HTML(detail_page_text)
    p_list = tree2.xpath('//*[@id="content"]/p/text()')
    for p in p_list:
        fp.write(p+'\n')
    print(title+'爬取完成!!!')
fp.close()