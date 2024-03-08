from django.contrib import admin
from electronic.models import Item, Category,CartItem,Checkout
# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Checkout)
