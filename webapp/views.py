from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import UpdateView, DeleteView
# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request,'webapp/index.html', {'title': 'Main', 'articles': articles})

class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'webapp/create.html'
    form_class = ArticleForm

class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news/'
    template_name = 'webapp/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Your form is wrong'
    form = ArticleForm
    context = {
        'form': form,
        'error': error
    }
    return render(request,'webapp/create.html', context)