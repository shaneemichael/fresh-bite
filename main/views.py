from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'freshbite2go',
        'name': 'Shane Michael Tanata Tendy',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)