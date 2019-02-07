from django.http import HttpResponse

def Cal(request, id):
    id = str(id) + str(id) + str(id)
    return HttpResponse(id)