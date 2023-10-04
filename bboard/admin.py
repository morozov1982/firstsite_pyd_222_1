from django.contrib import admin
from bboard.models import Bb, Rubric


# def title_and_rubric(rec):
#     return f'{rec.title} ({rec.rubric.name})'
#
#
# title_and_rubric.short_description = 'Название и рубрикасы'


class PriceListFilter(admin.SimpleListFilter):
    title = 'Кактегория цен'
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('low', 'Низкая цена'),
            ('medium', 'Средняя цена'),
            ('high', 'Высокая цена'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(price__lt=500)
        if self.value() == 'medium':
            return queryset.filter(price__gte=500, price__lte=5000)
        if self.value() == 'high':
            return queryset.filter(price__gt=5000)


@admin.register(Rubric)
class RubricAdmin(admin.ModelAdmin):
    search_fields = ('name',)


class BbAdmin(admin.ModelAdmin):
    list_display = ('title_and_rubric', 'title', 'content', 'price', 'rubric', 'published')
    # list_display = ('id', title_and_rubric, 'title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    # list_display_links = None
    list_editable = ('price', 'rubric')
    search_fields = ('title', 'content')
    # search_fields = ('^content',)
    # search_fields = ('=content',)

    # ordering = ('title',)
    sortable_by = ('title', 'rubric', 'published')

    list_filter = (PriceListFilter,)

    list_per_page = 10
    list_max_show_all = 15

    # actions_on_bottom = True

    # fields = (('title', 'price'), 'content')
    # fields = ('title', 'content', 'price', 'published')
    # exclude = ('rubric', 'kind')
    # readonly_fields = ('published',)

    # fieldsets = (
    #     (None, {
    #         'fields': (('title', 'rubric'), 'content'),
    #         'classes': ('wide',),  # ('collapse',)
    #     }),
    #     ('Дополнительные сведения', {
    #         'fields': ('price',),
    #         'description': 'Параметры, необязательные для указания',
    #     })
    # )

    radio_fields = {'kind': admin.HORIZONTAL}

    autocomplete_fields = ('rubric',)

    save_as = True
    # save_on_top = True

    def title_and_rubric(self, rec):
        return f'{rec.title} ({rec.rubric.name})'

    # def get_list_display(self, request):
    #     ld = ['title', 'content', 'price']
    #     if request.user.is_superuser:
    #         ld += ['published', 'rubric']
    #     return ld

    def get_list_display_links(self, request, list_display):
        # return list_display
        return 'title', 'content'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_hidden=False)

    title_and_rubric.short_description = 'Название и рубрика'


# admin.site.register(Rubric, RubricAdmin)
admin.site.register(Bb, BbAdmin)
