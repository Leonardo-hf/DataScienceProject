import json
import random
from json import JSONDecodeError
from time import sleep
import requests
import urllib3

# 获取媒体微博数据的爬虫

params = {
    'is_all': 1,
    'stat_date': '',
    'uid': '',
    'feature': 0,
    'page': ''
}
'''params2 = {
    'ajwvr': 6,
    'domain': '100206',
    'is_all': 1,
    'stat_date': '',
    'page': '',
    'pagebar': '',
    'profile_ftype': 1
}'''
headers = {
    'user-agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    # 'Cookie': 'SINAGLOBAL=9292833698938.977.1570156009363; wvr=6; login_sid_t=05ce34609684a95642dc764ea0f5dd54; cross_origin_proto=SSL; WBStorage=8daec78e6a891122|undefined; _s_tentry=passport.weibo.com; wb_view_log=1536*8641.25; Apache=4375111879541.127.1611198173911; ULV=1611198173923:11:7:3:4375111879541.127.1611198173911:1611127091931; ALF=1642734199; wb_view_log_7551646972=1536*8641.25; WBtopGlobal_register_version=91c79ed46b5606b9; SSOLoginState=1611198573; SUB=_2A25NDIA9DeRhGeFL7lMX9CjFzD6IHXVuDiB1rDV8PUJbkNAfLXD9kW1Nfey9JZEHBgce3spTgc6eJ5PNfZ1aM9sB; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SKwiwbN3SRJeS04j9wZnW5NHD95QNSK-pSoBc1KMEWs4DqcjTdsHadJ8E9sY_Isqt; UOR=,,www.baidu.com; webim_unReadCount=%7B%22time%22%3A1611198639506%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D',
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

'''URL1 = 'https://weibo.com/'
URL2 = 'https://weibo.com/p/aj/v6/mblog/mbloglist'''''

dates = [
    # '201912',
    # '202001',
    # '202002',
    '202003'
    # '202004',
    # '202005',
    # '202006'
]
# 观察者网，共青团中央，澎湃新闻，央视新闻，紫光阁，新华网，人民日报，凤凰网，中国新闻周刊，新京报
names = [
    # '1887344341',观察者网完成，全部
    # '3937348351',共青团中央完成，全部
    # '5044281310',4111 澎湃新闻
    # '2656274875',央视新闻，完成,只有每月月末
    # '5467852665',紫光阁完成，全部
    # '2810373291',无，新华网未公开当时的新闻
    # '2803301701',人民日报 全部
    # '2615417307',凤凰网完成，全部
    # '1642512402'  # ,7394 中国新闻周刊
    # '1644114654'  # 新京报，全部
]
URL = 'https://weibo.com/ajax/statuses/mymblog'
for name in names:
    params['uid'] = name
'''if not os.path.exists('weibo\\' + name):
    os.mkdir('weibo\\' + name)'''
ob = open('weibo\\' + params['uid'] + '.txt', 'a', encoding='utf-8')
for date in dates:
    params['stat_date'] = date

'''URL = URL + '?is_all=1&stat_data=' + date + "&key=Profile_V6_Timeline&value=month"

browser = webdriver.Chrome()

browser.implicitly_wait(30)

# browser.get('https://weibo.com/newoutlook?is_all=1&stat_date=201912&key=Profile_V6_Timeline&value=month')
browser.get('https://weibo.com/login.php')

cookie = {'SINAGLOBAL': '9292833698938.977.1570156009363', 'wvr': '6',
          'login_sid_t': '05ce34609684a95642dc764ea0f5dd54', 'cross_origin_proto': 'SSL',
          'WBStorage': '8daec78e6a891122|undefined', '_s_tentry': 'passport.weibo.com',
          'wb_view_log': '1536*8641.25', 'Apache': '4375111879541.127.1611198173911',
          'ULV': '1611198173923:11:7:3:4375111879541.127.1611198173911:1611127091931', 'ALF': '1642734199',
          'wb_view_log_7551646972': '1536*8641.25', 'WBtopGlobal_register_version': '91c79ed46b5606b9',
          'SSOLoginState': '1611198573',
          'SUB': '_2A25NDIA9DeRhGeFL7lMX9CjFzD6IHXVuDiB1rDV8PUJbkNAfLXD9kW1Nfey9JZEHBgce3spTgc6eJ5PNfZ1aM9sB',
          'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5SKwiwbN3SRJeS04j9wZnW5NHD95QNSK-pSoBc1KMEWs4DqcjTdsHadJ8E9sY_Isqt',
          'UOR': ',,www.baidu.com',
          'webim_unReadCount': '%7B%22time%22%3A1611198639506%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A2%2C%22msgbox%22%3A0%7D'}

for line in headers['Cookie'].split(';'):
    key, value = line.split('=', 1)  # 1代表只分一次，得到两个数据
    cookie[key[1:]] = value
print(cookie)
sleep(5)
for each in cookie:
    browser.add_cookie({'name': each, 'value': cookie[each]})
sleep(5)'''

pageIndex = 41

while True:
    params['page'] = pageIndex
    try:
        try:
            resp = requests.get(URL, params=params, headers=headers)
        except urllib3.exceptions.MaxRetryError and requests.exceptions.SSLError:
            continue
        # print(resp.text)
        if len(resp.text) == 0:
            break

        resp = json.loads(resp.text)
        weiboIndex = 0
        # print(pageIndex)

        weiboList = resp['data']['list']

        if len(weiboList) == 0:
            break

        while weiboIndex < len(weiboList):

            weibo = weiboList[weiboIndex]

            weiboIndex += 1

            text = ''.join(weibo['text_raw']).strip().replace('\n', '')
            print(text)
            if text.find('战疫') == -1 and text.find('疫情') == -1 and text.find('新冠') == -1 and text.find(
                    '新型冠') == -1 and text.find(
                '肺炎') == -1 and text.find('抗疫') == -1:
                continue
            ob.write(weibo['mid'] + '_' + weibo['created_at'] + '_' + text + '_' + str(
                weibo['comments_count']) + '_' + str(weibo['attitudes_count']) + '_' + str(
                weibo['reposts_count']) +
                     '\n')

            sleep(random.randint(3, 5))
    except JSONDecodeError:
        error = open('urlError.text', 'a+')
        error.write('错误：' + params['stat_date'] + ' ' + str(pageIndex) + '\n')
        error.close()
    finally:
        pageIndex += 1

ob.close()
