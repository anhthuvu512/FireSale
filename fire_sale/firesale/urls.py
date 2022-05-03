from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="sale-index"),
    path('<int:id>', views.get_item_by_id, name="item-details"),
    path('create_item', views.create_item, name="create_item")
]