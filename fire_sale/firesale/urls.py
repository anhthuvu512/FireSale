from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="sale-index"),
    path('<int:id>', views.item_details, name="item-details"),
    path('create_item', views.create_item, name="create-item"),
    path('delete_item/<int:id>', views.delete_item, name='delete-item'),
    path('update_item/<int:id>', views.update_item, name='update-item'),
    path('unavailable_item/<int:id>', views.unavailable_item, name='unavailable-item'),
    path('<int:id>/add_image', views.add_image, name='add-image'),
    path('sort_item', views.sort_item, name="sort-item"),
    path('make_offer/<int:id>', views.make_offer, name="make-offer"),
    path('notification/<int:id>', views.seller_notif_detail, name="notification"),
    path('decline_offer/<int:id>', views.decline_offer, name='decline-offer'),
    path('accept_offer/<int:id>', views.accept_offer, name='accept-offer')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)