from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context["request"].GET.copy()
    for arg, value in kwargs.items():
        query[arg] = value
    return query.urlencode()
