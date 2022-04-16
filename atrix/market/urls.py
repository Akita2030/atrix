from django.urls import path
from .views import CategoryListAPIView, SubcategoryListAPIView, AnnouncementOrderedAPIView

app_name = 'market'

urlpatterns = [
    path('api/category/list', CategoryListAPIView.as_view(), name='api-category-list'),
    path('api/subcategory/list', SubcategoryListAPIView.as_view(), name='api-subcategory-list'),
    path('api/announce_order/list', AnnouncementOrderedAPIView.as_view(), name='api-announce_order-list')
]