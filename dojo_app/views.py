from django.shortcuts import render, redirect

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
        return redirect(request, "result.html", context)
    return render(request, "result.html")