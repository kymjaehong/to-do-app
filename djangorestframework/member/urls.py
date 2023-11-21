from django.urls import path
from member import views

urlpatterns = [path("", views.MemberAPIView.as_view())]
