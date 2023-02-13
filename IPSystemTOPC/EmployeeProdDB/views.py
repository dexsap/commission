import csv
from datetime import datetime
from django.shortcuts import render
from .models import Productivity


from django.shortcuts import render

def home(request):
        return render(request, 'EmployeeProdDB/index.html')

def csv_import(request):
    with open('C:\Users\dxsap\Downloads\IPS_dummy_data.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            my_model = Productivity(
                field1=row[0],
                field2=row[1],
                field3=datetime.strptime(row[2], '%Y-%m-%d').date()
            )
            my_model.save()
    return render(request, 'csv_imported.html')
#def handle_file_upload(request):
#    if request.method == 'POST':
#        file = request.FILES.get('file-input')
        # You can now process the file as needed
        # ...
#    return render(request, 'uploadpage.html')

#def login_page(request):
#        return render(request, 'loginpage.html')

#def upload_file(request):
#    if request.method == 'POST':
#        form = Upload(request.POST.get('file'), request.FILES.get('file'))
#        if form.is_valid():
#            form.save()
#            return redirect('success_url')
#    else:
#        form = Upload()
#    return render(request, 'uploadpage.html', {'form': form})

#def index(request):
#    return render(request, 'index.html')
    

