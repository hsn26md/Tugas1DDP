from django.shortcuts import render

# Pastikan view memanggil 'WebProfile/...' (Sesuai nama folder yang kita buat tadi)
def home(request):
    return render(request, 'WebProfile/home.html')

def about(request):
    return render(request, 'WebProfile/about.html')

def gallery(request):
    return render(request, 'WebProfile/gallery.html')