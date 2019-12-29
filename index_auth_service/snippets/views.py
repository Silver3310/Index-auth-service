from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView

from django.utils.translation import ugettext_lazy as _

from .models import Snippet
from .search import SnippetSearchForm


class SnippetDetailView(LoginRequiredMixin, DetailView):
    """
    Show the snippet's info
    """

    model = Snippet


snippet_detail_view = SnippetDetailView.as_view()


class SnippetUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update a snippet and redirect to the detail page
    """

    model = Snippet
    fields = [
        "desc",
        "code",
        "is_visible"
    ]
    template_name_suffix = '_update_form'

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO,
            _("Infos successfully updated")
        )
        return super().form_valid(form)


snippet_update_view = SnippetUpdateView.as_view()


class SnippetListView(LoginRequiredMixin, ListView):
    """
    List all code snippets
    """

    model = Snippet
    paginate_by = 10

    def get_queryset(self):
        """
        Don't show the snippets that are hidden and don't belong to a user and
        sort the snippet so the first snippets belong to a user
        """
        return self.model._default_manager.get_snippets(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search_form'] = SnippetSearchForm(
            desc=self.request.GET.get('desc'),
            username=self.request.GET.get('username')
        )
        return context


snippet_list_view = SnippetListView.as_view()


class SnippetCreateView(LoginRequiredMixin, CreateView):
    """
    Create a snippet and redirect to the detail page
    """
    model = Snippet
    fields = [
        "desc",
        "code",
        "is_visible"
    ]

    def form_valid(self, form):
        """Add user to the form"""
        snippet = Snippet.objects.create(
            user_id=self.request.user.pk,  # fix for elasticsearch
            desc=form.cleaned_data['desc'],
            code=form.cleaned_data['code'],
            is_visible=form.cleaned_data['is_visible']
        )

        messages.add_message(
            self.request, messages.INFO,
            _("A snippet successfully created")
        )
        return HttpResponseRedirect(snippet.get_absolute_url())


snippet_create_view = SnippetCreateView.as_view()


class SnippetDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a snippet and redirect to the list page
    """
    model = Snippet
    success_url = reverse_lazy('snippets:snippets')


snippet_delete_view = SnippetDeleteView.as_view()
