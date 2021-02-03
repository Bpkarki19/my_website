from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Homepage
from .models import Cards


#def index(request):
    #return HttpResponse(print(Homepage.id))
    #return HttpResponse(print(Homepage.objects.all())) gives none; id also gives none | you can also use formated string
    
def index(request):  #home
    text = Homepage.objects.all()
    context = {'text': text,}
    return render(request, 'webapp/index.html',context)


#def shop(request):
    #return HttpResponse('this is my shop')

def creat_card(request):
    image = 
    text = Cards.objects.all()
    contex = {}
    return render(request, 'webapp/shop.html', contex)