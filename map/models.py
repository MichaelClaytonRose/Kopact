from django.db import models

class Location(models.Model):
    location_name = models.CharField(max_length=50)
    location_information = models.TextField(default='Sorry, we currently have no information about this company. Hopefully they will update their profile soon!')
    location_latitude = models.DecimalField(max_digits=20, decimal_places=8)
    location_longitude = models.DecimalField(max_digits=20, decimal_places=8)
    Drink = 'Drink'
    Nightclub = 'Nightclub'
    Shop = 'Shop'
    Food = 'Food'
    Other = 'Other'
    location_type_choices = (
        (Drink, 'Drink'),
        (Nightclub, 'Nightclub'),
        (Shop, 'Shop'),
        (Food, 'Food'),
        (Other, 'Other')
                            )
    location_type = models.CharField(max_length=20, choices=location_type_choices)
    x = models.IntegerField(default=0)
    z = models.IntegerField(default=0)
    u = models.IntegerField(default=0)
    def __str__(self):
        return self.location_name
