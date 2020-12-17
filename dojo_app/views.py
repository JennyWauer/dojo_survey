from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def result(request):
    if request.method == 'POST':
        context = {
            "name": request.POST['name'],
            "location": request.POST['location'],
            "fav": request.POST['fav'],
            "comment": request.POST['comment'],
        }
        return render(request, "result.html", context)