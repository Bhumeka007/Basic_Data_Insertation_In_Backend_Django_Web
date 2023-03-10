from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.

def index(request):
    
    computer = Computer.objects.all()
    shirt = Shirt.objects.all()
    jumka = Jhumka.objects.all()
    kangan = Kangan.objects.all()
    laptop = Laptop.objects.all()
    mobile = Mobile.objects.all()
    neklesh = Neklesh.objects.all()
    tshirt = T_Shirt.objects.all()
    womenCloth = Women_Cloth.objects.all()

    context = {
        'Computers': computer,
        'Shirts': shirt,
        'Jumkas': jumka,
        'Kangans': kangan,
        'Laptops': laptop,
        'Mobiles': mobile,
        'Nekleshs': neklesh,
        'tshirt': tshirt,
        'WomenCloths': womenCloth,
        
    }
    
    return render(request, 'index.html', context=context)