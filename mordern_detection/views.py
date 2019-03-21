from django.shortcuts import render

def homepage(request):
    return render(request,'homepage.html')

def idea(request):
    return render(request,'idea.html')

def team(request):
    return render(request,'team.html')

def planning(request):
    return render(request,'planning.html')

def content(request):
    return render(request,'content.html')

def resources(request):
    return render(request,'resources/resources_poly.html')

def resources_1(request):
    return render(request,'resources/kejian.html')

def resources_2(request):
    return render(request,'resources/anli.html')

def resources_3(request):
    return render(request,'resources/qita.html')

def activities(request):
    return render(request,'activities.html')