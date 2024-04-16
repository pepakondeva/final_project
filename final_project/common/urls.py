from django.urls import path

from final_project.common.views import IndexView, authorized

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('not-authrorized/', authorized, name='not authorized')

)