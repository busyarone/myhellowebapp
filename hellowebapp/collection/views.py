from django.shortcuts import render
from collection.models import Thing

# Create your views here.
def index(request):
    number = 6
    thing = "Thing name"
    name = "Arone Arokiasami"
    things = Thing.objects.all()
    return render(request,'index.html',
                  {'number':number,
                   'thing':thing,
                   'name':name,
                   'things':things,})