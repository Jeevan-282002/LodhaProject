from django.shortcuts import render, redirect
from . forms import EnquiryForm, MQEnquiryForm , WT5BHKForm, MQ3BHKForm, MQ4BHKForm, WT4BHKForm2, LoginForm, ReviewForm
from django.contrib.auth import authenticate , login , logout
from . models import EnquiryModel2, MQEnquiryModel, WT4BHKBookings2, WT5BHKBookings,MQ3BHKBookings,MQ4BHKBookings, ReviewModel
from django.contrib import messages
import random
# Create your views here.

# user

def home_view(request):
    return render(request, "LodhaApp/userhome.html")

def projects_view(request):
    return render(request, "LodhaApp/projects.html")

def bookings_view(request):
    return render(request, "LodhaApp/bookings.html")

def about_view(request):
    return render(request, "LodhaApp/about.html")

def review_view(request):
    data = ReviewModel.objects.all()
    context = {"data":data}
    return render(request, "LodhaApp/review.html", context)

def write_review_view(request):
    form = ReviewForm()
    if request.method == "POST":
        new_name = request.POST["name"]
        new_title = request.POST["title"]
        new_review = request.POST["review"]
        print(new_name)
        print(new_title)
        print(new_review)
        data = ReviewModel(name = new_name, title = new_title, review = new_review)
        data.save()
        messages.success(request, "Review Posted Successfully!")
        return redirect("userhome")

    context = {"form":form}
    return render(request, "LodhaApp/world_tower/wt_write_review.html", context)


def articles_view(request):
    return render(request, "LodhaApp/articles.html")

# admin 




def adminlogin_view(request):
    form = LoginForm()
    context = {"form":form}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username , password = password)

        if user is not None:
            login(request,user)
            messages.success(request, "Admin logged in successfully")
            return redirect('bookingselection')
        else:
            messages.warning(request, "Something went wrong")
            return redirect("userhome")
    return render(request, "LodhaApp/adminlogin.html", context)


def admin_review_view(request):
    data = ReviewModel.objects.all()
    context = {"data":data}
    return render(request,"LodhaApp/admin/admin_review.html", context)

def callrequests_view(request):
    return render(request, "LodhaApp/admin/callrequests.html")

def wt_callback_view(request):
    data1 = EnquiryModel2.objects.all()
    
    context = {"data1":data1}
    return render(request, "LodhaApp/admin/wt_callback.html", context)

def mq_callback_view(request):
    data2 = MQEnquiryModel.objects.all()
    context = {"data2":data2}
    return render(request, "LodhaApp/admin/mq_callback.html", context)

def bookingselection_view(request):
    return render(request, "LodhaApp/admin/bookingselection.html")



def wt_bookings_view(request):
    data1 = WT4BHKBookings2.objects.all()
    context = {"data1":data1}
    return render(request, "LodhaApp/admin/wt_bookings.html", context)

def wt_bookings2_view(request):
    data2 = WT5BHKBookings.objects.all()
    context = {"data2":data2}
    return render(request, "LodhaApp/admin/wt_bookings.html", context)


def mq_bookings_view(request):
    data1 = MQ3BHKBookings.objects.all()
    context = {"data1":data1}
    return render(request, "LodhaApp/admin/mq_bookings.html", context)

def mq_bookings2_view(request):
    data2 = MQ4BHKBookings.objects.all()
    context = {"data2":data2}
    return render(request, "LodhaApp/admin/mq_bookings.html", context)

def signout_view(request):
    if request.method == "POST":
        logout(request)
        messages.warning(request, "Admin Logged Off")
        return redirect("userhome")







    # the world tower section

def wt_home_view(request):
    form = EnquiryForm()
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Enquiry for 'The World Tower' is successfully requested!")
            return redirect("wt_home")
    context = {"form": form}
    return render(request, "LodhaApp/world_tower/wt_home.html", context)

def wt_location_view(request):
    return render(request, "LodhaApp/world_tower/wt_location.html")

def wt_plan_view(request):
    return render(request, "LodhaApp/world_tower/wt_plan.html")

def wt_amenties_view(request):
    return render(request, "LodhaApp/world_tower/wt_amenties.html")

def wt_gallery_view(request):
    return render(request, "LodhaApp/world_tower/wt_gallery.html")

def wt_bhkselection_view(request):
    return render(request, "LodhaApp/world_tower/wt_bhkselection.html")

def wt_4bhkbookings_view(request):
    form = WT4BHKForm2()
    if request.method == "POST":
        form = WT4BHKForm2(request.POST)
        if form.is_valid():
            print("data is valid")
            form.save()
            return redirect("wt_4bhkpayment")
    context = {"form":form}
    return render(request, "LodhaApp/world_tower/wt_4bhkbookings.html", context)

def wt_5bhkbookings_view(request):
    forms = WT5BHKForm()
    if request.method == "POST":
        forms = WT5BHKForm(request.POST)
        if forms.is_valid():
            forms.save()
            
            return redirect("wt_4bhkpayment")
            
    context = {"forms":forms}
    return render(request, "LodhaApp/world_tower/wt_5bhkbookings.html", context)

def wt_4bhkpayment_view(request):
    otp = random.randint(1000,9999)
    print(otp)
    context = {"otp":otp}
    return render(request, "LodhaApp/world_tower/wt_4bhkpayment.html", context)

def wt_4bhkotp_view(request):
    if request.method == "POST":
        print("method posted")
        entered_otp = request.POST['user_otp']
        system_otp = request.POST["system_otp"]
        print(entered_otp)
        print(system_otp)
        if entered_otp == system_otp:
            print("user verified")
            messages.success(request,"User verified")
            return redirect("wt_4bhkotp")
        else:
            print("user not verified")
            messages.warning(request, "OTP not verified")
            return redirect("wt_4bhkpayment")
    
    return render(request, "LodhaApp/world_tower/wt_4bhkotp.html")

def paymentsuccess_view(request):
    if request.method == "POST":
        messages.success(request, "Booking is successfull!!  Welcome to Lodha Family : )")
        return redirect("userhome")
        
        
    return render(request, "LodhaApp/world_tower/wt_home.html")





    # the marquise section

def mq_home_view(request):
    form = MQEnquiryForm()
    if request.method == "POST":
        form = MQEnquiryForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            messages.success(request, "Your Enquiry for 'Lodha Park-Marquise' is successfully requested!")
            return redirect("mq_home")
    context = {"form": form}
    return render(request, "LodhaApp/marquise/mq_home.html", context)

def mq_location_view(request):
    return render(request, "LodhaApp/marquise/mq_location.html")

def mq_plan_view(request):
    return render(request, "LodhaApp/marquise/mq_plan.html")

def mq_amenties_view(request):
    return render(request, "LodhaApp/marquise/mq_amenties.html")

def mq_gallery_view(request):
    return render(request, "LodhaApp/marquise/mq_gallery.html")

def mq_bhkselection_view(request):
    return render(request, "LodhaApp/marquise/mq_bhkselection.html")

def mq_3bhkbookings_view(request):
    forms = MQ3BHKForm()
    if request.method == "POST":
        forms = MQ3BHKForm(request.POST)
        if forms.is_valid():
            forms.save()
          
            return redirect("wt_4bhkpayment")
    context = {"forms":forms}
    return render(request, "LodhaApp/marquise/mq_3bhkbookings.html", context)

def mq_4bhkbookings_view(request):
    forms = MQ4BHKForm()
    if request.method == "POST":
        forms = MQ4BHKForm(request.POST)
        if forms.is_valid():
            forms.save()
          
            return redirect("wt_4bhkpayment")
            
    context = {"forms":forms}
    return render(request, "LodhaApp/marquise/mq_4bhkbookings.html", context)

def services_view(request):
    return render(request, "LodhaApp/marquise/mq_services.html")