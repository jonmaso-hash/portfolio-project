from django.shortcuts import render

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experince(request):
    return render(request, 'pages/experince.html')