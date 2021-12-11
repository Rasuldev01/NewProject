from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


def upload_to(instance, filename):
    return f'posts/{filename}'.format(filename=filename)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_to, default='posts/default.jpg')
    price = models.IntegerField(default=0)
    info = models.CharField(max_length=200)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
