from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="sale-index"),
    path('<int:id>', views.get_item_by_id, name="item-details"),
    path('create_item', views.create_item, name="create-item"),
    path('delete_item/<int:id>', views.delete_item, name='delete-item'),
    path('update_item/<int:id>', views.update_item, name='update-item')
]