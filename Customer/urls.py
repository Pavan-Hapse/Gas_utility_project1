from django.urls import path
from . import views

app_name = 'Customer'

urlpatterns = [

    path('', views.index, name= 'index'),
    path('request/', views.request_list, name='request_list'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),

]
