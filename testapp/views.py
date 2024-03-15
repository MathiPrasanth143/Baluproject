from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def shirts_view(request):
    return render(request,'testapp/shirts.html')