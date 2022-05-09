from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns=[
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit-profile'),
    path('contact/<int:id>', views.contact, name='contact'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('review/<int:id>', views.review, name='review')
]