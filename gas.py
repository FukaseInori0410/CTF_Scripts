from bs4 import BeautifulSoup
import requests

url = 'http://localhost:14652/'
payload = {"driver": "syy", "steering_control": "0", "throttle": "2"}
session = requests.session()

for i in range(7):
    response = session.post(url=url, data=payload)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.h3.string)
    if soup.h3.string == '弯道向右，抓地力太大了！':
        payload["steering_control"] = "-1"
        payload["throttle"] = "2"
    elif soup.h3.string == '弯道向右，保持这个速度':
        payload["steering_control"] = "-1"
        payload["throttle"] = "1"
    elif soup.h3.string == '弯道向右，抓地力太小了！':
        payload["steering_control"] = "-1"
        payload["throttle"] = "0"
    elif soup.h3.string == '弯道向左，抓地力太大了！':
        payload["steering_control"] = "1"
        payload["throttle"] = "2"
    elif soup.h3.string == '弯道向左，保持这个速度！':
        payload["steering_control"] = "1"
        payload["throttle"] = "1"
    elif soup.h3.string == '弯道向左，抓地力太小了！':
        payload["steering_control"] = "1"
        payload["throttle"] = "0"
    elif soup.h3.string == '弯道直行，抓地力太大了！':
        payload["steering_control"] = "0"
        payload["throttle"] = "2"
    elif soup.h3.string == '弯道直行，保持这个速度！':
        payload["steering_control"] = "0"
        payload["throttle"] = "1"
    elif soup.h3.string == '弯道直行，抓地力太小了！':
        payload["steering_control"] = "0"
        payload["throttle"] = "0"
    print(payload)
    if i == 6:
        print(soup)


