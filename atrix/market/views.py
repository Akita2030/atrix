from django.shortcuts import render
from market.models import Category, Announcement, Subcategory

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from.serializers import CategoryListSerializer, SubcategoryListSerializer, AnnouncementListSerializer


class CategoryListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_classes = CategoryListSerializer

    def get(self, request):
        category = Category.objects.all()
        serializer = self.serializer_classes(category, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class SubcategoryListAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_classes = SubcategoryListSerializer

    def get(self, request):
        subcategories = Subcategory.objects.all()
        serializer = self.serializer_classes(subcategories, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

class AnnouncementOrderedAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_classes = AnnouncementListSerializer

    def get(self, request):
        announcement_order = Announcement.objects.all().order_by('created_at')
        serializer = self.serializer_classes(announcement_order, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

class AnnounceByCategoryAPIView(APIView):
    permission_classes = (AllowAny, )
    serializer_classes = AnnouncementListSerializer

    def get(self,request):
        category_pk = Category.objects.get(pk=id)
        announce_order = Announcement.objects.filter(categ_relate = category_pk)
        serializer = self.serializer_classes(announce_order, many=True)
        if announce_order:
            return Response(
                status=status.HTTP_200_OK,
                data={
                'success':True,
                'message':serializer.data
                })
        else:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    'success':False,
                    'announce':'Not found!'
                    })
