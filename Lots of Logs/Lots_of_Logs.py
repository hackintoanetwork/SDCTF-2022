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