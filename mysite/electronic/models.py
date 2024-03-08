from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#----------------------------------Category table-----------------------------------
class Category(models.Model):
    category_name = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.category_name


#----------------------------------Products table-----------------------------------
class Item(models.Model):
    prod_code = models.IntegerField(default=50)
    company_owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = 1
    )
    added_by = models.CharField(
        max_length = 100,
        default = 'user'
    )
    item_name = models.CharField(
        max_length = 100,
        default = ''
    )
    item_desc = models.CharField(
        max_length = 5000,
        default = 'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Animi facilis saepe sit quaerat quos harum necessitatibus quod dolore ut alias quis nostrum illum, quasi aspernatur et in rerum rem reiciendis!'
    )
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to='products_pictures', default='prod_pic.jpg')
    item_category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)
    features_prod = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
    

class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(
            (
                self.product,
                self.quantity,
                self.user
            )
        )



class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
