
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('home/',views.home),


    path('login/',views.login),
    path('loginpost/',views.loginpost),
    path('addcompany/',views.add_company),
    path('addcompanypost/',views.addcompanypost),
    path('editcompany/',views.edit_company),
    path('viewcompany/',views.view_company),
    path('addvehicle/',views.add_vehicle),
    path('editvehicle/',views.edit_vehicle),
    path('viewvehicle/',views.view_vehicle),
    path('addreport/',views.add_report),
    path('editreport/',views.edit_report),
    path('viewreport/',views.view_report),
    path('viewcomplaint/',views.view_complaint),
    path('sendreply/',views.send_reply),
    path('changepassword/',views.change_password),
    path('viewbooking/',views.view_booking),
    path('viewacceptbooking/',views.view_acceptbooking),
    path('viewrequest/',views.view_request),
    path('updatebooking/', views.update_booking),
    path('viewpayment/', views.view_payment),
    path('updatepayment/', views.update_payment),
    path('viewreview/', views.view_review),
    path('register/', views.register),
    path('viewprofile/', views.view_profile),
    path('edit_profile/', views.edit_profile),
    path('changepassworduser/', views.change_password_user),
    path('viewcompanyuser/', views.view_company_user),
    path('viewvehicleuser/', views.view_vehicle_user),
    path('addbooking/', views.add_booking),
    path('viewstatus/', views.view_status),
    path('sendrequest/', views.send_request),
    path('viewpaymentstatususer/', views.view_paymentstatus_user),
    path('sendcomplaint/', views.send_complaint),
    path('viewreply/', views.view_reply),
    path('sendreview/', views.send_review),





]
