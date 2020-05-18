def extract_info (naver_list):
    result = []
    for naver in naver_list:
        title=naver.find("a",{"class" : "N=a:bta.title"}).string
        img_src=naver.find("div", {"class": "thumb_type thumb_type2"}).find("img")['src']
        link=naver.find("a",{"class" : "N=a:bta.title"})['href']
        author=naver.find("a",{"class":"txt_name N=a:bta.author"}).string
        publisher=naver.find("a",{"class":"N=a:bta.publisher"}).string
        
        naver_info={
        'title' : title,
        'img_src' : img_src,
        'link': link,
        'author': author,
        'publisher': publisher
        }

        #note info 저장하는 배열이 필요함!
        result.append(naver_info)
        
    
    return result
    