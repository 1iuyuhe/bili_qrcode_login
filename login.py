import requests
import qrcode
import json


qrcode_url = 'https://passport.bilibili.com/x/passport-login/web/qrcode/generate'
login_url = 'https://passport.bilibili.com/x/passport-login/web/qrcode/poll'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0'
}

s = requests.Session()
r = s.get(url=qrcode_url, headers=headers)
resp = json.loads(r.text)
url = resp['data']['url']
qrcode_key = resp['data']['qrcode_key']

qr = qrcode.QRCode()
qr.add_data(url)
qr.print_ascii()

while True:
    data = {
        'qrcode_key': qrcode_key
    }
    r = s.get(url=login_url, headers=headers, params=data)
    resp = json.loads(r.text)
    code = resp['data']['code']
    if code == 0:
        print(f'[code={code}]: 扫码登录成功')
        for k, v in s.cookies.items():
            print(f'{k}={v}')
        break
    elif code == 86038:
        print(f'[code={code}]: 已失效', end='\r')
    elif code == 86090:
        print(f'[code={code}]: 未确认', end='\r')
    elif code == 86101:
        print(f'[code={code}]: 未扫码', end='\r')
    else:
        print(f'[code={code}]: 未知错误')
        break
