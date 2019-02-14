from django.http import HttpResponse
from django.shortcuts import render
from .models import Number

def Show(request, id):
    # id = str(id) + str(id) + str(id)
    id_text = str(id) * 3
    context = {
        'num': id_text
    }
    return render(request, 'threenum.html',context)

def InputNum(request):
    return render(request,'Input.html')

def mul(request):
    list_num = []
    for i in range(1,13):
        num = int(request.POST['number']) * i
        list_num.append(num)
    context = {
        'id': request.POST['number'],
        'num': list_num
    }
    return render(request, 'Mul.html', context)

def keep(request):
    keepnum = Number.objects.get(id=request.POST['number'])
    keepnum.count += 1
    keepnum.save()
    context = {
        'id' : request.POST['number'] ,
    }

    return render(request, 'keep.html', context)


