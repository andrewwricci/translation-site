from django.urls import path

from . import views

app_name = "translations"

urlpatterns = [
    path("", views.index, name="index"),
    path("<uuid:original_text_id>/", views.detail, name="detail"),
    # path("<int:original_text_id>/results/", views.results, name="results"),
]
