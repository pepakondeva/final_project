from django.urls import path

from final_project.account.views import SignUpView, SignInView, LogoutViewAPI, UserEditView, UserDetailsView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('log-out/', LogoutViewAPI.as_view(), name='logout'),
    path('profile-edit/<int:pk>/', UserEditView.as_view(), name='profile-edit'),
    path('profile-details/<int:pk>/', UserDetailsView.as_view(), name='profile-details'),

)