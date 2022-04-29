from django.urls import path
from .views import get_subcategory, IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('getSubcategory/', get_subcategory, name = 'get_subcategory'),
]