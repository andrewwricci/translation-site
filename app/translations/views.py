from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Original_Text

from .forms import OriginalTextExistingUserForm


def index(request):
    original_text_form = OriginalTextExistingUserForm

    # allow users to change the status of original text while in 受付待ち or 下書き state
    original_text_list = Original_Text.objects.filter(user_id=request.user)
    latest_original_text_list = original_text_list.order_by("-last_updated_datetime")
    paginator = Paginator(latest_original_text_list, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'original_text_form': original_text_form, 
        'latest_original_text_list': latest_original_text_list,
        "page_obj": page_obj
        }
    return render(request, "translations/index.html", context)

class OriginalTextDetail(LoginRequiredMixin, DetailView):
    model = Original_Text

    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(user_id=self.request.user)

class OriginalTextCreate(LoginRequiredMixin, CreateView):
    form_class = OriginalTextExistingUserForm
    success_url = reverse_lazy("translations:index")

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(CreateView, self).form_valid(form)
    
class OriginalTextDelete(LoginRequiredMixin, DeleteView):
    model = Original_Text
    success_url = reverse_lazy("translations:index")

# ステータスが下書き・対応待ちでない時にUpdateできないようにする
class OriginalTextUpdate(LoginRequiredMixin, UpdateView):
    model = Original_Text
    form_class = OriginalTextExistingUserForm
    template_name_suffix = '_update_form'

    def get_success_url(self, **kwargs):
         return reverse_lazy("translations:original-text-detail", kwargs={'pk': self.kwargs['pk']})

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.kwargs = kwargs
        self.object = self.get_object()
        if not self.object.is_status_editable():
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(user_id=self.request.user)
        
    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(UpdateView, self).form_valid(form) 
