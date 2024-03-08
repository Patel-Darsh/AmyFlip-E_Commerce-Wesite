from django import forms
from electronic.models import Item,Checkout
from django.core.exceptions import ValidationError


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['prod_code', 'item_name', 'item_desc', 'item_category','item_price', 'features_prod','item_image']

    def clean_item_price(self):
        item_price = self.cleaned_data['item_price']
        if item_price == 0:
            raise ValidationError("Price cannot be 0.")
        return item_price
    


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['address', 'city', 'state', 'country', 'pincode']

    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if user.is_authenticated:
            self.fields['firstname'].initial = user.first_name
            self.fields['lastname'].initial = user.last_name
            self.fields['email'].initial = user.email
