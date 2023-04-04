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
    report_no = models.AutoField(primary_key=True)
    #employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    prod_date = models.DateField(null=True)
    workinghours = models.DurationField()
    remarks = models.TextField(max_length=2000, blank=True)
    prod_score = models.FloatField(null=True)
    joborder_no = models.CharField(max_length=10)
    process = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

#    class Meta:
#        constraints = [
#            models.ForeignKeyConstraint(
#                ['employee_id'], 
#                ['employee.employee_id'], 
#                name='productivity_fk'
#            )
#        ]

#class JobOrder(models.Model):
    #joborder_no = models.CharField(max_length=10, primary_key=True)
    #report_no = models.ForeignKey('Productivity', on_delete=models.CASCADE)
    #process = models.CharField(max_length=255)
    #status = models.CharField(max_length=255)


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

# class SummaryPR(models.Model):
#     productivity_score = models.IntegerField()
#     date = models.DateField()
#     totalworkhrs = models.DurationField()

class SummaryReport(models.Model):
    sr_no = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255, default="No Name")
    prod_score = models.FloatField()
    date = models.DateField()
    totalworkhrs = models.DurationField()

    def getSrno(self):
        return self.sr_no
    
    def getEmployeename(self):
        return self.employee_name
    
    def getProdScore(self):
        return self.prod_score
    
    def getDate(self):
        return self.date
    
    def __str__(self):
        return "pk: " + str(self.pk) + ": " + str(self.sr_no) + ", " + self.employee_name + ", " + str(self.prod_score) + ", " + str(self.date)

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

class IPSUser(models.Model):
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
