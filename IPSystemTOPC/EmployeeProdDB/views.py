from django.shortcuts import render, redirect
from .models import Upload


from django.shortcuts import render

#def handle_file_upload(request):
#    if request.method == 'POST':
#        file = request.FILES.get('file-input')
        # You can now process the file as needed
        # ...
#    return render(request, 'uploadpage.html')

def upload_file(request):
    if request.method == 'POST':
        form = Upload(request.POST.get('file'), request.FILES.get('file'))
        if form.is_valid():
            form.save()
            return redirect('success_url')
    else:
        form = Upload()
    return render(request, 'uploadpage.html', {'form': form})

def index(request):
    return render(request, 'employeeproddb/index.html')
    

