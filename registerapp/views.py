from django.shortcuts import render
from .models import RegisterModel

def register(request):
    if request.method=="POST":
        print("in post requst")
        name = request.POST['name']  # here 'name' is same as name in the input for taking the input from frontend to backend
        email = request.POST['email']
        print("name:",name)
        print("email:",email)
        obj = RegisterModel.objects.create(name=name,email=email)
        obj.save()

    return render(request,'register/register.html')

def search(request):
    if request.method=="POST":
        if "id" in request.POST:
            obj=RegisterModel.objects.get(id=request.POST['id'])
            obj.delete()
            return render(request,'register/search.html',{})  # {} means that the full page should be shown
        name=request.POST['name']
        queryset=RegisterModel.objects.filter(name=name)
        return render(request,'register/search.html',{'data':queryset})
    return render(request,'register/search.html',{})

def update(request):
    if request.method=="POST":
        print("in Update Views")
        name = request.POST['name']
        email = request.POST['email']
        obj = RegisterModel.objects.get(id=int(request.POST['id']))
        obj.name = name
        obj.email = email
        obj.save()
        if request.POST['from'] == 'search':
            return render(request,'register/update.html', {'name':obj.name, 'email':obj.email, 'id':obj.id})
        return render(request,'register/register.html')

def index(request):
    return render(request,'register/index.html')
