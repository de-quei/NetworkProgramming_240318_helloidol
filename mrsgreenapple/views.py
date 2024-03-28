from django.shortcuts import render

# Create your views here.
def show_omori_html(request):
    return render(request, 'mrsgreenapple/omori.html')

def show_wakai_html(request):
    return render(request, 'mrsgreenapple/wakai.html')