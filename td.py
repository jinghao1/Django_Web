import requests
from lxml import etree
import re
import json
import datetime
print(type(datetime.date.fromtimestamp(1462464000000/1000)))

print(datetime.date.fromtimestamp(1462464000000/1000))
exit()

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

    licheng = cont["props"]["pageProps"]["fundings"]
    for licheng in cont["props"]["pageProps"]["fundings"]:
        print(licheng)
        roundName = licheng["roundName"]
        fundingDate = licheng["fundingDate"]
        fundingDesc = json.loads(licheng["fundingDesc"])
        # 估值
        postMoney = fundingDesc["postMoney"]
        money = fundingDesc["money"]
        # 比例
        ratio = fundingDesc["ratio"]
        # 投资方

        if fundingDesc.get("investorStr", None) is None:
            investorStr = ""
        else:
            investorArr = json.loads(fundingDesc["investorStr"])
            in_arr = []
            for item in investorArr:
                in_arr.append(item['text'])
            investorStr = "".join(in_arr)
        print("investorStr====", investorStr)
    # # 工商信息
    # print(cont["props"]["pageProps"]["gongshang"])
    gongshang = json.loads(cont["props"]["pageProps"]["gongshang"])
    gs_name = gongshang.get("name", "")
    # 法人
    legalPersonName = gongshang.get("legalPersonName", "")
    # 成立时间
    establishTime = gongshang.get("establishTime", "0")
    # 工商描述
    businessScope = gongshang.get("businessScope", "")
    # 经营状态
    regStatus = gongshang.get("regStatus", "")
    # 注册资本
    regCapital = gongshang.get("regCapital", "")
    # 联系方式
    contact_info = gongshang.get("contact", {})
    telephone = contact_info.get("telephone", "")
    email = contact_info.get("email", "")
    address = contact_info.get("address", "")
    print(contact_info, address)
    # print("======")
    # 标签画像

    # 优势
    # # 行业分类
    # print(cont["props"]["pageProps"]["tileTagList"])
    tileTagListArr = cont["props"]["pageProps"]["tileTagList"]
    tag_arr_hy = []
    tag_arr_ys = []
    for item in tileTagListArr:
        if item['confidence']:
            tag_arr_ys.append(item['name'])
        else:
            tag_arr_hy.append(item['name'])

    print("youshi", tag_arr_ys)
    print("hangye", tag_arr_hy)

    exit("jing end")
