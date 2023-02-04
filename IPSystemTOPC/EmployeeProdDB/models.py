from django.db import models

class Upload(models.Model):
    file = models.FileField(upload_to='Uploaded CSV/')

    class Meta:
        app_label = 'your_app_name'