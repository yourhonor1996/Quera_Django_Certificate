from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=32, default='9T Pro')
    price = models.PositiveIntegerField(default=2097152)
    color = models.CharField(max_length=16, default='Black')
    display_size = models.SmallIntegerField(default=4)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return '{} {}'.format(self.brand.name, self.model)
