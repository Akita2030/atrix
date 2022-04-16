from ast import Sub
from dataclasses import fields
from logging.config import valid_ident
from re import sub
from rest_framework.serializers import ModelSerializer

from market.models import Category, Subcategory, Announcement

class CategoryListSerializer(ModelSerializer):
    def create(self, validated_data):
        category =  Category(**validated_data)
        category.save()

        return category

    class Meta:
        model = Category
        fields = '__all__'

class SubcategoryListSerializer(ModelSerializer):
    def create(self, validated_data):
        cat_relate = validated_data.pop('category_related',[])
        subcategory = Subcategory(**validated_data)
        subcategory.save()

        subcategory.category_relate.set(cat_relate)

        return subcategory

    class Meta:
        model = Subcategory
        fields = '__all__'

class AnnouncementListSerializer(ModelSerializer):
    def create(self, validated_data):
        announce =  Announcement(**validated_data)
        announce.save()

        return announce

    class Meta:
        model = Announcement
        fields = '__all__'