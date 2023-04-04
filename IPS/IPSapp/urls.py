from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginpage, name='loginpage'),
    path('home/', views.home, name='home'),
    path('upload_csv/', views.upload_csv, name = 'upload_csv'),
    path('show_csv_data/', views.show_csv_data, name ='show_csv_data'),
    path('signup/', views.signup, name='signup'),
    path('show_csv_data2/', views.show_csv_data2, name='show_csv_data2'),
    path('chart_template/', views.chart_template, name='chart_template')
    # path('', views.login_page, name='loginpage'),

]