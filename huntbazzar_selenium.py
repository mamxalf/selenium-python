import json
from selenium import webdriver

url = 'https://www.huntstreet.com/designer'

browser = webdriver.Firefox()
browser.get(url)

jsonArr = []
arrElements1 = []
arrElements2 = []
arrElements2Fix = []

elements1 = browser.find_elements_by_xpath('//div[contains(@class, "dbLeft")]')
for i in elements1:
    strData1 = i.text
    arrElements1.append(strData1)

elements2 = browser.find_elements_by_xpath('//div[contains(@class, "dbRight")]')
for i in elements2:
    strData2 = i.text
    arrElements2.append(strData2)

print(arrElements1)
print('%' * 75)

for i in arrElements2:
    arr = i.split('\n')
    arrElements2Fix.append(arr)

print(arrElements2Fix)
print('%' * 75)

count = 0
while (count < len(arrElements1)):
    # print(arrElements1[count])
    data = {
        arrElements1[count]: arrElements2Fix[count]
    }
    jsonArr.append(data)
    count += 1

jsonFix = json.dumps(jsonArr)
print(jsonFix)

out_file = open('data/huntbazzar.json', 'w')
json.dump(jsonArr, out_file)
out_file.close()

browser.close()
