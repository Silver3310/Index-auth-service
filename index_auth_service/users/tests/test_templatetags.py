import pytest

from django.test import RequestFactory
from django.contrib.auth import get_user_model
from django.template import Context
from django.template import Template
from django.urls import reverse

User = get_user_model()


class TestCommonTemplateTag:
    """Check common template tags"""

    def test_nav_bar_account_login(
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

    def test_nav_bar_account_signup(
        self,
        request_factory: RequestFactory
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse('account_signup')
        request = request_factory.get(url_to_check)
        context = Context()
        context['request'] = request

        template_to_render = Template(
            '{% load common %}'
            '{% nav_bar %}'
        )
        rendered_template = template_to_render.render(context)

        assert f'<a class="active item" href="{url_to_check}">Sign Up</a>' \
               in rendered_template

    def test_nav_bar_account_logout(
        self,
        request_factory: RequestFactory,
        user_to_login_username: str,
        client
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse('account_logout')
        response = client.get(url_to_check)

        assert bytes(
            f'<a class="active item" href="{url_to_check}">',
            encoding='utf-8'
        ) in response.content

    def test_nav_bar_friends(
        self,
        request_factory: RequestFactory,
        user_to_login_username: str,
        client
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse('friends:friends')
        response = client.get(url_to_check)

        assert bytes(
            f'<a class="active item" href="{url_to_check}">',
            encoding='utf-8'
        ) in response.content

    def test_nav_bar_list(
        self,
        request_factory: RequestFactory,
        user_to_login_username: str,
        client
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse('users:list')
        response = client.get(url_to_check)

        assert bytes(
            f'<a class="active item" href="{url_to_check}">',
            encoding='utf-8'
        ) in response.content

    def test_nav_bar_detail(
        self,
        request_factory: RequestFactory,
        user_to_login_username: str,
        client
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse(
            'users:detail',
            kwargs={
                'username': user_to_login_username
            }
        )
        response = client.get(url_to_check)

        assert bytes(
            f'<a class="active item" href="{url_to_check}">My Profile</a>',
            encoding='utf-8'
        ) in response.content

    def test_nav_bar_about(
        self,
        request_factory: RequestFactory
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse('about')
        request = request_factory.get(url_to_check)
        context = Context()
        context['request'] = request

        template_to_render = Template(
            '{% load common %}'
            '{% nav_bar %}'
        )
        rendered_template = template_to_render.render(context)

        assert f'<a class="active item" href="{url_to_check}">About</a>' \
               in rendered_template

    def test_nav_bar_home(
        self,
        request_factory: RequestFactory
    ):
        """
        Test if the navigation bar template tag correctly identifies an
        active tag
        """
        url_to_check = reverse('home')
        request = request_factory.get(url_to_check)
        context = Context()
        context['request'] = request

        template_to_render = Template(
            '{% load common %}'
            '{% nav_bar %}'
        )
        rendered_template = template_to_render.render(context)

        assert f'<a class="active item" href="{url_to_check}">Home</a>' \
               in rendered_template
