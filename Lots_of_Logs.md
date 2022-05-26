![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FPiEvI%2FbtrBMCvuDCE%2FxUnggBjvK2QSebWrXFkDmk%2Fimg.png)
문제에 들어가면 위와 같은 페이지가 나온다.


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FLPoWZ%2FbtrBMaTvHrU%2FYDRmojUZwoF35xcO2qjZ9k%2Fimg.png)
페이지를 내리면 View raw log 버튼을 볼 수 있다.<br/>


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbYL9kN%2FbtrBNdip2Eg%2FqC8t9P2wZgQFUkL2Xk037K%2Fimg.png)
버튼을 눌러 들어가면 위와 같이 로그 파일들이 나온다.<br/>


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCecKE%2FbtrBLUKdb3S%2Fm6ORr4HxWkl58TztkTue21%2Fimg.png)
날짜를 바꿔 2022년 3월 8일 화요일로도 들어가보았다.<br/>
2022년 3월 8일 화요일도 마찬가지로 로그가 쌓여 있는 것을 확인할 수 있다.<br/>
로그는 YYYY/MM/DD/DAY.log 형식의 경로에서 호스팅되고 있다.



로그들을 수집하는 파이썬 스크립트를 짜보았다.

```
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
``` </br>

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FQFPOD%2FbtrBQDf7JOT%2FerS9wpakmDUAUKA31yKvDk%2Fimg.png)
2018년도 로그들을 수집하던 중 2018년 6월에 3일 동안 로그가 끊겨 있는 것을 발견하였고 그 다음 날인 2018년 6월 13일 로깅 서버를 악용하여 3일 동안의 로그를 삭제하는 사람을 캡처한 로그가 있었다.<br/>


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcKOjir%2FbtrBHpYBB7t%2FA0S9kCK47YTnO4o1vemUB0%2Fimg.png)
로그를 보면 비밀번호를 사용하여 포트에 백도어를 설치하는 것을 볼 수 있다.<br/>


![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbC753K%2FbtrBPffvqxc%2FBrJDrnj1LmfDBwblOsmAA0%2Fimg.png)
netcat을 실행하여 열려있는 로그 서버에 접속하였고 암호를 입력하여 플래그를 얻을 수 있었다.<br/>


> Flag : sdctf{b3tr4y3d_by_th3_l0gs_8a4dfd}
