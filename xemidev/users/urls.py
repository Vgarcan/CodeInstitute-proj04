from django.urls import path
from . import views
# from .views import CustomLoginView
app_name = 'users'

urlpatterns = [
    path('', views.home, name='home'),
    # path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
]
