![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FPiEvI%2FbtrBMCvuDCE%2FxUnggBjvK2QSebWrXFkDmk%2Fimg.png)

If you go into the challenge, you will see the same page as above.</br>

---

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLPoWZ%2FbtrBMaTvHrU%2FYDRmojUZwoF35xcO2qjZ9k%2Fimg.png)

If you scroll down the page, you can see the View raw log button.</br>

---

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbYL9kN%2FbtrBNdip2Eg%2FqC8t9P2wZgQFUkL2Xk037K%2Fimg.png)

I pressed the button to enter and the log records came out as above.<br>

---

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCecKE%2FbtrBLUKdb3S%2Fm6ORr4HxWkl58TztkTue21%2Fimg.png)

I changed the date and entered Tuesday, March 8, 2022.</br>

It was also confirmed that the logs were stacked on Tuesday, March 8, 2022.<br>

Logs are hosted on a path in the format YYYY/MM/DD/DAY.log.</br>

---

I wrote Python scripts to collect logs.<br>

(For convenience, the script was changed to collect only logs in June 2018.)</br>


```python
import requests

weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for year in range (2018, 2019):
    for month in range (6, 7):
        for day in range(1, 32):
            for week in weeks:
                response = requests.get("https://logs.sdc.tf/logs/"+str(year)+"/"+str(month)+"/"+str(day)+"/"+str(week)+".log")
                if "Welcome to LoggerOS" in response.text:
                    f = open("/Users/dltpgud0427/lots-of-logs/" + str(year) + '-' + str(month) + '-' + str(day) + '-' + str(week) + ".log", 'w')
                    f.write(response.text)
                    f.close()
```

---

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQFPOD%2FbtrBQDf7JOT%2FerS9wpakmDUAUKA31yKvDk%2Fimg.png)

While collecting the 2018 logs, I found that the logs were cut off for 3 days in June 2018</br>

The next day, on June 13, 2018, there was a log that captured a person who abused the logging server to delete the log for three days.<br>

---

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcKOjir%2FbtrBHpYBB7t%2FA0S9kCK47YTnO4o1vemUB0%2Fimg.png)

If you look at the log, you can see that the backdoor is installed on the port using a password.</br>

---

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbC753K%2FbtrBPffvqxc%2FBrJDrnj1LmfDBwblOsmAA0%2Fimg.png)

I was able to access the open log server by running netcat and enter a password to get a flag.</br>


> Flag : sdctf{b3tr4y3d_by_th3_l0gs_8a4dfd}
