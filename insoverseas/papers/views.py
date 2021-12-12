from django.shortcuts import render
from.models import Contact

# Create your views here.


def index (request):
    return render(request,'index.html')



def about (request):
    return render(request,'about.html')



def contact (request):
    thank = False
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})




def fatorytour (request):
    return render(request,'factorytour.html')












def boxes (request):
    return render(request,'boxes.html')



def cards (request):
    return render(request,'cards.html')





def christmas (request):
    return render(request,'Christmas.html')





def gift (request):
    return render(request,'gift.html')



def journal (request):
    return render(request,'journal.html')



def lamp (request):
    return render(request,'lamp.html')



def papers (request):
    return render(request,'papers.html')



def papersbag (request):
    return render(request,'papersbag.html')




def seedpapers (request):
    return render(request,'seedpapers.html')




