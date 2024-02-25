import requests
from lxml import etree
user_token = "CNYBQ7P7M8C1FSIBI4850JY6A3TPA81C"
song_token = "ND7HF4WRDLBINXYUL0A1TX576LHDF568"
# litianshu utoken=CNYBQ7P7M8C1FSIBI4850JY6A3TPA81C btoken=DK3OVIBB9C7LL3DUEK28G5KE7SAS2D1A
def xn_search(s_search):


    # s_search = "小菜园"
    response = {}

    try:
        response = requests.get("https://www.xiniudata.com/search2?name={}".format(s_search),
                                headers={"Cookie": "utoken={}".format(user_token)})
    except Exception as e:
        print(e)
    return response


def xn_company_detail(xn_href):


    # s_search = "小菜园"
    response = {}

    try:
        response = requests.get("https://www.xiniudata.com/company/{}/overview".format(xn_href),
                                headers={"Cookie": "utoken={}".format(user_token)})
    except Exception as e:
        print(e)
    return response