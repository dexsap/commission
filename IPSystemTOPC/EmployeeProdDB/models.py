from django.db import models
#from .employee import Employee

class Upload(models.Model):
    file = models.FileField(upload_to='Uploaded CSV/')

    class Meta:
        app_label = 'your_app_name'

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, primary_key=True)
    employee_fname = models.CharField(max_length=255)
    employee_mname = models.CharField(max_length=255, blank=True, null=True)
    employee_lname = models.CharField(max_length=255)
    employee_sex = models.CharField(max_length=1)
    employee_bday = models.DateField()
    employee_email = models.CharField(max_length=255)
    employee_num = models.CharField(max_length=10, blank=True, null=True)
    employee_emergnum = models.CharField(max_length=10, blank=True, null=True)

#    class Meta:
#        db_table = 'employee'

class Productivity(models.Model):
    report_no = models.CharField(max_length=10, primary_key=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    prod_date = models.DateField()
    workinghours = models.DurationField()
    remarks = models.TextField(max_length=2000, blank=True)
    prod_score = models.FloatField(null=True)

#    class Meta:
#        constraints = [
#            models.ForeignKeyConstraint(
#                ['employee_id'], 
#                ['employee.employee_id'], 
#                name='productivity_fk'
#            )
#        ]

class JobOrder(models.Model):
    joborder_no = models.CharField(max_length=10, primary_key=True)
    report_no = models.ForeignKey('Productivity', on_delete=models.CASCADE)
    process = models.CharField(max_length=255)
    status = models.CharField(max_length=255)


class Position(models.Model):
    position_id = models.CharField(max_length=10, primary_key=True)
    history_no = models.CharField(max_length=10)
    position_name = models.CharField(max_length=255)

#    class Meta:
#        constraints = [
#            models.ForeignKeyConstraint(
#                ['history_no'], 
#                ['history.history_no'], 
#                name='position_fk'
#            )
#        ]

class History(models.Model):
    history_no = models.CharField(max_length=10, primary_key=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    employee_fname = models.CharField(max_length=255)
    employee_mname = models.CharField(max_length=255, blank=True)
    employee_lname = models.CharField(max_length=255)
    position_name = models.CharField(max_length=255)
    position_startdate = models.DateField()
    position_enddate = models.DateField(null=True)

#    class Meta:
#        constraints = [
#            models.ForeignKeyConstraint(
#                ['employee_id'], 
#                ['employee.employee_id'], 
#                name='history_fk1'
#            ),
#            models.ForeignKeyConstraint(
#                ['position_id'], 
#                ['position.position_id'], 
#                name='history_fk2'
#            )
#        ]

class Dashboard(models.Model):
    dashboard_id = models.CharField(max_length=10, primary_key=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    report_no = models.CharField(max_length=255)
    timespan = models.DurationField()
    displaytype = models.CharField(max_length=255)
    total_workinghours = models.DurationField()
    contribution = models.CharField(max_length=10)
    avgprodscore = models.FloatField()

#    class Meta:
#        constraints = [
#            models.ForeignKeyConstraint(
#                ['employee_id'], 
#                ['employee.employee_id'], 
#                name='dashboard_fk1'
#            ),
#            models.ForeignKeyConstraint(
#                ['report_no'], 
#                ['productivity.report_no'], 
#                name='dashboard_fk2'
#            )
#        ]

class User(models.Model):
    username = models.CharField(max_length=300, unique=True)
    password = models.CharField(max_length=300)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    birthday = models.DateField()
    sex = models.CharField(max_length=50)
    objects = models.Manager()

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def getBirthday(self):
        return self.birthday

    def getSex(self):
        return self.sex

    def __str__(self):
        return "pk: " + str(self.pk) + ": " + self.username + ", " + self.first_name + " " + self.last_name + ", " + str(self.birthday) + ", " + self.sex
