from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from home.filters import user_filter
from ..forms import *
from home.generics import filter_view_generic
from user.models import User


@method_decorator(login_required(), name="dispatch")
class create_user(CreateView):
    model = User
    template_name = "create_user.html"
    success_url = "/list_user"
    form_class = user_form


@method_decorator(login_required(), name="dispatch")
class list_user(filter_view_generic):
    queryset = User.objects.all().order_by('-id')
    model = User
    template_name = "list_user.html"
    paginate_by = 25
    filterset_class = user_filter
    context_object_name = "objects"


@method_decorator(login_required(), name="dispatch")
class update_user(UpdateView):
    model = User
    template_name = "update_user.html"
    success_url = "/list_user"
    form_class = user_form_update


@method_decorator(login_required(), name="dispatch")
class delete_user(DeleteView):
    model = User
    template_name = "delete.html"
    success_url = "/list_user"
