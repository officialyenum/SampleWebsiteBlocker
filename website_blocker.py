import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect="127.0.0.1"
website_list = ["http://server.cpmstar.com",
                "server.cpmstar.com", "https://cobalten.com", "cobalten.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,1) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("Working hours...")
        with open(hosts_temp, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)  # takes pointer to the top
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
