#의용메카트로닉스공학과 20195277 하유민 
print("의용메카트로닉스공학과 20195277 하유민")

# 1. api 실행하는 파일 
# 2. tk 만드는 파일
# 3. 장소를 선택하면 그 장소에 맞는 출력 값을 가져온다. 
# 4. 장소를 선택 => 선택 값을 api 파일로 보내줌 => 그 장소 값에 맞는 결과를 호출 => 다시 tk 로 보내줌 => tk 에서 결과 출력 

from tkinter import * 

# api 모듈 불러오기 
from apitest import api

site = Tk()
site.title("시도별 대기상태 정보 조회 서비스")

# 옵션 리스트 정의 
place = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주', '세종']
# 옵션에서 선택된 값 정의 
selected = StringVar()
selected.set(None)

# api 로 선택된 지역을 보내주는 함수. 
def send() : 
    # 선택된 지역을 placeS 에 저장
    placeS = selected.get()
    # api 함수로 선택된 지역을 인자로 보내주고, 결과값을 result 에 저장 
    result = api(placeS)
    
    # send 함수는 chango 함수를 리턴, result 값을 인자로 담아 change 에 보내준다. 
    return change(result)

# api로부터 받은 결과 값을 gui 로 출력해주는 함수 . 
def change(result) :
    # j 는 한 줄에 지역 하나씩 출력하기 위한 변수값
    j = 3
    # result 값은 리스트 형태로, 한 지역이 리스트 안에 딕셔너리 형태로 나오기 때문에 for 문을 돌면서 
    # 리스트에서 지역 하나(i)를 선택하고, key 값으로 지역명, 측정시간, 미세먼지 농도, 오존 농도를 조회하여
    # Label 로 key 값에 따른 value 값을 gui로 출력해준다. 
    for i in result : 
        Label(site, text = "각 지역의 대기 상태를 확인해보세요.").grid(row=0, column=1)
        Label(site, text = "지역명").grid(row=2, column=0)
        Label(site, text = "측정날짜").grid(row=2, column=1)
        Label(site, text = "미세먼지 농도").grid(row=2, column=2)
        Label(site, text = "오존 지수").grid(row=2, column=3)
        Label(site, text = str(i['stationName'])).grid(row=j, column=0)
        Label(site, text = str(i['dataTime'])).grid(row=j, column=1)
        Label(site, text = str(i['pm10Value'])).grid(row=j, column=2)
        Label(site, text = str(i['o3Grade'])).grid(row=j, column=3)
        # for 문을 돌 때마다 j 를 1씩 증가시켜줌으로써 한 줄에 하나의 지역을 출력해준다. 
        j = j+1 
    
    
# 선택 받을 지역을 optionmenu 로 띄우기. 
OptionMenu(site, selected, *place).grid(row=1, column=1)
# Label(site, text="결과값", width=20).grid(row=0, column=0)

# 버튼을 클릭할시 선택된 지역의 값을 api 함수로 전달하여 그에 맞는 데이터를 출력 
Button(site, text="출력", command = send, width=20).grid(row=13, column=1)

site.mainloop()