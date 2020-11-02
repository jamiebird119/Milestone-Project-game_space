from django.urls import path
from . import views


urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_profile_photo/', views.add_profile_photo, name="add_profile_photo"),
]