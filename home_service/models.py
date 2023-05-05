from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.city

class Status(models.Model):
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.status

class FStatus(models.Model):
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.status

class ID_Card(models.Model):
    card = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.card
    
class FID_Card(models.Model):
    card = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.card

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name

class Service_Man(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    doj = models.DateField(null=True)
    dob = models.DateField(null=True)
    id_type = models.CharField(max_length=100, null=True)
    service_name = models.CharField(max_length=100, null=True)
    experience = models.CharField(max_length=100, null=True)
    id_card = models.FileField(null=True)
    image = models.FileField(null=True)
    latitude = models.FloatField(null=True)
    longitude= models.FloatField(null = True)

    def __str__(self):
        return self.user.first_name

class Fuel_man(models.Model):
    status = models.ForeignKey(FStatus, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    id_type = models.CharField(max_length=100, null=True)
    service_name = models.CharField(max_length=100, null=True)
    id_card = models.FileField(null=True)
    image = models.FileField(null=True)
    latitude = models.FloatField(null=True)
    longitude= models.FloatField(null = True)

    def __str__(self):
        return self.user.first_name



class Service_Category(models.Model):
    category = models.CharField(max_length=30, null=True)
    desc = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    total=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category

class FService_Category(models.Model):
    category = models.CharField(max_length=30, null=True)
    desc = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    total=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category  

class Service(models.Model):
    category = models.ForeignKey(Service_Category,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service_Man, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.service.user.first_name

class Contact(models.Model):
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True)
    message1 = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    def __str__(self):
        return self.name

class Total_Man(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.service.user.first_name

class Order(models.Model):
    report_status = models.CharField(max_length=100, null=True)
    status = models.ForeignKey(Status,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Service_Man, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    book_date = models.DateField(null=True)
    book_days = models.CharField(max_length=100, null=True)
    book_hours = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.service.user.first_name+" "+self.customer.user.first_name

class FOrder(models.Model):
    report_status = models.CharField(max_length=100, null=True)
    status = models.ForeignKey(FStatus,on_delete=models.CASCADE,null=True)
    service = models.ForeignKey(Fuel_man, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    vehicle_no = models.CharField(max_length=100,null=True)
    book_days = models.CharField(max_length=100, null=True)
    book_hours = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.service.user.first_name+" "+self.customer.user.first_name


def get_file_path(request,filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)

class Pcategory(models.Model):
    slug = models.CharField(max_length=150, null = False, blank=False)
    name = models.CharField(max_length=150, null = False, blank = False)
    image = models.ImageField(upload_to=get_file_path,null = True, blank=True)

    def __str__(self):
        return self.name

class Pcategory1(models.Model):
    pcategory = models.ForeignKey(Pcategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    name = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.name



class Carbrand(models.Model):
    carbrand = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.carbrand
    
class Carmodel(models.Model):
    carbrand = models.ForeignKey(Carbrand,on_delete=models.CASCADE)
    carmodel = models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.carmodel

class Product(models.Model):
    category = models.ForeignKey(Pcategory1,on_delete=models.CASCADE)
    carbrand = models.ForeignKey(Carbrand, on_delete=models.CASCADE, null=True, blank=True)
    carmodel = models.ForeignKey(Carmodel, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    product_image1 = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    product_image2 = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    small_description = models.CharField(max_length=250,null=False,blank=False)
    quantity = models.IntegerField(null = False,blank = False)
    description = models.TextField(max_length=500,null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
   
    def __str__(self):
        return self.slug
    
