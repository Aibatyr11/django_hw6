from django.db import models
from django.core.exceptions import ValidationError


def positive_number_validator(value):
    if value < 0:
        raise ValidationError(f'{value} is not a positive number or zero.')


class Human(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


    def title_and_content(self):
        return f"Title: {self.name}, Content: Age: {self.age}, Height: {self.height}"



class Children(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey(Human, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    def title_and_content(self):
        return f"Title: {self.name}, Content: Age: {self.age}, Height: {self.height}"


class IceCream(models.Model):
    size = models.IntegerField(null=True, blank=True, validators=[positive_number_validator])
    price = models.IntegerField(null=True, blank=True, validators=[positive_number_validator])
    kiosk = models.ForeignKey('Kiosk', related_name='ice_creams', on_delete=models.CASCADE)

    def __str__(self):
        return f'Ice Cream size {self.size}, price {self.price}'


    def price_and_published(self):
        return f"Price: {self.price}, Published: {'Yes' if self.kiosk else 'No'}"


class Kiosk(models.Model):
    quantity_of_icecream = models.IntegerField(null=True, blank=True, validators=[positive_number_validator])
    size = models.IntegerField(null=True, blank=True, validators=[positive_number_validator])


    class Meta:
        verbose_name = "Kiosk"
        verbose_name_plural = "Kiosks"
        ordering = ['size']

    def __str__(self):
        return f'Kiosk size {self.size}'


    def title_and_content(self):
        return f"Title: Kiosk {self.size}, Content: Ice cream quantity {self.quantity_of_icecream}"

