from math import ceil

from django.shortcuts import render
from .models import Core, Project
from .forms import PostForm, ProjectForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.urls import reverse, reverse_lazy

# Create your views here.

class CoreView(LoginRequiredMixin, ListView):
    template_name = 'core/Blog.html'
    model = Core
    context_object_name = 'post'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     model_post = Core.objects.all()
    #     n = len(model_post)
    #     nSlides = n // 3 + ceil((n / 3) - (n // 3))
    #     context['no_of_slides'] = nSlides
    #     context['range'] = range(1, nSlides)
    #     return context


class SingleView(LoginRequiredMixin, DetailView):
    model = Core
    template_name = 'core/Detailed-Blog.html'
    context_object_name = 'post'


class PostsView(LoginRequiredMixin, ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Core
    form_class = PostForm
    template_name = 'core/add_post.html'
    success_url = reverse_lazy('core:index')

class CoreUpdateView(LoginRequiredMixin, UpdateView):
    model = Core
    form_class = PostForm
    template_name = "core/add_post.html"
    success_url = reverse_lazy("core:posts")
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "post"
    permission_required = 'core.change_project'

    def __init__(self, **kwargs):
        return super(CoreUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CoreUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(CoreUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(CoreUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CoreUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(CoreUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(CoreUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(CoreUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(CoreUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(CoreUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(CoreUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(CoreUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        return super(CoreUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(CoreUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CoreUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CoreUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CoreUpdateView, self).get_template_names()

class CoreDeleteView(LoginRequiredMixin, DeleteView):
    model = Core
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "post"


    def __init__(self, **kwargs):
        return super(CoreDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(CoreDeleteView, self).dispatch(*args, **kwargs)
    #
    # def get(self, request, *args, **kwargs):
    #     raise Http404

    def post(self, request, *args, **kwargs):
        return super(CoreDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(CoreDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(CoreDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(CoreDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(CoreDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(CoreDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(CoreDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(CoreDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(CoreDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:posts")

#----------------------------------------------------------------------------------

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = "create.html"
    success_url = reverse_lazy("core:project-list")

#PermissionRequiredMixin
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'project_list.html'
    paginate_by = 50

    def get_queryset(self):
        base_queryset = self.model.objects.all()
        return base_queryset

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_detail.html'

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = "create.html"
    success_url = reverse_lazy("core:project-list")
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "project"
    # permission_required = 'lrp.change_project'

    def __init__(self, **kwargs):
        return super(ProjectUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ProjectUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ProjectUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ProjectUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ProjectUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ProjectUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ProjectUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ProjectUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ProjectUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ProjectUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ProjectUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ProjectUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        return super(ProjectUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ProjectUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ProjectUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ProjectUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ProjectUpdateView, self).get_template_names()

    # def get_success_url(self):
    #     return reverse("core:project-list", args=(self.object.pk,))

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "project_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy("core:project-list")
    pk_url_kwarg = 'pk'
    context_object_name = "project"
    # permission_required = 'lrp.delete_project'

    # @method_decorator(permission_required('proj.delete_proj'))

    def __init__(self, **kwargs):
        return super(ProjectDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ProjectDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ProjectDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ProjectDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ProjectDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ProjectDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ProjectDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ProjectDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ProjectDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ProjectDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("core:project-list")

