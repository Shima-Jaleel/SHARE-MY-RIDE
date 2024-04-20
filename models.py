from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class user(models.Model):
    name = models.CharField(max_length=100)
    Houseno = models.CharField(max_length=100)
    idproof = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)

class Driver(models.Model):
    givennamed = models.CharField(max_length=100)
    taximodel = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    idproof = models.CharField(max_length=500)
    # lastlogindate = models.DateField()
    status = models.CharField(max_length=100, default=0)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default='')

class review(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateField()
    review = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)

class Notification(models.Model):
    # USER = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.DateField()
    notification = models.CharField(max_length=100)

class Record(models.Model):
    # USER = models.ForeignKey(user, on_delete=models.CASCADE)
    DRIVER = models.ForeignKey(Driver, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rating = models.CharField(max_length=100, default="")

class Report(models.Model):
    Date = models.DateField()
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class complaints(models.Model):
    date = models.DateField()
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=100)
    replay = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class UserRequest(models.Model):
    date = models.DateField()
    DRIVER = models.ForeignKey(Driver, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    request = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    action = models.CharField(max_length=100)

class DriverRequest(models.Model):
    date = models.DateField()
    DRIVER = models.ForeignKey(Driver, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    request = models.CharField(max_length=100)
    action = models.CharField(max_length=100)

class Journey(models.Model):
    DRIVER = models.ForeignKey(Driver, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    Typeofvehicle = models.CharField(max_length=100)
    seats = models.CharField(max_length=100)


class Availableseats(models.Model):
    JOURNEY = models.ForeignKey(Journey, on_delete=models.CASCADE)
    available = models.CharField(max_length=100)
    booked = models.CharField(max_length=100)

class Book(models.Model):
    Status = models.CharField(max_length=100)
    Booking = models.CharField(max_length=100)
    Date = models.DateField()
    AVAILABLESEATS = models.ForeignKey(Availableseats, on_delete=models.CASCADE,default=1)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class Feedback(models.Model):
    Date = models.DateField()
    Feedback = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE,default="1")

class Lost(models.Model):
    Date = models.DateField()
    Object = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default="1")

class Delay(models.Model):
    date = models.DateField()
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    notification = models.CharField(max_length=100)
    replay = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    DRIVER = models.ForeignKey(Driver, on_delete=models.CASCADE)

class Location(models.Model):
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)
