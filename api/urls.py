from django.urls import path, include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_auth.registration.views import VerifyEmailView, RegisterView

app_name = 'api'

urlpatterns = [
    path('profile/', ProfileViewList.as_view()),
    path('profile/<int:pk>/', ProfileViewDetail.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/signup/', RegistrationView.as_view()),
 #   path('rest-auth/registration/', include('rest_auth.registration.urls')),
 #   path('account-confirm-email/', VerifyEmailView.as_view(),
 #    name='account_email_verification_sent'),
  #  path('account-confirm-email/(?P<key>[-:\w]+)/', VerifyEmailView.as_view(),
  #   name='account_confirm_email'),
]
urlpatterns = format_suffix_patterns(urlpatterns)