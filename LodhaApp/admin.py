from django.contrib import admin
from . models import  EnquiryModel2, MQEnquiryModel, WT5BHKBookings , MQ3BHKBookings, MQ4BHKBookings, WT4BHKBookings2, ReviewModel

# Register your models here.




@admin.register(EnquiryModel2)
class EnquiryAdmin2(admin.ModelAdmin):
    list_display = ["name","email","contact","city", "updates", "enq_formate" ]

@admin.register(MQEnquiryModel)
class MQEnquiryAdmin(admin.ModelAdmin):
    list_display = ["name","email","contact","city", "updates", "enq_formate" ]



@admin.register(WT4BHKBookings2)
class WT4BHKAdmin(admin.ModelAdmin):
    list_display = ["full_name","username","address","email","dob" ,"state","city","pincode","How_do_you_hear", "contact","password"]



@admin.register(WT5BHKBookings)
class WT5BHKAdmin(admin.ModelAdmin):
    list_display = ["full_name","username","address","email","dob" ,"state","city","pincode","How_do_you_hear", "contact","password"]

@admin.register(MQ3BHKBookings)
class MQ3BHKAdmin(admin.ModelAdmin):
    list_display = ["full_name","username","address","email","dob" ,"state","city","pincode","How_do_you_hear", "contact","password"]
    

@admin.register(MQ4BHKBookings)
class MQ4BHKAdmin1(admin.ModelAdmin):
    list_display = ["full_name","username","address","email","dob" ,"state","city","pincode","How_do_you_hear", "contact","password"]


#feedback
@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "review"]


#wt4BHK payment

