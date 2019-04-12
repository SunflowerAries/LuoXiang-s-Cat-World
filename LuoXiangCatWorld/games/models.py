from django.db import models
from django.urls import reverse
import uuid
# Create your models here.

class Cat(models.Model):
    #Fields
    # cat_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20, help_text="Enter this cat's name")
    sex_option = (
        ('♂', '♂'),
        ('♀', '♀'),
    )
    sex = models.CharField(max_length=1, choices=sex_option, blank=True)
    birth = models.DateField(null=True, blank=True)
    age = models.IntegerField()
    breed = models.CharField(max_length=20, blank=True, null=True)
    hunger_status = (
        ('s', 'I\'m Starving!'),
        ('p', 'Pretty Hungry'),
        ('h', 'Hungry'),
    )

    hunger = models.CharField(max_length=1, choices=hunger_status, blank=True, default='h')
    picture = models.ImageField(upload_to='Cat')

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Master(models.Model):
    name = models.CharField(max_length=20, help_text="Explore with a lovely name")
    # user_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    sex_option = (
        ('♂', '♂'),
        ('♀', '♀'),
    )
    sex = models.CharField(max_length=1, choices=sex_option, blank=True)
    money = models.IntegerField(default=200)
    password = models.CharField(max_length=20)
    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Food(models.Model):
    # food_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20)
    CHOICES = [(i,i) for i in range(1, 6)]
    effect = models.IntegerField(choices=CHOICES)
    picture = models.ImageField(upload_to='Food')

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Market(models.Model):
    # market_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='Market')

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Park(models.Model):
    # park_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='Park')
    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class Adopt(models.Model):
    cat = models.ForeignKey('Cat', on_delete=models.SET_NULL, null=True)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)
    park = models.ForeignKey('Park', on_delete=models.SET_NULL, null=True)
    time = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["master", "cat"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.cat.name + " and " + self.master.name + "'s first encounter"

class Wild(models.Model):
    cat = models.ForeignKey('Cat', on_delete=models.SET_NULL, null=True)
    park = models.ForeignKey('Park', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["park"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.cat.name + "'s old home"

class Store(models.Model):
    food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)
    num = models.IntegerField(default=0)
    class Meta:
        ordering = ["master"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.master.name + "'s refrigerator"

class Sell(models.Model):
    food = models.ForeignKey('Food', on_delete=models.SET_NULL, null=True)
    market = models.ForeignKey('Market', on_delete=models.SET_NULL, null=True)
    num = models.IntegerField()
    price = models.IntegerField()
    class Meta:
        ordering = ["price", "-num"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.market.name + "'s cates"

class Feed(models.Model):
    cat = models.ForeignKey('Cat', on_delete=models.SET_NULL, null=True)
    master = models.ForeignKey('Master', on_delete=models.SET_NULL, null=True)
    intimacy = models.IntegerField(default=50)
    class Meta:
        ordering = ["master", "cat"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.master.name + "and" + self.cat.name + "'s interaction"
