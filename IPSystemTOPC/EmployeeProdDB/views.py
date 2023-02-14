import csv
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Productivity
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_duration
from dateutil.parser import parse as parse_date

def home(request):
        return render(request, 'EmployeeProdDB/index.html')

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file')
        else:
            # read the data from the uploaded file
            csv_data = csv.reader(
                (line.decode('utf-8') for line in csv_file),
                delimiter=',',
                quotechar='"'
            )

            # create and save model instances for each row of data
            for row in csv_data:
                report_no = row[0]
                employee_id = row[1]
                prod_date_str = row[2]
                #prod_date = row[2]
                prod_date = None
                if prod_date_str:
                    prod_date = parse_date(prod_date_str)
                workinghours_str = row[3]
                workinghours = None
                if workinghours_str:
                    workinghours = parse_duration(workinghours_str)
                remarks = row[4]
                prod_score = row[5]

                Productivity.objects.create(
                    report_no=report_no,
                    employee_id=employee_id,
                    prod_date=prod_date,
                    workinghours=workinghours,
                    remarks=remarks,
                    prod_score=prod_score,
                    # add more fields as needed
                )

            return redirect('show_csv_data')

    return render(request, 'EmployeeProdDB/upload_csv.html')


def show_csv_data(request):
    csv_data = Productivity.objects.all()
    return render(request, 'EmployeeProdDB/show_csv_data.html', {'csv_data': csv_data})
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
    

