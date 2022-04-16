from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=128)

    created_at = models.DateTimeField(default=timezone.now,editable=False)

class Subcategory(models.Model):
    category_relate = models.ForeignKey(
        to = Category,
        on_delete=models.CASCADE,
    )

    subcategory_name = models.CharField(max_length=128)

    created_at = models.DateTimeField(default=timezone.now,editable=False)

class Announcement(models.Model):


    announce = models.CharField(max_length=256)

    created_at = models.DateTimeField(default=timezone.now,editable=False)
