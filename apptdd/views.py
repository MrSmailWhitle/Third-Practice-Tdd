from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    '''if request.method=="POST":
        return HttpResponse(request.POST['new a item'])
    return render(request,'home.html')'''
    #return render(request,'home.html',{'new_item_text':request.POST['new a item']})
    return render(request, 'home.html', {'new_item_text': request.POST.get('new a item','')})
