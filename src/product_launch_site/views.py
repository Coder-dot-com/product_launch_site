from django.shortcuts import render

def home(request):

    context = {
    }

    return render(request, 'home_site/index.html', context=context)



def robots_txt(request):
    return render(request, 'robots.txt')

