<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcdpEaM%2FbtrBGNxzMZC%2FmppNaMeVju817KI9SZ1Pp1%2Fimg.png" width="800" height="500"/>


문제에 들어가면 위와 같은 페이지가 나온다.</br>

---
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcdgFsx%2FbtrBAPCV1ER%2FAhamJfmKSd14mkETpPybyK%2Fimg.png" width="800" height="500"/>

우선 로그인 버튼을 눌러 아래 페이지로 들어갔다.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQd2v2%2FbtrBHpo68aS%2FSJhMlYBLbkHzkcwj2TvAx0%2Fimg.png" width="800" height="400"/>
아이디 비밀번호는 페이지 소스에서 주석으로 알려주고 있었다.</br>
ID : AzureDiamond</br>
PW : hunter2</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fqh81h%2FbtrBJMqVoNW%2FWR1OC1O2lHSA3u6WkVRt7k%2Fimg.png" width="800" height="500"/>

페이지 소스코드 주석에서 알려준 아이디로 로그인을 하니 Flag 버튼이 생겼다.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkLJmj%2FbtrB67I2Liy%2FkRb9cvVbi9LliChQY3IJo1%2Fimg.png" width="800" height="200"/>

Flag 버튼을 눌렀더니 "Inavalid Token: Access Denied" 라는 문구만 나오고 Flag는 나오지 않았다.</br>

---

"Inavalid Token: Access Denied" 문구를 통해서 Token을 활용해 푸는 문제라는 걸 대략 짐작할 수 있었고
바로 EditThisCookie로 Token 값을 확인해보았다.</br>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdlKh6f%2FbtrBHU34C3p%2Fitm4rEAGc8nZB0jw4qF0vk%2Fimg.png" width="700" height="500"/>

Token 값은 아주 길었다.

---

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.

eyJ1c2VybmFtZSI6IkF6dXJlRGlhbW9uZCIsInRva2VuIjoiNTU3NjJmMjAyYjIzMjI2NDQ0Y2E0Zjk5ZTczMjdiNTkiLCJpYXQiOjE2NTIxNDg1NDksImV4cCI6MTY1MjE0ODU1MX0.

K3A_hVp5cMbVmaGTvohdC3KNFnOhfePoH3N-7mS034Q
```

긴 Token 값을 [.] 기준으로 아래와 같이 세 문단으로 나누어 보았다.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbmRNhe%2FbtrBF4mjxNK%2FNQ1N6ZMWB3Lf4NSgJANhhk%2Fimg.png" width="800" height="400"/>

그리고 Base64로 인코딩 되어 있는 것 같아 디코딩도 시도해보았다.</br>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnlWKC%2FbtrBHVBTgZw%2FQJPp7geYiJf4dhLJxsOpbk%2Fimg.png" width="800" height="400"/>

첫번째 문단과 두번째 문단은 디코딩이 되었다.</br>
하지만 세번째 문단은 디코딩이 되지 않았다.</br>

---
```
{"alg":"HS256","typ":"JWT"}.  

 {"username":"AzureDiamond","token":"55762f202b23226444ca4f99e7327b59","iat":1652148549,"exp":165214855MX0.

K3A_hVp5cMbVmaGTvohdC3KNFnOhfePoH3N-7mS034Q
```

디코딩 된 최종 값은 위와 같다.</br>
첫번째 문단이 디코딩 된 값에 "JWT" 라 적혀 있어 구글에 검색해 보았고 JSON 웹 토큰이라는 것을 알 수 있었다.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcekpMu%2FbtrBF4NnLjM%2FSp93TpiMZb6oKmVh205G00%2Fimg.png" width="800" height="500"/>

jwt.io에선 JWT 웹 토큰 구조를 더 잘 파악할 수 있다.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbwOAi3%2FbtrBHquQMuL%2Fv1llmBMACDMzN9cV9HNmJ0%2Fimg.png" width="800" height="300"/>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbYdsrI%2FbtrBFHrmbXy%2F1CqkB5CrS2K1L8oycSHePk%2Fimg.png" width="800" height="300"/>

토큰의 Payload 분석 결과 토큰 만료 시간이 2초임을 확인 할 수 있었다.</br>

---
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcSiiT8%2FbtrBFYskEdZ%2Fr9x8YrhpJOu9jnG2M2Eluk%2Fimg.png" width="800" height="200"/>

앞에서 Flag 버튼을 눌렀지만 "Inavalid Token: Access Denied"라는 문구가 뜬 것은 토큰이 만료되었기 때문이다.</br>
로그인 후 토큰이 만료되기 전에 Flag 버튼을 눌러 들어가야 한다.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fo1Cgm%2FbtrBF5yMWaS%2F4KzjoaFJrOzmBZW3OGXkx1%2Fimg.png" width="800" height="200"/>

토큰이 만료 되기 전 재빠르게 Flag 버튼을 눌러 들어갔고 "d"라는 문자가 출력된 것을 보았다.</br>
그런 다음 https://jawt.sdc.tf/s/d 로 들어갔다. 그랬더니 "c"라는 문자가 출력된 것을 볼 수 있었다.</br>
이를 보고 디렉터리 안에 계속 디렉터리가 있다는 것을 눈치채게 되었다.</br>

---
```python
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
```

바로 문제 풀이에 필요한 파이썬 스크립트를 짜보았다.</br>


---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcW4JGq%2FbtrBGMMgj1E%2Fic9VE6dA2YbGb01EB5EYo0%2Fimg.png" width="800" height="500"/>

이렇게 파이썬 자동화 스크립트를 통해 간편하게 문제를 풀 수 있었다.</br>

> Flag : sdctf{Th3_m0r3_t0k3ns_the_le55_pr0bl3ms_adf3d}



