
from django.shortcuts import render

from Project.models import vechile

# Create your views here.
def index(request):

    
    vech1 = vechile()
    vech1.name = "Auto"
    vech1.desc = "Get affortable Auto rides with no haggling. Request  Auto and ride comfortably around your city"
    vech1.price = 30
    vech1.img = 'auto.png'

    vech2 = vechile()
    vech2.name = "Moto"
    vech2.desc = "Get affortable bike rides at your doorstep . skip the crowd and Zip through traffic with Moto"
    vech2.price = 20
    vech2.img = 'Moto.png'

    vech3 = vechile()
    vech3.name = "Rentals"
    vech3.desc = "Book Rentals to save time with one car and driver for mult-stop trips."
    vech3.price = 35
    vech3.img = 'Rentals.png'

    vech4 = vechile()
    vech4.name = "Intercity"
    vech4.desc = "Book intercity to head outstation anytime in convenient and affortable cars"
    vech4.price = 40
    vech4.img = 'Intercity.png'

    vechs = [vech1,vech2,vech3,vech4]

    return render(request, "index.html",{'vechs': vechs})