from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from apptdd.models import Item
def home(request):

    '''if request.method=="POST":
        return HttpResponse(request.POST['new a item'])
    return render(request,'home.html')'''
    #return render(request,'home.html',{'new_item_text':request.POST['new a item']})
    ##item=Item()
    ##item.text=request.POST.get("new a item",'')
    ##item.save()


   # return render(request, 'home.html', {'new_item_text': request.POST.get('new a item','')})
    ##return render(request, 'home.html', {'new_item_text': item.text})
    if request.method=='POST':
        ###new_item_text=request.POST['new a item']
        ###Item.objects.create(text=new_item_text)
        Item.objects.create(text=request.POST['new a item'])
        return redirect('/apptdd/the-only-list-in-world/')
    ###else:
        ###new_item_text=''
    ###return render(request,'home.html',{'new_item_text':new_item_text,})
    ####return render(request,'home.html')
    items=Item.objects.all()
    return render(request,'home.html',{'items':items})
def view_lists(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})