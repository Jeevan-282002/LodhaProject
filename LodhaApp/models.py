from django.db import models

# Create your models here.

class EnquiryModel2(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    city = models.CharField(max_length=100)
    updates = models.CharField(max_length=100)
    enq_formate = models.CharField(max_length=100)

class MQEnquiryModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    city = models.CharField(max_length=100)
    updates = models.CharField(max_length=100)
    enq_formate = models.CharField(max_length=100)



class WT4BHKBookings2(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    dob =  models.DateField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    How_do_you_hear = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)





class WT5BHKBookings(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    dob =  models.DateField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    How_do_you_hear = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class MQ3BHKBookings(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    dob =  models.DateField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    How_do_you_hear = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class MQ4BHKBookings(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    dob =  models.DateField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField()
    How_do_you_hear = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


#
# feedbacks

class ReviewModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    review = models.TextField(max_length=200)
