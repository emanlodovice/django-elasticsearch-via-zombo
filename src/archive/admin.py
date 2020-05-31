from django.contrib.admin import register, ModelAdmin
from .models import Archive, ArchiveZombo


@register(Archive)
class ArchiveAdmin(ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("content__icontains",)


@register(ArchiveZombo)
class ArchiveZomboAdmin(ModelAdmin):
    list_display = ("name", "user")
    search_fields = ("content__icontains",)

    def get_search_results(self, request, queryset, search_term):
        if search_term:
            queryset = queryset.query_string_search(f'"${search_term}"')
        return queryset, False
