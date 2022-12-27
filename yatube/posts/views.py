from django.shortcuts import HttpResponse, render

# Create your views here.
# Главная страница
def index(request):
    template = 'posts/index.html'
    context = {
        # В словарь можно передать переменную
        'message': 'Это главная страница проекта Yatube',
        # А можно сразу записать значение в словарь. Но обычно так не делают
        
    }
    return render(request, template, context)
    


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    context = {
        # В словарь можно передать переменную
        'message': 'Здесь будет информация о группах проекта Yatube',
        # А можно сразу записать значение в словарь. Но обычно так не делают
        
    }
    return render(request, template, context)
    