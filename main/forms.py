from django.forms import ModelForm
from main.models import Product

# untuk deploy ulang
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]