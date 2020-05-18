import requests
from bs4 import BeautifulSoup

note_html = requests.get("http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=03&PageNumber=2")
note_soup = BeautifulSoup(note_html.text, "html.parser")

note_list_box = note_soup.find("table",{"id" : "category_layout"})
note_list= note_list_box.find_all("tr")

i=1
for note in note_list:
    print(f"{i}번째 상품")
    i=i+1
    print(note)

# title=note_list[1].find("td",{"class" : "goodsTxtInfo"}).find("p").find("a").string
# print(title)


