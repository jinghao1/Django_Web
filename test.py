import requests
from lxml import  etree
s_search="小菜园"
resqonse = requests.get("https://www.xiniudata.com/search2?name={}".format(s_search),
                   headers={"Cookie": "utoken=ND7HF4WRDLBINXYUL0A1TX576LHDF568"})
if resqonse.status_code == 200:

    # 获取页面资源
    page_text = resqonse.text
    # 构造一个etree对象
    tree = etree.HTML(page_text)
    # 取值

    res = tree.xpath('//section//div[@class="company-wrapper"]/div')
    for div in res:
        print("=====")
        com_url = div.xpath('./div[1]/a/@href')
        com_title = div.xpath('./div[2]/div[1]//a//text()')
        com_brief = div.xpath('./div[2]/div[2]//span//text()')
        com_highlight = div.xpath('./div[2]/div[3]//span//text()')
        print(com_url[0])
        print("".join(com_title))
        print(com_brief)
        print("".join(com_highlight))

    # 你可以找到相应的节点，然后取值就好
    # 查询class=col0的div下面的所有li节点
    # res=tree.xpath('//div[@class="col0"]//li')
    # print(len(res),res)