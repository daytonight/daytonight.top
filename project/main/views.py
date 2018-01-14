from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


# 个人主页
def home_page(request):
    return render(request, 'main/home_page.html')