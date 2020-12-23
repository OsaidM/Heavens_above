from django.db import models
from urllib import request
import re, bcrypt
# Create your models here.

'''
this command to create a user with the admin role:
User.objects.create(first_name = 'Omar', last_name = 'alqasem', email = 'omar@gmail.com', address = 'tulkarm', password = '123', role = Role.objects.create(isAdmin = True, isUser = False))
----
create new product:
Product.objects.create(title='starsframe',description='thshdishdhasd',image='asdasdasd',price='99.89')
----

create new order:
Order.objects.create(name = 'stars',date_of_birth ='2020-12-23' ,place_of_birth ='ramallah',phone ='0597102030',user_id = User.objects.get(id = 1),product_id = Product.objects.get(id = 1))

---
Create new like:
this_user = User.objects.get(id=1)
this_product = Product.objects.get(id=1)
this_user.liked_products.add(this_product)
---
Create new review:
Review.objects.create(content='asfasbdafdsfbf',product_id=this_product,user_id=this_user)
'''

class Role(models.Model):
    isAdmin = models.BooleanField(null=False)
    isUser = models.BooleanField(null=True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now_add = True)



class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    address = models.CharField(max_length = 255)
    password = models.CharField(max_length = 45)
    role = models.ForeignKey(Role, related_name='role', on_delete= models.CASCADE)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now_add = True)


class Product(models.Model):
    title = models.CharField(max_length = 45)
    description = models.TextField()
    image = models.ImageField(blank = True, null = True)
    price = models.FloatField()
    like = models.ManyToManyField(User, related_name = 'liked_products')
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now_add = True)


class Review(models.Model):
    content= models.TextField(null=False)
    product_id= models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now_add = True)

class Order(models.Model):
    name = models.CharField(max_length = 60)
    date_of_birth =  models.DateField()
    place_of_birth = models.CharField(max_length = 60)
    phone = models.CharField(max_length = 10)
    user_id= models.ForeignKey(User, on_delete=models.CASCADE)
    product_id= models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now_add = True)

