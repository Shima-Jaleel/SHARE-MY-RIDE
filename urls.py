"""
URL configuration for sharemyride project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('adminhome/',views.admin_home),

    path('login/', views.admin_login),
    path('login_post/', views.login_post),

    path('view_user/',views.view_user),
    path('view_user_post/',views.view_user_post),

    path('admin_view_rating/',views.admin_view_rating),
    path('admin_view_rating_post/',views.admin_view_rating_post),

    path('add_notification/',views.add_notification),
    path('add_notification_post/',views.add_notification_post),

    path('notification/',views.notification),
    path('notification_post/',views.notification_post),

    path('delete_notification/<id>',views.delete_notification),

    path('view_blk_users/',views.view_blk_users),
    path('view_blk_drivers/', views.view_blk_drivers),

    path('view_detection/', views.view_detection),

    path('report/', views.report),
    path('report_post/', views.report_post),

    path('driver/', views.driver),
    path('driver_post/', views.driver_post),

    path('admin_approve_driver/<id>', views.admin_approve_driver),
    path('admin_reject_driver/<id>', views.admin_reject_driver),

    path('approved_driver/', views.approved_driver),
    path('approved_driver_post/', views.approved_driver_post),

    path('reject_driver/', views.reject_driver),
    path('reject_driver_post/', views.reject_driver_post),

    path('admin_view_user_complaints/', views.admin_view_user_complaints),
    path('admin_view_user_complaints_search/', views.admin_view_user_complaints_search),
    path('adminsentreplyuser/', views.adminsentreplyuser),

    path('admin_view_user_request/', views.admin_view_user_request),
    path('admin_view_user_request_search/', views.admin_view_user_request_search),
    path('adminsentactionuser/', views.adminsentactionuser),

    path('admin_view_driver_request/', views.admin_view_driver_request),
    path('admin_view_driver_request_search/', views.admin_view_driver_request_search),
    path('adminsentreplydriver/', views.adminsentreplydriver),


######################  DRIVER  #############


    path('and_login/', views.and_login),
    path('signup/', views.signup),
    path('driver_view_profile/', views.driver_view_profile),

    path('add_ride/', views.add_ride),
    path('view_journey/', views.view_journey),
    path('edit_journey/', views.edit_journey),
    path('update_journey/', views.update_journey),
    path('delete_journey/', views.delete_journey),

    path('driver_view_seats/', views.driver_view_seats),
    path('driver_add_seat/', views.driver_add_seat),
    path('driver_edit_seat/', views.driver_edit_seat),
    path('driver_update_seat/', views.driver_update_seat),
    path('delete_seat/', views.delete_seat),

    path('driver_view_notification/', views.driver_view_notification),

    path('view_booking_user/', views.view_booking_user),
    path('Verify_user/', views.Verify_user),

    path('driver_send_block/', views.driver_send_block),
    path('driver_view_action/', views.driver_view_action),

    path('driver_view_user/', views.driver_view_user),

    path('driver_send_notif/', views.driver_send_notif),
    path('driver_view_n_reply/', views.driver_view_n_reply),
    path('user_rep_notif/', views.user_rep_notif),

    path('user_view_n_reply/', views.user_view_n_reply),



######################  USER  #############


    path('user_signup/', views.user_signup),
    path('user_view_profile/', views.user_view_profile),
    path('user_Changepassword/', views.user_Changepassword),
    path('view_driver/', views.view_driver),
    path('view_rating/', views.view_rating),
    path('view_new_journey/', views.view_new_journey),
    path('book_jorney/', views.book_jorney),
    path('view_book_status/', views.view_book_status),
    path('user_send_complaint/', views.user_send_complaint),
    path('user_view_reply/', views.user_view_reply),
    path('user_sendfeedback/', views.user_sendfeedback),

    path('user_send_block/', views.user_send_block),
    path('user_view_action/', views.user_view_action),

    path('add_lost/', views.add_lost),
    path('view_lost/', views.view_lost),
    path('view_others_lost/', views.view_others_lost),
    path('delete_lost/', views.delete_lost),


    path('update_location/', views.update_location),
    path('user_editprofile/', views.user_editprofile),



]

