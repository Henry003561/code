import os
import requests
from lxml import etree
# 创建数据储存文件
if not os.path.exists('./数据集'):
    os.mkdir('./数据集')
# 发起网络请求
url = "https://archive.ics.uci.edu/ml/index.php"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
page_text = requests.get(url=url, headers=headers).text
# 对数据进行解析
tree = etree.HTML(page_text)
td_list = tree.xpath("/html/body/table[3]/tr/td")
print(td_list)
for x in range(1,3):
    td = td_list[x]
    tr_list = td.xpath('./table/tr')
    for y in range(1, len(tr_list)):
        tr = tr_list[y]
        detail_url = 'https://archive.ics.uci.edu/ml/'+tr.xpath('./td[2]/table/tr/td[2]/span/a/@href')[0] #获取详情页的url
        detail_title = tr.xpath('./td[2]/table/tr/td[2]/span/a/text()')[0]
        fp1 = './数据集/%s'%detail_title
        if not os.path.exists(fp1):
            os.mkdir(fp1)
        detail_page_text = requests.get(url=detail_url, headers=headers).text
        tree2 = etree.HTML(detail_page_text)
        data_url_list = tree2.xpath('//span[@class="normal"]/a[1]/@href')
        data_url ='https://archive.ics.uci.edu/ml/machine-learning-databases/'+data_url_list[1].split('/')[-2]
        try:
            data_folder = requests.get(url=data_url, headers=headers).text
        except requests.exceptions.HTTPError or requests.exceptions.RequestException:
            pass
        tree3 = etree.HTML(data_folder)
        li_list = tree3.xpath('/html/body/ul/li')
        for t in range(1,len(li_list)):
            li = li_list[t]
            download_url = data_url+'/'+li.xpath("./a/@href")[0]
            download_title = li.xpath('./a/text()')[0]
            content_code = requests.get(url=download_url, headers=headers).content
            fileName = fp1+'/'+download_title
            with open(fileName, 'wb') as fp:
                fp.write(content_code)
                print(detail_title+'爬取完成!!!')