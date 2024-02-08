from movies import views
from django.urls import path


urlpatterns = [
    path("search/", views.search, name="search"),
    path(
        "search-wait/<uuid:result_uuid>/", views.search_wait, name="search_wait"
    ),
    path("search-results/", views.search_results, name="search_results")
]
