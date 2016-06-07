from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active_if(context, view_name):
    if context.request.resolver_match.view_name == view_name:
        return 'active'
    return ''
