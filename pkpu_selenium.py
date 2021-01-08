import json
from selenium import webdriver

url = 'https://jadwalsholat.pkpu.or.id/'

browser = webdriver.Firefox()
browser.get(url)

jsonArr = []

count = 4
while count <= 34:
    elements = browser.find_elements_by_xpath(f'/html/body/table/tbody/tr[{count}]')
    for i in elements:
        strData = i.text
        data = {
            'tanggal': strData[0:2],
            'Shubuh': strData[3:8],
            'Dzuhur': strData[9:14],
            'Ashar': strData[15:20],
            'Maghrib': strData[21:26],
            'Isya': strData[27:32]
        }
        jsonArr.append(data)

    count += 1

print(jsonArr)
out_file = open('data.json', 'w')
json.dump(jsonArr, out_file)
out_file.close()

browser.close()