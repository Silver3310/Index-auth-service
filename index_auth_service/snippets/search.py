from django.shortcuts import render
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.core.paginator import Paginator
from django.utils.functional import LazyObject

from .documents import SnippetDocument
from .forms import SnippetSearchForm


class SearchResults(LazyObject):
    """Get search results"""
    def __init__(self, search_object):
        self._wrapped = search_object

    def __len__(self):
        return self._wrapped.count()

    def __getitem__(self, index):
        search_results = self._wrapped[index]
        if isinstance(index, slice):
            search_results = list(search_results)
        return search_results


def snippet_search(request):
    """
    Search for snippets using elasticsearch

    Search is done by fields:
        desc - description of snippets
        username - a snippet owner's name

    the following search shows only visible snippets
    """

    if request.method == "GET":
        desc = request.GET.get('desc')
        username = request.GET.get('username')
        paginate_by = 10

        object_list = SnippetDocument.search()
        if username:
            object_list = object_list.query(
                "match",
                user__username=username,
            )
        if desc:
            object_list = object_list.query(
                "match",
                desc=desc,
            )

        object_list = object_list.query(
            "match",
            is_visible="true",
        )

        search_results = SearchResults(object_list)

        paginator = Paginator(search_results, paginate_by)
        page_number = request.GET.get("page")
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            # If page parameter is not an integer, show first page.
            page = paginator.page(1)
        except EmptyPage:
            # If page parameter is out of range, show last existing page.
            page = paginator.page(paginator.num_pages)

        return render(
            request,
            'snippets/snippet_list.html',
            {
                'object_list': page.object_list,
                'search_form': SnippetSearchForm(
                    desc=desc,
                    username=username
                ),
                'page_obj': page,
                'is_paginated': True
            }
        )
