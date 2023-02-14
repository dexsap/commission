from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('upload_csv/', views.upload_csv, name = 'upload_csv'),
    path('show_csv_data/', views.show_csv_data, name ='show_csv_data')
    #path('', views.login_page, name='loginpage'),

]