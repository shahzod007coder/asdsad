from django.shortcuts import render
from main.models import *

def index(request):
    # categoriya = Categoriya.objects.all()
    # categoriyaproduct = CategoriyaProduct.objects.all()
    #
    # ctx = {
    #     "categoriya":categoriya,
    #     "categoriyaproduct":categoriyaproduct
    # }
    return render(request, 'main/index.html')
