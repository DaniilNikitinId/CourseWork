from django import template
import store.views as views
from store.models import TagPost

register = template.Library() #обьект для регистрации новых тегов


@register.inclusion_tag('store/list_tags.html')
def show_all_tegs():
    return {'tags': TagPost.objects.all()}