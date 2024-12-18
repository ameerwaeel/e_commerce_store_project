from django.shortcuts import render

# Create your views here.
def settings(request):
    context={'settings':'settings'}
    return render(request,'settings.html',context)