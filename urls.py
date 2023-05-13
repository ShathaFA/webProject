from django.urls import path 
from . import views

urlpatterns = [
    path('leaderboard', views.leaderboard,name='leaderboard'),
       path('redeem', views.redeem,name='redeem'),
       path('coupons/<int:pk>/redeem/', views.redeem_coupon, name='redeem_coupon'),
]