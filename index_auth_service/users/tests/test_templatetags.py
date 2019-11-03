from django.test import RequestFactory
from django.template import Context
from django.template import Template
from django.urls import reverse


class TestCommonTemplateTag:
    """Check common template tags"""

    def test_nav_bar(
        self,
        request_factory: RequestFactory
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse('account_login')
        request = request_factory.get(url_to_check)
        context = Context()
        context['request'] = request

        template_to_render = Template(
            '{% load common %}'
            '{% nav_bar %}'
        )
        rendered_template = template_to_render.render(context)

        assert f'<a class="active item" href="{url_to_check}">Sign In</a>' \
               in rendered_template
