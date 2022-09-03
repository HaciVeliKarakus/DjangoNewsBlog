from django.urls import path

from account.views import SignupForm

urlpatterns = [
    path('signup', SignupForm.as_view(), name='signup')
]
