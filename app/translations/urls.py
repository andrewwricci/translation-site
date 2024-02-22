from django.urls import path

from . import views

app_name = "translations"

urlpatterns = [
    path("", views.OriginalListView.as_view(), name="index"),
    path("original/<uuid:pk>/", views.OriginalDetailView.as_view(), name="original-detail"),
    path("original/add", views.OriginalCreateView.as_view(), name="original-add"),
    path("original/delete/<uuid:pk>/", views.OriginalDeleteView.as_view(), name="original-delete"),
    path("original/update/<uuid:pk>/", views.OriginalUpdateView.as_view(), name="original-update"),
    path("original/update-status/<uuid:pk>/", views.OriginalUpdateStatusView.as_view(), name="original-update-status")
]
