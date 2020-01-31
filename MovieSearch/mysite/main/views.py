import json
import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import auth
from .forms import *
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from .models import *
#from .forms import UserForm

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

from django.shortcuts import redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import CustomUserChangeForm
from django.views.decorators.csrf import csrf_exempt




def __unicode__(self):
    return u'Proposal for: %s' % self.project.name

def index(request):
    return render(request,'main/main.html')

def movies(request):
    return render(request,'main/movies.html')

def profile(request):
    pflist = User.objects.all()
    return render(request,'main/profile.html',
                 {'pflist':pflist})

def popup(request):
    return render(request,'main/popup.html')


def write(request):
    if request.method == 'POST':
        print("머고")
        form = Form(request.POST)
        
        ###form = Form(initial={'name': 'root', 'email':'na1234@naver.com', 'title':'sibal','comment':'dqwdqwd'})
       # print(form)
        #print(form.is_valid())
        if form.is_valid():
           # print(form)
            form.save()
            return render (request, 'main/popup.html' , {'form':form})
    else:
        form =Form()
    return render (request, 'main/write.html' , {'form':form})



def board(request):
    boardlist = Users.objects.all()
    return render(request,'main/board.html',
                 {'boardlist':boardlist})
    
def boardlist(request,pk):
    lists = Users.objects.get(pk=pk)
    return render(request,'main/boardlist.html',
                 {'lists':lists})   

def signup(request):    
    if request.method =='POST':
        user = User.objects.create_user(username=request.POST['username'],password=request.POST["password"],email=request.POST["email"], photo=request.POST.get("photo"),user_comment=request.POST.get("user_comment"), selected1=request.POST["selected1"],selected2=request.POST["selected2"],selected3=request.POST["selected3"],selected4=request.POST["selected4"],selected5=request.POST["selected5"])
    # user_comment 왜해놓음 ? 프로필수정으로할거아님?
	
	
	
	
	
       # form=CustomUserCreationForm(request.POST)
      #  if form.is_valid():
       #     print(user)
       #     form.save() 
        return render (request,'main/success.html')  
   # else :
        #form=CustomUserCreationForm()  
        
    return render(request, 'main/signup.jsp')

    

def success(request):
    return render(request,'main/success.html')

def delete(request, pk): #게시판삭제
    dels = Users.objects.get(pk=pk)
    dels.delete()
    return render(request,'main/main.html')

def edit(request, pk):  #게시판수정
    listedit = Users.objects.get(pk=pk)
    if request.method == "POST":
        form = Form(request.POST)
		#print(form)
        if form.is_valid():
            listedit.title = form.cleaned_data['title']
            listedit.comment = form.cleaned_data['comment']
            listedit.save()
            return redirect('/board/'+str(listedit.pk))  # 물어볼까봐씀 redirect = URL불러오기 render = 템플릿불러오기
    else:
        form = Form()
        return render(request, 'main/write.html',{'form':form})
	
    
def login(request):
    if request.method =="POST":
        username =request.POST["username"]
        password =request.POST["password"]
        user = auth.authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'main/main.html')
        else:
            return render(request,'main/login.html',{'ERROR'})
    else:
        return render(request,'main/login.html')

   
def logout(request):
    auth.logout(request)
    return render(request,'main/main.html')

def useredit(request):  #프로필수정
   # edituser = User.objects.all()
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        print(user_change_form)
        print(user_change_form.is_valid())
        if user_change_form.is_valid():
            #user_comment = form.cleaned_data['user_comment']
           # edituser.photo = form.cleaned_data['photo']
            user_change_form.save()
            return render(request, 'main/profile.html',{'user_change_form':user_change_form})
    else:
        user_change_form = CustomUserCreationForm(instance=request.user)
        return render(request, 'main/useredit.html',{'user_change_form':user_change_form})

    
#@csrf_exempt
def search_restful(request):
    search_term1 = request.GET['search_term']
    subscription_key = "8723311019d84791961586339c4086b0"
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    search_term = search_term1+' movie'
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}

    params  = {"q": search_term, "license": "all", "imageType": "photo", "aspect" : "tall"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    
    search_term_link= search_results["value"][0]["contentUrl"]
    context={'search_term_link':search_term_link}
    print(context['search_term_link'])
    return HttpResponse(json.dumps(context['search_term_link']), content_type="application/json")