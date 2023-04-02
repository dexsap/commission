import io
import csv
from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Productivity, User, Employee
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_duration
from dateutil.parser import parse as parse_date

def home(request):
        return render(request, 'EmployeeProdDB/home.html')


def loginpage(request):
    if(request.method == "POST"):
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        accountList = User.objects.filter(username = uname)

        if(len(accountList) > 0):
            findUser = User.objects.get(username= uname)

            if(findUser.getPassword() == pword):
                global loggedInUser
                loggedInUser = findUser
                messages.success(request, 'SUCCESSFULLY LOGGED IN!')
                return redirect('home')
            else:
                messages.info(request, 'Invalid Username or Password')
                return render(request, 'EmployeeProdDB/loginpage.html')
        else:
            messages.info(request, 'User Account Not Found')
            return render(request, 'EmployeeProdDB/loginpage.html')
    else:
        return render(request, 'EmployeeProdDB/loginpage.html')

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

            encountered_empty_row = False

            # Loop through data rows
            for i, row in enumerate(csv_data):
                # Check if this row is the start of a new report
                if row[0] == 'PRODUCTIVITY REPORT':
                    # Reset variables for the new report
                    report_no = row[1]
                    employee = None
                    prod_date = None
                    workinghours = None
                    remarks = None
                    prod_score = None
                    joborder_no = None
                    process = None
                    status = None

                    # Skip 8 rows
                    count = 0
                    while count < 8:
                        next(csv_data)
                        count += 1

                    # Reset the flag for encountered empty row
                    encountered_empty_row = False

                    # Read headers from 9th row
                    headers = next(csv_data)
                    jo_no_index = headers.index('JO NO')
                    status_index = headers.index('Status')
                    process_index = headers.index('Process')
                    duration_index = headers.index('Duration')
                    remarks_index = headers.index('Remarks')
                elif all(cell == '' for cell in row):
                    # Check if an empty row has been encountered before
                    if encountered_empty_row:
                        # Stop processing data as we have encountered two consecutive empty rows
                        break
                    else:
                        # Set the flag to indicate that an empty row has been encountered
                        encountered_empty_row = True
                else:
                    # Read data from the row
                    joborder_no = row[jo_no_index]
                    status = row[status_index]
                    process = row[process_index]
                    workinghours = row[duration_index]
                    remarks = row[remarks_index]

                    # Convert working hours to a Duration object
                    if workinghours:
                        hours, minutes = map(int, workinghours.split(':'))
                        workinghours = timedelta(hours=hours, minutes=minutes)

                    # Create a new productivity object
                    Productivity.objects.create(
                        #report_no=report_no,
                        #employee=employee,
                        #prod_date=prod_date,
                        workinghours=workinghours,
                        remarks=remarks,
                        #prod_score=prod_score,
                        joborder_no=joborder_no,
                        process=process,
                        status=status
                    )

            return render(request, 'EmployeeProdDB/upload_csv.html', {'message': 'Data imported successfully!'})

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
    

