from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
from . import api_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='authentication/login.html',
        authentication_form=LoginForm,
        redirect_authenticated_user=True
    ), name="login_view"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout_view'),
    path('device/init/', api_views.InitiateDeviceLoginView.as_view(), name='device_init_view'),
    path('device/poll/', api_views.PollDeviceLoginView.as_view(), name='device_poll_view'),
    path('device/<uuid:device_code>/', views.ApproveDeviceLoginView.as_view(), name='device_check_view')
]
