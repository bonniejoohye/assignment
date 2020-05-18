#과제3
# - 1~20페이지 크롤링
# - 오류 발생시 가능한 페이지까지 크롤링 Ex) 5페이지에서 오류 -> 4페이지까지 크롤링
# • 제목
# • 이미지주소 
# • 저자
# • 출판사
# • 가격
# • 요약글

import requests
from bs4 import BeautifulSoup
from yes24 import extract_info
import csv

file=open("yes24_books.csv", mode="w", newline="", encoding = 'utf-8')
writer = csv.writer(file) # 위에 적은 파일을 변수로 넣기
writer.writerow(['title','img_src','author','publisher','price','summ'])


final_result=[] #전체 페이지를 크롤링한 결과
for i in range (20):
    print(f'{i+1}번째 페이지 크롤링 중......기다려주세영')
    book_html = requests.get(f"http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber={i+1}")
    book_soup = BeautifulSoup(book_html.text, "html.parser")
    book_list_box = book_soup.find("table",{"id" : "category_layout"})
    book_list= book_list_box.find_all("tr")
    result= extract_info (book_list) # 한 페이지의 모든 상품 정보가 들어가있음
    final_result+= result

    #Result= [{}{}... =>80개]
    #final_result = [[ {}{}[}{}{} ]  [ {}{}[}{}{} ] ... => 30개 ] =>상품 2400개

for result in final_result:
    row=[]

    row.append(result['title'])
    row.append(result['img_src'])
    row.append(result['author'])
    row.append(result['publisher'])
    row.append(result['price'])
    row.append(result['summ'])

    writer.writerow(row)
    #csv 에서 한줄 입력완료!

print('크롤링 끝')
