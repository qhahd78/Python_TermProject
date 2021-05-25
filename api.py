from urllib.parse import urlencode, unquote, quote_plus
import json 
import requests



print('실시간 지하철 위치 조회 서비스')

url ='http://swopenapi.seoul.go.kr/api/subway/'

with open ("secret.json") as file : 
    secret = json.loads(file.read())

station = input("조회할 역을 입력해주세요. ")

params = urlencode({
    quote_plus('KEY'):secret['SECRET'],
    quote_plus('TYPE'): 'json',
    quote_plus('SERVICE'): '지하철 위치 조회 서비스',
    quote_plus('START_INDEX'): 0,
    quote_plus('END_INDEX'): 5,
    quote_plus('statnNm') : station
})

data = requests.get(url + unquote(params))

res = data.json()

print(data)
print(res)
