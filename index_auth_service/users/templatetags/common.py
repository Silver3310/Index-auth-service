from django import template
from django.urls import resolve

register = template.Library()


@register.inclusion_tag(
    'nav_bar.html',
    takes_context=True
)
def nav_bar(context):
    """
    Define an active tab for the navigation bar
    """

    home_active = ''
    about_active = ''
    detail_active = ''
    logout_active = ''
    signup_active = ''
    login_active = ''

    request = context['request']
    url_name = resolve(request.path_info).url_name

    if url_name == 'home':
        home_active = 'active'
    elif url_name == 'about':
        about_active = 'active'
    elif url_name == 'detail':
        detail_active = 'active'
    elif url_name == 'account_logout':
        logout_active = 'active'
    elif url_name == 'account_signup':
        signup_active = 'active'
    elif url_name == 'account_login':
        login_active = 'active'

    return {
        'request': request,
        'home_active': home_active,
        'about_active': about_active,
        'detail_active': detail_active,
        'logout_active': logout_active,
        'signup_active': signup_active,
        'login_active': login_active,
    }
