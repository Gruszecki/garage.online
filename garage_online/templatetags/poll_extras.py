from garage_online.choices import get_genres
from django import template

register = template.Library()


@register.inclusion_tag('results.html')
def genres():
    return {'genres': get_genres()}

# mydata = Members.objects.filter(firstname='Emil').values() | Members.objects.filter(firstname='Tobias').values()
# plus do tego jeszcze set
