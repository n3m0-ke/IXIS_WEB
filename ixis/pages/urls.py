from django.urls import path
from . import views

urlpatterns = [
	path('signin/', views.signin_view, name='signin'),
	path('signup/', views.signup_view, name='signup'),
	path('Err404_view/', views.Err404_view, name='Err404_view'),
	path('Err500_view/', views.Err500_view, name='Err500_view'),
	path('origin/', views.origin_view, name='origin'),
	path('feed/', views.feed_view, name='feed'),
	path('profile1/', views.profile1_view, name='profile1'),
	path('profile3/', views.profile3_view, name='profile3'),
]