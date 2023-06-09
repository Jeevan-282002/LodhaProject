from django.urls import path
from . import views


urlpatterns = [

    # user

    path("",views.home_view, name = "userhome"),
    path("projects/", views.projects_view, name = "projects"),
    path("bookings/", views.bookings_view, name = "bookings"),
    path("about/", views.about_view, name = "about"),
    path("review/", views.review_view, name = "review"),
    path("write_review/", views.write_review_view, name = "write_review"),
    path("articles/", views.articles_view, name = "articles"),

    # admin

    path("adminlogin/", views.adminlogin_view, name = "adminlogin"),
    path("callrequests/", views.callrequests_view, name = "callrequests"),
    path("wt_callback/", views.wt_callback_view, name = "wt_callback"),
    path("mq_callback/", views.mq_callback_view, name = "mq_callback"),
    path("bookingselection/", views.bookingselection_view, name = "bookingselection"),
    path("wt_bookings/", views.wt_bookings_view, name = "wt_bookings"),
    path("wt_bookings2/", views.wt_bookings2_view, name = "wt_bookings2"),
    path("mq_bookings/", views.mq_bookings_view, name = "mq_bookings"),
    path("mq_bookings2/", views.mq_bookings2_view, name = "mq_bookings2"),
    path("signout/", views.signout_view, name = "signout"),
    path("admin_review/", views.admin_review_view, name = "admin_review"),
    




    # the world tower section
    path("wt_home/", views.wt_home_view, name = "wt_home"),
    path("wt_location/", views.wt_location_view, name = "wt_location"),
    path("wt_plan/", views.wt_plan_view, name = "wt_plan"),
    path("wt_amenties/", views.wt_amenties_view, name = "wt_amenties"),
    path("wt_gallery/", views.wt_gallery_view, name = "wt_gallery"),
    path("wt_bhkselection/", views.wt_bhkselection_view, name = "wt_bhkselection"),
    path("wt_4bhkbookings/", views.wt_4bhkbookings_view, name = "wt_4bhkbookings"),
    path("wt_5bhkbookings/", views.wt_5bhkbookings_view, name = "wt_5bhkbookings"),
    path("wt_4bhkpayment/", views.wt_4bhkpayment_view, name = "wt_4bhkpayment"),
    path("wt_4bhkotp/", views.wt_4bhkotp_view, name = "wt_4bhkotp"),
    path("paymentsuccess/", views.paymentsuccess_view, name = "paymentsuccess"),


    # the Marquise section
    path("mq_home/", views.mq_home_view, name = "mq_home"),
    path("mq_location/", views.mq_location_view, name = "mq_location"),
    path("mq_plan/", views.mq_plan_view, name = "mq_plan"),
    path("mq_amenties/", views.mq_amenties_view, name = "mq_amenties"),
    path("mq_gallery/", views.mq_gallery_view, name = "mq_gallery"),
    path("mq_bhkselection/", views.mq_bhkselection_view, name = "mq_bhkselection"),
    path("mq_3bhkbookings/", views.mq_3bhkbookings_view, name = "mq_3bhkbookings"),
    path("mq_4bhkbookings/", views.mq_4bhkbookings_view, name = "mq_4bhkbookings"),
    path("services/", views.services_view, name = "services"),

   
]