from django.shortcuts import render
import re 


# Create your views here.

#count 라는 함수 만들기

def count(request):
    return render (request, 'count.html')

#Result 라는 함수 만들기

def result(request):
    text = request.POST['text'] #name='text' 이랑 똑같은거
    total_len = len(text)
    text_len = len(text.replace(' ',''))
    vocab_len = len(re.findall(r"['\w']+", text))
    return render (request, 'result.html', {
        'total_len' :total_len,
        'text': text,
        'text_len': text_len,
        'vocab_len':vocab_len,
    })