from django.urls import path

from app import views

urlpatterns=[
    path('add_Studenta', views.add_Studenta, name='add_Studenta'),
    path('view_Studenta', views.view_Studenta, name='view_Studenta'),
    path('', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
#########################
    path('admin_Temp', views.admin_Temp, name='admin_Temp'),
    path('add_Notification', views.add_Notification, name='add_Notification'),
    path('view_Notification', views.view_Notification, name='view_Notification'),
    path('view_Complaint', views.view_Complaint, name='view_Complaint'),

##################################################################################################################
    path('student_Temp', views.student_Temp, name='student_Temp'),
    path('add_Complaints', views.add_Complaints, name='add_Complaints'),
    path('view_Complaints', views.view_Complaints, name='view_Complaints'),
    path('view_Notifications', views.view_Notifications, name='view_Notifications'),
    path('view_Students', views.view_Students, name='view_Students'),


]