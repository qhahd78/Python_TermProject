from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json

url = 'http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx'
# url2 ='http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx?serviceKey=RhmUqd23ZvRpI7Z24m6hZFEs0TcTgEU75ade%2Bh5XSJumgbUvjA6zoe3Q0DI7fFagSLQS3PwIchFzu%2BO%2FF1WOmg%3D%3D&pageNo=1&numOfRows=10&dataType=JSON&CURRENT_DATE=202105250000&DAY=3&CITY_AREA_ID=5013000000'
with open ("secret.json") as file : 
    secret = json.loads(file.read())

params = "?" + urlencode({
    quote_plus('serviceKey'): secret["SECRET"],
    quote_plus('pageNo'): '1',
    quote_plus('numOfRows'): '10',
    quote_plus('dataType'): 'JSON',
    quote_plus('CURRENT_DATE'): '202105250000',
    quote_plus('DAY') : '3',
    quote_plus('CITY_AREA_ID') : '5013000000'
})

data = requests.get(url + unquote(params))
# data2=requests.get(url2)

print(data)
# print(data2)
res = data.json()
# res2 = data2.json()
print(res['response']['body']['items']['item'])
# print(res2)