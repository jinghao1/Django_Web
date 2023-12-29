import requests
from lxml import etree

def xn_search(s_search):


    # s_search = "小菜园"
    response = {}

    try:
        response = requests.get("https://www.xiniudata.com/search2?name={}".format(s_search),
                                headers={"Cookie": "utoken=ND7HF4WRDLBINXYUL0A1TX576LHDF568"})
    except Exception as e:
        print(e)
    return response


def xn_company_detail(xn_href):


    # s_search = "小菜园"
    response = {}

    try:
        response = requests.get("https://www.xiniudata.com/company/{}/overview".format(xn_href),
                                headers={"Cookie": "utoken=ND7HF4WRDLBINXYUL0A1TX576LHDF568"})
    except Exception as e:
        print(e)
    return response