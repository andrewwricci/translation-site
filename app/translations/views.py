from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models.base import Model as Model
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Original, EditableStatus

from .forms import OriginalExistingUserForm

def set_status(self):
    if 'save_as_draft' in self.request.POST:
        return EditableStatus.DRAFT
    elif 'request_translation' in self.request.POST:
        return EditableStatus.WAITING_FOR_ACTION
    
class OriginalListView(LoginRequiredMixin, ListView):
    paginate_by = 5
    model = Original
    template_name="translations/index.html"

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user).order_by("-last_updated_datetime")
    
    def get_context_data(self, **kwargs):
        context = super(OriginalListView, self).get_context_data(**kwargs)
        context['editable_status'] = EditableStatus
        return context

class OriginalDetailView(LoginRequiredMixin, DetailView):
    model = Original

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)

class OriginalCreateView(LoginRequiredMixin, CreateView):
    model = Original
    form_class = OriginalExistingUserForm
    success_url = reverse_lazy("translations:index")

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        form.instance.status = set_status(self)
        return super(CreateView, self).form_valid(form)
    
class OriginalDeleteView(LoginRequiredMixin, DeleteView):
    model = Original
    success_url = reverse_lazy("translations:index")

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)

class OriginalUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Original
    fields = []
    success_url = reverse_lazy("translations:index")

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)

    def form_valid(self, form):
        form.instance.status = set_status(self)
        return super(UpdateView, self).form_valid(form)

class OriginalUpdateView(LoginRequiredMixin, UpdateView):
    model = Original
    form_class = OriginalExistingUserForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy("translations:index")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.is_status_editable():
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(user_id=self.request.user)
        
    def form_valid(self, form):
        form.instance.status = set_status(self)
        return super(UpdateView, self).form_valid(form) 
