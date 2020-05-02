from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from .models import Quiz
from rest_framework import generics
from .serializers import QuizSerializers
# Create your views here.

def home(request):
    return render(request, 'quiz/home.html')


def quizroom(request):
    results = Quiz.objects.all()
    return render(request, 'quiz/quizroom.html',{'results':results})
    #return JsonResponse({'results':results})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'quiz/signupuser.html', {'form': UserCreationForm()})
    else:
        #create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'quiz/signupuser.html',{'forms':UserCreationForm(),'error':"That user name has been taken. Please try someother username"})
        else:
            return render(request, 'quiz/signupuser.html',{'forms':UserCreationForm(), 'error':'password did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'quiz/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request,username = request.POST['username'],password = request.POST['password'])
        if user is None:
            return render(request, 'quiz/loginuser.html', {'form':AuthenticationForm,'error':'Username and password did not match'})
        else:
            login(request,user)
            return redirect('home')

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

class QuizAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers

class QuizAPIDetailView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializers





        


        