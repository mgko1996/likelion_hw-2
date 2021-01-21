from django.shortcuts import render

def first(request):
    return render(request, 'post2/first.html')


def second(request):
    return render(request, 'post2/second.html')


def third(request):
    return render(request, 'post2/third.html')