from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'edu/about.html')
