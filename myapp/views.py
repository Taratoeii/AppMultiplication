from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def Cal(request, id):
    # id = str(id) + str(id) + str(id)
    id_text = str(id)
    context = {
        'name': "what",
    }
    return render(request, 'Show.html',context)

def InputNum(request):
    return HttpResponseRedirect(reverse('polls:Cal'))