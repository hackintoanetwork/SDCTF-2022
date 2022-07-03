<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcdpEaM%2FbtrBGNxzMZC%2FmppNaMeVju817KI9SZ1Pp1%2Fimg.png" width="800" height="500"/>

If you go into the problem, you will see the same page as above.</br>

---
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcdgFsx%2FbtrBAPCV1ER%2FAhamJfmKSd14mkETpPybyK%2Fimg.png" width="800" height="500"/>

First, I entered the page below by pressing the login button.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQd2v2%2FbtrBHpo68aS%2FSJhMlYBLbkHzkcwj2TvAx0%2Fimg.png" width="800" height="400"/>

The ID password was indicated by annotation from the page source.</br>

ID : AzureDiamond</br>
PW : hunter2</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fqh81h%2FbtrBJMqVoNW%2FWR1OC1O2lHSA3u6WkVRt7k%2Fimg.png" width="800" height="500"/>

When I logged in with the ID given by the page source code comment, a Flag button was created.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkLJmj%2FbtrB67I2Liy%2FkRb9cvVbi9LliChQY3IJo1%2Fimg.png" width="600" height="200"/>

When I pressed the Flag button, the phrase "Invalid Token: Access Denied" came out, and Flag didn't come out.</br>

---

Through the phrase "Invalid Token: Access Denied," we could roughly guess that it was a problem that was solved using Token, and we immediately checked the Token value with Edit This Cookie.</br>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdlKh6f%2FbtrBHU34C3p%2Fitm4rEAGc8nZB0jw4qF0vk%2Fimg.png" width="700" height="500"/>

The Token value was very long.</br>

---

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.

eyJ1c2VybmFtZSI6IkF6dXJlRGlhbW9uZCIsInRva2VuIjoiNTU3NjJmMjAyYjIzMjI2NDQ0Y2E0Zjk5ZTczMjdiNTkiLCJpYXQiOjE2NTIxNDg1NDksImV4cCI6MTY1MjE0ODU1MX0.

K3A_hVp5cMbVmaGTvohdC3KNFnOhfePoH3N-7mS034Q
```

Based on [.], the long Token value was divided into three paragraphs as follows.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbmRNhe%2FbtrBF4mjxNK%2FNQ1N6ZMWB3Lf4NSgJANhhk%2Fimg.png" width="800" height="400"/>

And I tried decoding it because it seemed to be encoded in Base64.</br>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FnlWKC%2FbtrBHVBTgZw%2FQJPp7geYiJf4dhLJxsOpbk%2Fimg.png" width="800" height="400"/>

The first paragraph and the second paragraph were decoded.</br>

However, the third paragraph was not decoded.</br>

---
```
{"alg":"HS256","typ":"JWT"}.  

 {"username":"AzureDiamond","token":"55762f202b23226444ca4f99e7327b59","iat":1652148549,"exp":165214855MX0.

K3A_hVp5cMbVmaGTvohdC3KNFnOhfePoH3N-7mS034Q
```

The decoded final value is as above.</br>

The first paragraph read "JWT" on the decoded value, so I searched it on Google and found that it was a JSON web token.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcekpMu%2FbtrBF4NnLjM%2FSp93TpiMZb6oKmVh205G00%2Fimg.png" width="800" height="500"/>

jwt.io provides a better understanding of the JWT web token structure.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbwOAi3%2FbtrBHquQMuL%2Fv1llmBMACDMzN9cV9HNmJ0%2Fimg.png" width="800" height="300"/>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbYdsrI%2FbtrBFHrmbXy%2F1CqkB5CrS2K1L8oycSHePk%2Fimg.png" width="800" height="300"/>

As a result of the Payload analysis of the token, it was confirmed that the token expiration time was 2 seconds.</br>

---

Earlier, the flag button was pressed, but the phrase "Invalid Token: Access Denied" appeared because the token had expired.</br>

After logging in, you must press the Flag button to enter before the token expires.</br>

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcSiiT8%2FbtrBFYskEdZ%2Fr9x8YrhpJOu9jnG2M2Eluk%2Fimg.png" width="600" height="200"/>

Before the token expired, I quickly pressed the Flag button and saw the letter "d" printed out.</br>

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fo1Cgm%2FbtrBF5yMWaS%2F4KzjoaFJrOzmBZW3OGXkx1%2Fimg.png" width="600" height="200"/>

Then I went to https://jawt.sdc.tf/s/d. Then you can see the letter "c" printed out.</br>

When I saw this, I noticed that there was still a directory in the directory.</br>


---

I wrote the Python script that was needed to solve the problem right away.</br>

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

---

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcW4JGq%2FbtrBGMMgj1E%2Fic9VE6dA2YbGb01EB5EYo0%2Fimg.png" width="800" height="500"/>

This Python automation script made it easy to solve the problem.</br>

> Flag : sdctf{Th3_m0r3_t0k3ns_the_le55_pr0bl3ms_adf3d}



