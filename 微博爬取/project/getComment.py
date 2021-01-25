import json
import os
import random
from json import JSONDecodeError
from time import sleep

import requests
import urllib3

# 获取评论信息的爬虫

params = {
    'id': '',
    'flow': '0',
    'is_reload': '1',
    'is_show_bulletin': '2',
    'is_mix': '0',
    # 'max_id': '',
    'uid': '',
    'count': '20'
}
headers = {
    'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Cookie': 'SINAGLOBAL=9292833698938.977.1570156009363; wvr=6; login_sid_t=05ce34609684a95642dc764ea0f5dd54; '
              'cross_origin_proto=SSL; _s_tentry=passport.weibo.com; wb_view_log=1536*8641.25; '
              'Apache=4375111879541.127.1611198173911; '
              'ULV=1611198173923:11:7:3:4375111879541.127.1611198173911:1611127091931; ALF=1642734199; '
              'wb_view_log_7551646972=1536*8641.25; WBtopGlobal_register_version=91c79ed46b5606b9; '
              'SSOLoginState=1611198573; '
              'SUB=_2A25NDIA9DeRhGeFL7lMX9CjFzD6IHXVuDiB1rDV8PUJbkNAfLXD9kW1Nfey9JZEHBgce3spTgc6eJ5PNfZ1aM9sB; '
              'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SKwiwbN3SRJeS04j9wZnW5NHD95QNSK'
              '-pSoBc1KMEWs4DqcjTdsHadJ8E9sY_Isqt; UOR=,,www.gooseeker.com; XSRF-TOKEN=AMa8ynfVdbEyZkTP3WpBhYkC; '
              'WBPSESS=Bl-7iRE9k_THnnVfNrdeLxcl6LqYMxVSomkuOVIgx4OOdpvIrO5Zec0yCs9gMiWrVZmCNCXNbh4JmvYEXLcx93gd63EGlaR1TrGHVZj8jmfUrCZX47Azyo6oPlSItz2z; webim_unReadCount=%7B%22time%22%3A1611210926027%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A3%2C%22msgbox%22%3A0%7D '
}
URL = 'https://weibo.com/ajax/statuses/buildComments'

default_max_number = 200

# for root, dirs, files in os.walk('weibo'):
# for file in files:
# ob = open(os.path.join(root, file), 'r', encoding='utf-8')
obList = ['2656274875']
for each in obList:
    ob = open('weibo\\' + each + '.txt', 'r', encoding='utf-8')
    weiboList = ob.read().split('\n')
    # params['uid'] = file[0:file.index('.')]
    params['uid'] = each
    for weibo in weiboList:
        weibo = weibo.split('_')
        if len(weibo) == 1:
            break
        params['id'] = weibo[0]
        date = weibo[1].split(' ')
        date = date[1] + date[2]
        name = weibo[2]
        # print(URL, end='?')
        # for each in params:
        #    print(each + "=" + str(params[each]), end='&')
        print(name)
        max_comment_number = default_max_number
        number = 0
        if not os.path.exists('comment\\' + date + '\\' + '2803301701' + '\\' + params['id']):
            os.makedirs('comment\\' + date + '\\' + '2803301701' + '\\' + params['id'])
        while number < max_comment_number:
            try:
                resp = requests.get(URL, params=params, headers=headers)
            except urllib3.exceptions.MaxRetryError and requests.exceptions.SSLError:
                continue
            if len(resp.text) == 0:
                break
            try:
                resp = json.loads(resp.text)
                if resp['max_id'] == 0 or len(resp) == 5:
                    break
                if number == 0:
                    max_comment_number = min(resp['total_number'], default_max_number)
                commentList = resp['data']
                for comment in commentList:
                    number += 1
                    print(number)
                    commentName = str(comment['user']['id'])  # + '_' + str(comment['like_counts'])
                    commentFile = open(
                        'comment\\' + date + '\\' + '2803301701' + '\\' + params[
                            'id'] + '\\' + commentName + '.txt',
                        'w',
                        encoding="utf-8")
                    commentFile.write(comment['text_raw'])
                    commentFile.close()
                max_id = resp['max_id']
                params['max_id'] = max_id
                if max_id == 0:
                    break
                else:
                    print(max_id)
                sleep(random.randint(1, 2))
            except JSONDecodeError:
                error = open('error.text', 'a+')
                error.write('错误：' + params['id'] + '\n')
                error.close()
                break
        print(str(number) + '_' + str(max_comment_number))
        params['max_id'] = '233'
        params.pop('max_id')
    ob.close()
