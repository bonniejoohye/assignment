from django.shortcuts import render,redirect
from .models import Article

# Create your views here.
def index_function(request):
    articles_movie_count = Article.objects.filter(category="movie").count()
    articles_drama_count = Article.objects.filter(category="drama").count()
    articles_entertain_count = Article.objects.filter(category="entertain").count()
    return render(request, 'index.html', {
        'articles_movie_count':articles_movie_count,
        'articles_drama_count':articles_drama_count,
        'articles_entertain_count':articles_entertain_count
    })

def new_function(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category = request.POST['category']
        )
        return redirect('detail_in_html', pk_of_article=new_article.pk)
    else:
        return render(request, 'new.html')

def detail_function(request,pk_of_article):
    article = Article.objects.get(pk=pk_of_article)
    return render(request, 'detail.html', {'article': article})

def movie_function(request):
    articles_movie = Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'articles_movie':articles_movie})

def drama_function(request):
    articles_drama = Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'articles_drama':articles_drama})

def entertain_function(request):
    articles_entertain = Article.objects.filter(category="entertain")
    return render(request, 'entertain.html', {'articles_entertain':articles_entertain})