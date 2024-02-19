from django.urls import path

from . import views

app_name = "translations"

urlpatterns = [
    path("", views.index, name="index"),
    path("original-text/<uuid:pk>/", views.OriginalTextDetail.as_view(), name="original-text-detail"),
    path("original-text/add", views.OriginalTextCreate.as_view(), name="original-text-add"),
    path("original-text/delete/<uuid:pk>/", views.OriginalTextDelete.as_view(), name="original-text-delete"),
    path("original-text/update/<uuid:pk>/", views.OriginalTextUpdate.as_view(), name="original-text-update")
]
