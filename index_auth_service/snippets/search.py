from django.shortcuts import render

from .documents import SnippetDocument
from .forms import SnippetSearchForm


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

        return render(
            request,
            'snippets/snippet_list.html',
            {
                'object_list': object_list,
                'search_form': SnippetSearchForm(
                    desc=desc,
                    username=username
                )
            }
        )
