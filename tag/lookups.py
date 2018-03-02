from ajax_select import register, LookupChannel

from userProfile_app.models import UserProfile
from .models import Tag


@register('tags')
class TagsLookup(LookupChannel):
    model = Tag

    def get_query(self, q, request):
        user = request.user  # type: UserProfile
        tags = [a.uuid for a in user.selected_tag.all()]
        return self.model.objects.filter(name__icontains=q).exclude(uuid__in=tags)

    def format_item_display(self, item):
        return u"<li class='list-group-item active'>%s</span>" % item.name

    def check_auth(self, request):
        pass
