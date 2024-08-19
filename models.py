from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Company(models.Model):
    # LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneno = models.BigIntegerField()
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode= models.BigIntegerField()
    established_date = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)


class Vehicle(models.Model):
    vehicle = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    feature = models.CharField(max_length=100)
    drivername = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    regno= models.CharField(max_length=100)
    typeofvehicle= models.CharField(max_length=100)
    amountperhour = models.CharField(max_length=100)


class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    housename = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode= models.BigIntegerField()
    phoneno = models.BigIntegerField()
    email= models.CharField(max_length=100)
    photo= models.CharField(max_length=100)

# class Report(models.Model):
#     VEHICLE = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     USER = models.ForeignKey(User, on_delete=models.CASCADE)
#     rental_date= models.CharField(max_length=100)
#     total_hour= models.CharField(max_length=100)
#     rental_income = models.BigIntegerField()
#     expense = models.BigIntegerField()
# class Charge(models.Model):
#     VEHICLE = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     date = models.CharField(max_length=100)
#     hour = models.CharField(max_length=100)
#     amountperhour = models.CharField(max_length=100)

class Booking(models.Model):
    USER = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status  = models.CharField(max_length=100)
    VEHICLE = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    from_time = models.CharField(max_length=100)
    to_time = models.CharField(max_length=100)

class Payment(models.Model):
    BOOKING = models.ForeignKey(Booking, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(User , on_delete=models.CASCADE)
    amount = models.BigIntegerField(max_length=100)

class Request(models.Model):
    VEHICLE = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    hours_extra = models.CharField(max_length=100)

class Complaint(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    VEHICLE = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=250)
    date = models.CharField(max_length=100)
    reply = models.CharField(max_length=250)
    status = models.CharField(max_length=100)

class Review(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    VEHICLE = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    review = models.CharField(max_length=250)

