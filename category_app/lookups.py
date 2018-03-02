from ajax_select import register, LookupChannel
from .models import Category


@register('categories')
class CategoriesLookup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        categories_selected_already = [a.uuid for a in request.user.selected_category.all()]
        return self.model.objects.filter(name__icontains=q).exclude(uuid__in=categories_selected_already)

    def format_item_display(self, item):
        return u"<li class='list-group-item active'>%s</span>" % item.name

    def check_auth(self, request):
        pass
