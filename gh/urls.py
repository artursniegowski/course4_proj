from gh import views
from django.urls import path

app_name = "gh"

urlpatterns = [
    path("", views.index, name="index-gh-view"),
]
