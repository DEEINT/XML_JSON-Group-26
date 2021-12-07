import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
result = []
file = open('news.json', 'w', encoding = 'utf-8')
for child in root.findall('channel/item'):
    result.append({'pubDate':  child.find("pubDate").text,'title':child.find("title").text})
file.write(json.dumps(result, ensure_ascii=False, separators = (',\n', ': ')))
file.close()

tags = []
for child in root.findall('channel/item')[0]:
    tags.append(child.tag)

result = []
file = open('items.json', 'w', encoding = 'utf-8')
for child in root.findall('channel/item'):
    result.append({})
    for tag in tags:
        try:
            result[-1][tag] = child.find(tag).text
        except BaseException:
            result[-1][tag] = 'None'
file.write(json.dumps(result, ensure_ascii=False, separators = (',\n', ': ')))
file.close()