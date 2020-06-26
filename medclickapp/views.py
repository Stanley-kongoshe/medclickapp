from django.shortcuts import render


# Create your views here.

def homepage(request):
    return render(request, 'medclickapp/index.html')


# # def login_page(request):
#     return render(request, 'medclickapp/login.html')


# def signup_page(request):
#     return render(request, 'medclickapp/signup.html')
