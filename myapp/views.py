from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
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
    get_num = request.POST['number']
    list_num = []
    for i in range(1,13):
        num = int(get_num) * i
        list_num.append(num)
    try: 
        keep_num = Number.objects.get(Number_text=request.POST['number'])
    except (KeyError, Number.DoesNotExist):
        keep_num = Number(Number_text=request.POST['number'])
        keep_num.save()
    else:
        keep_num.count += 1
        keep_num.save()
    
    context = {
        'get_num': request.POST['number'],
        'list_num': list_num,
        'keep': keep_num.count
    }
    return render(request, 'keep.html', context)



