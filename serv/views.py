from django.shortcuts import render

# Create your views here.
def service_page(requerst):
    return render(requerst,'serv/service.html')