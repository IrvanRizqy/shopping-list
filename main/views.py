from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Irvan Rizqy Kusuma',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)