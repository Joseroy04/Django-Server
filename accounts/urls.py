from django.urls import path
from .views import signin, signup, home, logout_view
# CustomSignupView, additional_info

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    # path('signup/custom/', CustomSignupView.as_view(), name='custom_signup'),
    # path('signup/additional/', additional_info, name='additional_info'),
]
