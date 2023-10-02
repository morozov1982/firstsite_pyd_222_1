from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from bboard.views import (index, BbCreateView, detail, BbByRubricView,
                          BbDetailView, rubrics, bbs, search, BbEditView)

vals = {
    'name': 'by_index',
    'beaver': 'beaver – это бобёр!'
}

# app_name = 'bboard'

# urlpatterns = [
#     re_path(r'^$', index, name='index'),
#     re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, vals, name='by_rubric'),
#     re_path(r'^add/$', BbCreateView.as_view(), name='add'),
# ]

urlpatterns = [
    path('', index, name='index'),
    path('rubrics/', rubrics, name='rubrics'),
    path('bbs/<int:rubric_id>/', bbs, name='bbs'),
    path('page/<int:page>/', index, name='page'),

    path('<int:rubric_id>/', cache_page(60 * 5)(BbByRubricView.as_view()), name='by_rubric'),

    path('<int:rubric_id>/page/<int:page>/', BbByRubricView.as_view(), name='rubric_page'),
    path('read/<int:rec_id>/', detail, name='read'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),

    path('search/', search, name='search'),
]
