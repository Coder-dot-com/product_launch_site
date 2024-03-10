from django.shortcuts import render

def home(request):

    context = {
    }

    return render(request, 'home_site/index.html', context=context)



def robots_txt(request):
    return render(request, 'robots.txt')

def tandc(request):
    return render(request, 'home_site/pages/tandc.html')


def privpolicy(request):
    context = {
    }
    return render(request, 'home_site/pages/privpolicy.html', context=context)