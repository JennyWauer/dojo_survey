
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def home(request):
    return render(request, "index.html")

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['survey_result'] = {
            "name": request.POST['name'],
            "location": request.POST['location'],
            "fav": request.POST['fav'],
            "comment": request.POST['comment'],
    }
    return redirect('result/')

def result(request):
    context = {
        'your_answer': request.session['survey_result']
    }
    return render(request, "result.html", context)