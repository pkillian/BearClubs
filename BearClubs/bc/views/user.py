from django.shortcuts import render

def userSignUp(request):
    return render(request, 'signup.html');
