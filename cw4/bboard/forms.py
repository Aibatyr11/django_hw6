from django.forms import ModelForm
from .models import *

class HumanForm(ModelForm):
    class Meta:
        model = Human
        fields = ('name', 'age', 'height')


class ChildrenForm(ModelForm):
    class Meta:
        model = Children
        fields = ('name', 'age', 'height')


class IceCreamForm(ModelForm):
    class Meta:
        model = IceCream
        fields = ('size', 'price')


class KioskForm(ModelForm):
    class Meta:
        model = Kiosk
        fields = ('quantity_of_icecream', 'size')
