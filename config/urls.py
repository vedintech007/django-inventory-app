"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from user import views as user_view
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('dashboard.urls')),

	# User url paths
	path('register/', user_view.register, name="user-register"),
	path('profile/', user_view.profile, name="user-profile"),
	path('profile/update/', user_view.profile_update, name="user-profile-update"),

	# Login and logout url & view (class based views)
	path('', auth_views.LoginView.as_view(template_name="user/login.html"), name="user-login"),
	path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="user-logout"),

	# This will handle password reset feature (Do not change order, not a restriction tho)
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
	path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html') , name='password_reset_done'),
	path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
	path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]

handler404='dashboard.views.error_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
