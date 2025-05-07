from django.urls import path, include
from core import views as core_views
from functions import views as functions_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('accounts/profile/', core_views.profile, name='accounts/profile/'),
    path('main/', core_views.main, name='main'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('form_bussiness/', functions_views.show_form, name='form'),
]
