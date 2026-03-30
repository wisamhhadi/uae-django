from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from home.filters import captain_filter
from home.forms import *
from home.generics import filter_view_generic


@method_decorator(login_required(), name="dispatch")
class create_captain(CreateView):
    model = Captain
    template_name = "create_captain.html"
    success_url = "/list_captain"
    form_class = captain_form


@method_decorator(login_required(), name="dispatch")
class list_captain(filter_view_generic):
    queryset = Captain.objects.all().order_by('-id')
    model = Captain
    template_name = "list_captain.html"
    paginate_by = 25
    filterset_class = captain_filter
    context_object_name = "objects"


@method_decorator(login_required(), name="dispatch")
class update_captain(UpdateView):
    model = Captain
    template_name = "update_captain.html"
    success_url = "/list_captain"
    form_class = captain_form_update


@method_decorator(login_required(), name="dispatch")
class delete_captain(DeleteView):
    model = Captain
    template_name = "delete.html"
    success_url = "/list_captain"
