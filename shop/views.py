from django.shortcuts import render


def index(request):
    context = {
        'a': 'hello',
    }
    return render(request, 'shop/index.html', context)
