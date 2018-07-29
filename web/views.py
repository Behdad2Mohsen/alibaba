from django.shortcuts import render

app_name = "web"


def index(request):
    return render(request, 'index.html')
