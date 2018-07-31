from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)


class Office(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField()


class City(models.Model):
    name = models.CharField(max_length=20)


class Flight(models.Model):
    flight_number = models.CharField(max_length=30)
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    airplane_model = models.CharField(max_length=50)
    max_weight = models.IntegerField()
    cost = models.BigIntegerField()
    capacity = models.IntegerField()
    flight_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    national_code = models.CharField(max_length=10)
    sex = models.BooleanField()
    date_of_birth = models.DateField()


class Ticket(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
