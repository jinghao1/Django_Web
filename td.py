import requests
from lxml import etree
import re
import json

s_search = "小菜园"
response = requests.get("https://www.xiniudata.com/company/InterHousetjhd/overview",
                        headers={"Cookie": "utoken=ND7HF4WRDLBINXYUL0A1TX576LHDF568"})
if response.status_code == 200:

    # 获取页面资源
    page_text = response.text
    scriptlis = re.findall(r'<script>(.*?)</script>', page_text)
    content = re.findall(r'__NEXT_DATA__ = (.*?);__NEXT_LOADED_PAGES__=', page_text)
    cont = json.loads(content[0])
    # company
    print(cont["props"]["pageProps"]["company"])
    com_info = cont["props"]["pageProps"]["company"]
    name = com_info["name"]
    brief = com_info["brief"]
    roundName = com_info["roundName"]
    cityName = com_info["cityName"] + ">" + com_info["districtName"]
    establishDate = com_info["establishDate"]
    print("======")
    # 融资历程
    # print(cont["props"]["pageProps"]["fundings"])
    # print("======")
    # # 工商信息
    # print(cont["props"]["pageProps"]["gongshang"])
    # print("======")
    # # 行业分类
    # print(cont["props"]["pageProps"]["tileTagList"])
    print("======")


    exit("jing end")
