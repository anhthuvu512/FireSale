from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('firesale.urls')),
    path('admin/', admin.site.urls),
    path('sales/', include('firesale.urls')),
    path('user/', include('user.urls'))
]
