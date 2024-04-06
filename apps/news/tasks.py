from .models import NewCategory, News, Banner
import requests, time
from django.db.models import Q

import re
import copy
from django.http import JsonResponse

# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

import requests
import random
import json
from hashlib import md5


# query = 'Hello World! This is 1st paragraph.\nThis is 2nd paragraph.'

# Generate salt and sign
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def to_translate(query):
    # Set your own appid/appkey.
    appid = '20231202001899147'
    appkey = 'ciZbPXWbkBQnm2wAuk9U'
    #  litianshu   APP ID：20240225001972867
    # 密钥：SL45TUTOvWDh74tDlvyB

    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'zh'
    to_lang = 'en'
    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    url = endpoint + path
    salt = random.randint(32768, 65536)
    sign = make_md5(appid + query + str(salt) + appkey)

    # Build request
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()
    # Show response
    # print(json.dumps(result, indent=4, ensure_ascii=False))
    return result


def field_content_to_translate(trans_content):
    en_con = copy.deepcopy(trans_content)
    before_trans = re.findall(r'[\u4e00-\u9fa5]+', trans_content)
    line_ind = 0
    for line_one in before_trans:
        after_trans = to_translate(line_one)
        for one in after_trans.get("trans_result", []):
            en_con = en_con.replace(one["src"], one["dst"], 1)

        if line_ind > 8:
            time.sleep(1)
    return en_con


def translate_news(request):
    """文章翻译 标题、描述、内容"""
    # newses = News.objects.all()
    # 用于加载界面显示新闻的个数，settings中设置的ONE_PAGE_NEWS_COUNT是1，
    # 这里配置后，界面只会展示1篇文章
    newses = News.objects.filter(need_trans=1)[0:2]

    for item in newses:
        if not bool(item.title_en) and item.title:
            en_con = field_content_to_translate(item.title)
            News.objects.filter(id=item.id).update(title_en=en_con)
            # print(en_con)
        if not bool(item.desc_en) and item.desc:
            en_con = field_content_to_translate(item.desc)
            News.objects.filter(id=item.id).update(desc_en=en_con)
            # print(en_con)
        if not bool(item.content_en) and item.content:
            en_con = field_content_to_translate(item.content)
            News.objects.filter(id=item.id).update(content_en=en_con,need_trans=0)
            # print(en_con)
        # print("end++++")

    return JsonResponse(data={
        "msg": "success"
    })
