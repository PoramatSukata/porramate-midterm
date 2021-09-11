from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render (request, 'index.html')
def patient(request):
    return render (request, 'patient.html')
def physician(request):
    return render (request, 'physician.html')
