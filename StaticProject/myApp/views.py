from django.shortcuts import render

# Create your views here.
def my_view(request):
    myName="Daveed"
    favPlayer="Virat Kohli"
    favAnimal="Lion"
    favSubject="Python"
    d={"name": myName,"playername":favPlayer,"animal":favAnimal,"subject":favSubject}
    return render(request,"myApp/1.html",d)