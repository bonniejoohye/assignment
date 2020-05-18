#과제 1 네이버북스 크롤링하기
#- 1~8페이지 크롤링
# - 오류 발생시 가능한 페이지까지 크롤링 Ex) 6페이지에서 오류 -> 5페이지까지 크롤링
# • 제목
# • 이미지주소
# • 상세 페이지 링크
# • 저자
# • 출판사
# • 가격(optional) 

import requests
from bs4 import BeautifulSoup
from naver import extract_info
import csv

file=open("naver_books.csv", mode="w", newline="", encoding = 'utf-8')
writer = csv.writer(file) # 위에 적은 파일을 변수로 넣기
writer.writerow(['title','img_src','link','author','publisher'])


final_result=[] #전체 페이지를 크롤링한 결과
for i in range (8):
    print(f'{i+1}번째 페이지 크롤링 중......기다려주세영')
    naver_html = requests.get(f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i+1}")
    naver_soup = BeautifulSoup(naver_html.text, "html.parser")

    naver_list_box = naver_soup.find("ol",{"class" : "basic"})
    naver_list= naver_list_box.find_all("li")
    
    result= extract_info (naver_list) # 한 페이지의 모든 상품 정보가 들어가있음
    final_result+= final_result + result

    #Result= [{}{}... =>80개]
    #final_result = [[ {}{}[}{}{} ]  [ {}{}[}{}{} ] ... => 30개 ] =>상품 2400개

for result in final_result:
    row=[]

    row.append(result['title'])
    row.append(result['img_src'])
    row.append(result['link'])
    row.append(result['author'])
    row.append(result['publisher'])
    writer.writerow(row)
    #csv 에서 한줄 입력완료!

print('크롤링 끝')


