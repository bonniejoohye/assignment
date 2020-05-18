# 과제 2
# • 시도
# • 시군구
# • 선별진료소(이름) 
# • 전화번호
# > corona_hospital.csv로 저장
# Github repo에 코드, csv 파일 업로드 후 Issue 댓글에 repo 주소 달기

import requests
from bs4 import BeautifulSoup
import csv

file=open("corona_hospital.csv", mode="w", newline="")
writer = csv.writer(file) # 위에 적은 파일을 변수로 넣기
writer.writerow(['sido','sigungu','name','phonenum'])

hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'

hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")
hospital_body= hospital_soup.find("tbody",{"class" : "tb_center"})
hospital_all= hospital_body.find_all("tr")

result=[]
for i in range(len(hospital_all)):
    hospital_tr=hospital_all[i].contents
    hospital_name=hospital_tr[3].text.split()

    hospital_info={
        'sido':hospital_tr[1].string,
        'sigungu':hospital_tr[2].string,
        'name':hospital_name[0],
        'phonenum':hospital_tr[4].string
    }
    
    result.append(hospital_info)


for info in result:
    row=[]
    row.append(info['sido'])
    row.append(info['sigungu'])
    row.append(info['name'])
    row.append(info['phonenum'])
    writer.writerow(row)



