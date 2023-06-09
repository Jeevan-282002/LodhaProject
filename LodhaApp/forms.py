from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from . models import  EnquiryModel2, MQEnquiryModel, WT5BHKBookings, MQ4BHKBookings, MQ3BHKBookings, WT4BHKBookings2, ReviewModel
 



# admin login

class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Enter Your Username' , widget=forms.TextInput(attrs={'class':'form-control'}))

    password = forms.CharField(label='Enter Your Password' , widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User



#world tower wnq model

updates_choices = [("Yes","Yes"), ("No","No")]
formate_choices = [("Enquire","Enquire"), ("site visit","site visit")]

class EnquiryForm(forms.ModelForm):
    updates = forms.ChoiceField(choices = updates_choices, label = "Receive updates on Whatsapp", widget=forms.RadioSelect)

    enq_formate = forms.ChoiceField(choices = formate_choices, label = "Enquiry type", widget=forms.RadioSelect)
    class Meta:
        model = EnquiryModel2
        fields = ["name", "email", "contact","city","updates","enq_formate" ]
        labels = {
            "name":"Enter Your Name",
            "email": "Enter Your Email",
            "contact":"Enter Your Contact",
            "city":"Enter Your City",   
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={"class":"form-control"}),
            "contact": forms.NumberInput(attrs={"class":"form-control"}),
            "city": forms.TextInput(attrs={"class":"form-control"}),
        }


# world tower 4 bhk bookings





add_choices = [("Lodha Booked Customer", "Lodha Booked Customer"), ("Corporate Customer","Corporate Customer"),("Online add, search or social","Online add, search or social")]



class WT4BHKForm2(forms.ModelForm):

    How_do_you_hear = forms.ChoiceField(choices= add_choices, label = "how do you hear", widget= forms.Select(attrs= {"class":"form-control"}))

    class Meta:

        model = WT4BHKBookings2

        fields = ["full_name","username","address","email","dob", "state","city","pincode","How_do_you_hear", "contact","password"]

        labels = {
            "full_name":"Enter Your full_name",
            "username":"Enter username",
            "address": "Enter Your address",
            "email":"Enter Your email",
            "dob":"Enter Your Date Of Birth",
            "state":"Enter Your State",
            "city": "Enter Your City",
            "pincode":"Enter Your Pincode",
            "How_do_you_hear":"Enter How do you hear about us",   
            "contact": "Enter Your Contact",
            "password":"Enter Your Password", 
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Full name" }),
            'username': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Username"}),
            "address": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Address"}),
            "email": forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}),
            "dob": forms.DateInput(attrs={"class":"form-control","placeholder":"Enter Date Of Birth"}),
            "state": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter State"}),
            "city": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter City"}),
            "pincode": forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Pincode"}),
            'contact': forms.NumberInput(attrs={'class':'form-control',"placeholder":"Enter Contact Number"}),
            "password": forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}),
        }


        
# world tower 5 bhk bookings

class WT5BHKForm(forms.ModelForm):

    How_do_you_hear = forms.ChoiceField(choices= add_choices, label = "how do you hear", widget= forms.Select(attrs= {"class":"form-control"}))

    class Meta:

        model = WT5BHKBookings

        fields = ["full_name","username","address","email","dob", "state","city","pincode","How_do_you_hear", "contact","password"]

        labels = {
            "full_name":"Enter Your full_name",
            "username":"Enter username",
            "address": "Enter Your address",
            "email":"Enter Your email",
            "dob":"Enter Your Date Of Birth",
            "state":"Enter Your State",
            "city": "Enter Your City",
            "pincode":"Enter Your Pincode",
            "How_do_you_hear":"Enter How do you hear about us",   
            "contact": "Enter Your Contact",
            "password":"Enter Your Password", 
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Full name" }),
            'username': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Username"}),
            "address": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Address"}),
            "email": forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}),
            "dob": forms.DateInput(attrs={"class":"form-control","placeholder":"Enter Date Of Birth"}),
            "state": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter State"}),
            "city": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter City"}),
            "pincode": forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Pincode"}),
            'contact': forms.NumberInput(attrs={'class':'form-control',"placeholder":"Enter Contact Number"}),
            "password": forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}),
        }

        



#Marquise enq model

class MQEnquiryForm(forms.ModelForm):
    updates = forms.ChoiceField(choices = updates_choices, label = "Receive updates on Whatsapp", widget=forms.RadioSelect)

    enq_formate = forms.ChoiceField(choices = formate_choices, label = "Enquiry type", widget=forms.RadioSelect)
    class Meta:
        model = MQEnquiryModel
        fields = ["name", "email", "contact","city","updates","enq_formate" ]
        labels = {
            "name":"Enter Your Name",
            "email": "Enter Your Email",
            "contact":"Enter Your Contact",
            "city":"Enter Your City",   
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            "email": forms.TextInput(attrs={"class":"form-control"}),
            "contact": forms.NumberInput(attrs={"class":"form-control"}),
            "city": forms.TextInput(attrs={"class":"form-control"}),
        }


# marquise 3 bhk booking

class MQ3BHKForm(forms.ModelForm):

    How_do_you_hear = forms.ChoiceField(choices= add_choices, label = "how do you hear", widget= forms.Select(attrs= {"class":"form-control"}))

    class Meta:

        model = MQ3BHKBookings

        fields = ["full_name","username","address","email","dob", "state","city","pincode","How_do_you_hear", "contact","password"]

        labels = {
            "full_name":"Enter Your full_name",
            "username":"Enter username",
            "address": "Enter Your address",
            "email":"Enter Your email",
            "dob":"Enter Your Date Of Birth",
            "state":"Enter Your State",
            "city": "Enter Your City",
            "pincode":"Enter Your Pincode",
            "How_do_you_hear":"Enter How do you hear about us",   
            "contact": "Enter Your Contact",
            "password":"Enter Your Password", 
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Full name" }),
            'username': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Username"}),
            "address": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Address"}),
            "email": forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}),
            "dob": forms.DateInput(attrs={"class":"form-control","placeholder":"Enter Date Of Birth"}),
            "state": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter State"}),
            "city": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter City"}),
            "pincode": forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Pincode"}),
            'contact': forms.NumberInput(attrs={'class':'form-control',"placeholder":"Enter Contact Number"}),
            "password": forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}),
        }




# marquise 4 bhk booking

class MQ4BHKForm(forms.ModelForm):

    How_do_you_hear = forms.ChoiceField(choices= add_choices, label = "how do you hear", widget= forms.Select(attrs= {"class":"form-control"}))

    class Meta:

        model = MQ4BHKBookings

        fields = ["full_name","username","address","email","dob", "state","city","pincode","How_do_you_hear", "contact","password"]

        labels = {
            "full_name":"Enter Your full_name",
            "username":"Enter username",
            "address": "Enter Your address",
            "email":"Enter Your email",
            "dob":"Enter Your Date Of Birth",
            "state":"Enter Your State",
            "city": "Enter Your City",
            "pincode":"Enter Your Pincode",
            "How_do_you_hear":"Enter How do you hear about us",   
            "contact": "Enter Your Contact",
            "password":"Enter Your Password", 
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Full name" }),
            'username': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Username"}),
            "address": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Address"}),
            "email": forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}),
            "dob": forms.DateInput(attrs={"class":"form-control","placeholder":"Enter Date Of Birth"}),
            "state": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter State"}),
            "city": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter City"}),
            "pincode": forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Pincode"}),
            'contact': forms.NumberInput(attrs={'class':'form-control',"placeholder":"Enter Contact Number"}),
            "password": forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}),
        }




# Feedback model

title_choices = [("The World Tower", "The World Tower"), ("Lodha Park- Marquise", "Lodha Park- Marquise")]

class ReviewForm(forms.ModelForm):

    title = forms.ChoiceField(choices= title_choices, label = "Enter Project Name", widget= forms.Select(attrs= {"class":"form-control"}))

    class Meta:
        model = ReviewModel
        fields = ["name","title","review"]
        labels = {
            "name":"Enter Username",
            "review":"Enter Review",
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control',"placeholder":"Enter Username"}),
            "title": forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Title"}),
            "review": forms.Textarea(attrs={"class":"form-control","placeholder":"Enter Review"}),
        }


# WT4bhk payment

