import random
import os

from django.db import models
from django.db.models.query import QuerySet

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3910908400)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "goods/{new_filename}/{final_filename}".format(new_filename = new_filename, final_filename = final_filename)

class GoodManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) #Good.objects self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None


class Good(models.Model): #Good_category
    id          = models.AutoField(primary_key=True)
    description = models.CharField(max_length=120)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    objects = GoodManager()
    
    def __str__(self):
        return str(self.id)

    def __str__(self):
        return str(self.description)

#class Stock(models.Model):
#    id          = models.ForeignKey("Good", to_field='id')
#    whid        = models.PositiveIntegerField(blank=True, null=True)
#    amount      = models.PositiveIntegerField(default=0)

# class Aorder(models.Model):
    # ordernum    = models.AutoField(prmary_key=True)
    # ID          = models.ForeignKey("Good", to_field='id')
    # description = models.CharField(max_length=120)
    # amount      = models.PositiveIntegerField(default=0)
    # ups         = models.CharField(max_lengh=60) #ups account id
    # whid        = models.PositiveIntegerField(blank=True, null=True)
    # desx        = models.IntegerField(default=0)
    # dexy        = models,IntegerField(default=0)
    # goodid      = models.PositiveIntegerField(blank=True, null=True)
    # truckid     = models.PositiveIntegerField(blank=True, null=True)
    # truck_ready = models.BooleanField(default=False)
    # pack_ready  = models.BooleanField(default=False)
    # load_ready  = models.BooleanField(default=False)
    # delivered   = models.BooleanField(default=False)
    # userid      = models.ForeignKey("auth_user", to_field='id')


