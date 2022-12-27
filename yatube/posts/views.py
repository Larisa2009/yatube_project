from django.shortcuts import HttpResponse

# Create your views here.
# Главная страница
def index(request):    
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Посты, отфильтрованные по группам {slug}')