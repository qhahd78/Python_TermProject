from urllib.parse import urlencode, unquote, quote_plus
import requests
import json

url = 'http://apis.data.go.kr/1360000/TourStnInfoService/getCityTourClmIdx'

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

print(data)

res = data.json()

print(res['response']['body']['items']['item'])