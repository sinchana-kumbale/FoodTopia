from django.shortcuts import render
from Login.models import Login
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        post=Login.objects.get(username=username)
        if (post):
            if (post.password==password):
                return render(request, "homepage.html")
            else:
                return render(request,"index2.html")
                '''lst=Login()
        lst.user=username
        lst.pwd=password
    
        lst.save()
        return render(request,'offers.html')'''
    else:
        
        return render(request,"index2.html")

def signup(request):
    if request.method=="POST"and "cancel" not in request.POST:
        print("hhhh")
        username=request.POST['username']
        password=request.POST['password']
        lst=Login()
        lst.username=username
        lst.password=password
    
        lst.save()
        return render(request,'index2.html')
    else:
        return render(request,'signup.html')

def Delhi(request):
    if request.method=="POST":
        return render(request,'delhi.html')
    else:
        return render(request,'delhi.html')
def offers(request):
    if request.method=="POST":
        return render(request,'offers.html')
    else:
        return render(request,'offers.html')
    
    
