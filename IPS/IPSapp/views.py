from django.shortcuts import render, redirect
import io
import csv
from datetime import datetime, timedelta
from .models import Productivity, User, SummaryReport
from django.contrib import messages
from django.utils.dateparse import parse_date, parse_duration
# from dateutil.parser import parse as parse_date
from django.views.generic import View
# from chartjs.views.lines import BaseLineChartView
# import Chart from 'chart.js/auto';
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse

def home(request):
        return render(request, 'EmployeeProdDB/home.html')


def my_view(request):
    user = User.objects.getUsername()
    return render(request, 'EmployeeProdDB/base.html', {'user': user})

# def show_csv_data2(request):
#     csv_data = SummaryReport.objects.all()
#     return render(request, 'EmployeeProdDB/show_csv_data2.html', {'csv_data': csv_data})


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        confirm_pword = request.POST.get('confirm_password')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        bday = request.POST.get('birthday')
        sex = request.POST.get('sex')

        if pword==confirm_pword:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already taken.')
                return redirect('signup')
            else:
                user = User.objects.create(username = uname, password = pword, first_name = fname, last_name = lname, birthday = bday, sex = sex)
                user.save()
                messages.success(request, 'User account created.')
                return redirect('loginpage')
        
        else:
            messages.info(request, 'Password does not match. Please try again.')
            return redirect('signup')
            
    else:
        return render(request, 'EmployeeProdDB/signup.html')
    
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

# def upload_csv(request):
#     if request.method == 'POST':
#         csv_file = request.FILES['csv_file']
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request, 'This is not a CSV file')
#         else:
#             # read the data from the uploaded file
#             csv_data = csv.reader(
#                 (line.decode('utf-8') for line in csv_file),
#                 delimiter=',',
#                 quotechar='"'
#             )
#             #Loop through data rows
#             for i, row in enumerate(csv_data):
#                 # Check if this row is the start of a new report
#                 if row[0] == 'PRODUCTIVITY REPORT':
#                     # Reset variables for the new report
#                     sr_no = row[1]
#                     employee_name= None
#                     prod_score = None
#                     date = None
#                     totalworkhrs = None
#                 # Check if this is the fifth row after the start of the report
#                 elif i == 4 and employee_name is None:
#                     employee_name = row[0]
#                 # Check if this row contains a date and "Total Duration:" and "Productivity %"
#                     if len(row) > 2 and "/" in row[0] and "Total Duration:" in row and "Productivity %" in row:
#                         date = datetime.strptime(row[0], '%m/%d/%Y').date()
#                         totalworkhrs = timedelta(hours=float(row[row.index("Total Duration:") + 2]))
#                         prod_score = int(row[row.index("Productivity %") + 2])
#                         summary_pr = SummaryReport.objects.create(sr_no=sr_no, employee_name=employee_name, prod_score=prod_score, date=date, totalworkhrs=totalworkhrs)
#                         summary_pr.save()
#             return redirect('home')
#     return render(request, 'EmployeeProdDB/upload_csv.html')






def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file')
        else:
            # Read the data from the uploaded file
            csv_data = csv.DictReader(csv_file.read().decode('utf-8').splitlines())
            
            # Loop through data rows
            for row in csv_data:
                # Convert duration string to a Duration object
                working_hours = row['Work Hours']
                if working_hours:
                    hours, minutes, seconds= map(int, working_hours.split(':'))
                    working_hours = timedelta(hours=hours, minutes=minutes, seconds=seconds)
                
                # Create a new SummaryReport object
                summary_report = SummaryReport.objects.create(
                    employee_name=row['Employee Name'],
                    prod_score=row['Productivity Score'],
                    date=row['Date'],
                    totalworkhrs=working_hours
                )

            return render(request, 'EmployeeProdDB/upload_csv.html', {'message': 'Data imported successfully!'})

    return render(request, 'EmployeeProdDB/upload_csv.html')


def chart_template(request):
    data = SummaryReport.objects.values('employee_name').annotate(total_prod_score=Sum('prod_score')).order_by('-total_prod_score')[:10]
    labels = list(map(lambda x: x['employee_name'], data))
    data = list(map(lambda x: x['total_prod_score'], data))
    return render(request, 'EmployeeProdDB/chart_template.html', {
        'labels': labels,
        'data': data,
    })



# def upload_csv(request):
#     if request.method == 'POST':
#         csv_file = request.FILES['csv_file']
#         if not csv_file.name.endswith('.csv'):
#             messages.error(request, 'This is not a CSV file')
#         else:
#             # read the data from the uploaded file
#             csv_data = csv.reader(
#                 (line.decode('utf-8') for line in csv_file),
#                 delimiter=',',
#                 quotechar='"'
#             )

#             encountered_empty_row = False

#             # Loop through data rows
#             for i, row in enumerate(csv_data):
#                 # Check if this row is the start of a new report
#                 if row[0] == 'PRODUCTIVITY REPORT':
#                     # Reset variables for the new report
#                     report_no = row[1]
#                     employee = None
#                     prod_date = None
#                     workinghours = None
#                     remarks = None
#                     prod_score = None
#                     joborder_no = None
#                     process = None
#                     status = None

#                     # Skip 8 rows
#                     count = 0
#                     while count < 8:
#                         next(csv_data)
#                         count += 1

#                     # Reset the flag for encountered empty row
#                     encountered_empty_row = False

#                     # Read headers from 9th row
#                     headers = next(csv_data)
#                     jo_no_index = headers.index('JO NO')
#                     status_index = headers.index('Status')
#                     process_index = headers.index('Process')
#                     duration_index = headers.index('Duration')
#                     remarks_index = headers.index('Remarks')
#                 elif all(cell == '' for cell in row):
#                     # Check if an empty row has been encountered before
#                     if encountered_empty_row:
#                         # Stop processing data as we have encountered two consecutive empty rows
#                         break
#                     else:
#                         # Set the flag to indicate that an empty row has been encountered
#                         encountered_empty_row = True
#                 else:
#                     # Read data from the row
#                     joborder_no = row[jo_no_index]
#                     status = row[status_index]
#                     process = row[process_index]
#                     workinghours = row[duration_index]
#                     remarks = row[remarks_index]

#                     # Convert working hours to a Duration object
#                     if workinghours:
#                         hours, minutes = map(int, workinghours.split(':'))
#                         workinghours = timedelta(hours=hours, minutes=minutes)

#                     # Create a new productivity object
#                     Productivity.objects.create(
#                         #report_no=report_no,
#                         #employee=employee,
#                         #prod_date=prod_date,
#                         workinghours=workinghours,
#                         remarks=remarks,
#                         #prod_score=prod_score,
#                         joborder_no=joborder_no,
#                         process=process,
#                         status=status
#                     )

#             return render(request, 'EmployeeProdDB/upload_csv.html', {'message': 'Data imported successfully!'})

#     return render(request, 'EmployeeProdDB/upload_csv.html')

# def chart_view(request):
#     Define the data pool
#     data_pool = DataPool(
#         series=[{
#             'options': {
#                 'source': SummaryPR.objects.all()
#             },
#             'terms': [
#                 'my_field_1',
#                 'my_field_2',
#             ]
#         }]
#     )

#     # Define the chart
#     chart = Chart(
#         datasource=data_pool,
#         series_options=[{
#             'options': {
#                 'type': 'pie',
#                 'stacking': False
#             },
#             'terms': {
#                 'my_field_1': 'my_field_2'
#             }
#         }]
#     )

#     # Render the chart template
#     return render(request, 'chart_template.html', {
#         'chart': chart,
#     })

def show_csv_data(request):
    csv_data = Productivity.objects.all()
    return render(request, 'EmployeeProdDB/show_csv_data.html', {'csv_data': csv_data})
    
def show_csv_data2(request):
    csv_data = SummaryReport.objects.all()
    return render(request, 'EmployeeProdDB/show_csv_data2.html', {'csv_data': csv_data})

# Create your views here.
