from .views import dashboard, usersView, allowUserApplicationAccess, declineUserApplicationAccess
from django.urls import path

urlpatterns = [

    path("dashboard", dashboard, name='admin.dashboard'),
    path("users", usersView, name='admin.users_view'),
    path("allow-user-application-access", allowUserApplicationAccess, name='admin.allow_user_application_access'),
    path("decline-user-application-access", declineUserApplicationAccess, name='admin.decline_user_application_access'),

]