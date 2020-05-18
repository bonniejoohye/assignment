def extract_info (book_list):
    result = []
    for i in range(len(book_list)):
        book=book_list[i]

        if (i+1)%2==1:
            title=book.find("td",{"class" : "goodsTxtInfo"}).find("p").find("a").string
            img_src=book.find("div", {"class": "goodsImgW"}).find("img")["src"]
            author=book.find("td",{"class":"goodsTxtInfo"}).find("div",{"class":"aupu"}).find_all("a")[0].string
            publisher=book.find("td",{"class":"goodsTxtInfo"}).find("div",{"class":"aupu"}).find_all("a")[-1].string
            price=book.find("td",{"class":"goodsTxtInfo"}).find("span",{"class":"priceB"}).string
            
            book_info={
                'title' : title,
                'img_src' : img_src,
                'author': author,
                'publisher': publisher,
                'price': price
                }

        else:
            if book.find("p",{"class":"read"})!=None:
                summ=book.find("p",{"class":"read"}).string.strip()

            else:
                summ=""
            
            book_info['summ']=summ
            
            
            result.append(book_info)
        
    
    return result
    