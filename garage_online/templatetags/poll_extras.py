from django import template
from garage_online.models import GlobalColorSet
from garage_online.choices import get_default_colors

register = template.Library()


@register.inclusion_tag('global_colors.html', takes_context=True)
def get_global_colors(context):
    if context.request.user.is_authenticated:
        global_colors = GlobalColorSet.objects.filter(user=context.request.user)
        if global_colors:
            pass
        else:
            global_colors = get_default_colors()
    else:
        global_colors = get_default_colors()

    return {'global_colors': global_colors}

