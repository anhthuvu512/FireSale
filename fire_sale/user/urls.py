from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('contact/<int:id>', views.contact, name='contact'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('rate_seller/<int:id>', views.rate_seller, name='rate-seller'),
    path('review/<int:id>', views.review, name='review')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)