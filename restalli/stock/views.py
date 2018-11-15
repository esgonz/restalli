from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ProductoStock
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

class StaffRequiredMixin(object):
  def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)   

# Create your views here.
class PageListView(ListView):
    model = ProductoStock

class PageDetailView(DetailView):
    model = ProductoStock

class PageCreate(CreateView):
    model = ProductoStock
    fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

class PageUpdate(UpdateView):
    model = ProductoStock
    fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form' 

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDelete(DeleteView):
    model = ProductoStock
    success_url = reverse_lazy('pages:pages')
