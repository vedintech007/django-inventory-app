from django.urls import path
from .views import *

from user import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('register/', user_view.register, name="user-register"),
	path('profile/', user_view.profile, name="user-profile"),
	path('profile/update/', user_view.profile_update, name="user-profile-update"),

	# Login and logout url & view (class based views)
	path('', auth_views.LoginView.as_view(template_name="user/login.html"), name="user-login"),
	path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="user-logout"),

	# password reset views
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
	path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html') , name='password_reset_done'),
	path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

	# password change views
	path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user/password_change_form.html'), name='password_change'),
	path('password_change_done/', auth_views.PasswordChangeView.as_view(template_name='user/password_change_done.html'), name='password_change_done'),
]
