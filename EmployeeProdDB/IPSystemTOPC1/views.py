from django.shortcuts import render, redirect
from .models import Upload


from django.shortcuts import render

def index(request):
    return render(request, 'books/index.html')
    
def upload_file(request):
    if request.method == 'POST':
        form = Upload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = Upload()
    return render(request, 'upload.html', {'form': form})
