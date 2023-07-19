from django.urls import path, re_path

from bboard.views import index, by_rubric, BbCreateView, \
    add_save, add, add_and_save, detail, BbByRubricView, BbDetailView, BbAddView

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
    path('page/<int:page>/', index, name='page'),
    # path('<int:rubric_id>/', by_rubric, vals, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('<int:rubric_id>/page/<int:page>/', BbByRubricView.as_view(), name='rubric_page'),
    # path('add/', BbCreateView.as_view(), name='add'),
    # path('add/save/', add_save, name='add_save'),
    # path('add/', add, name='add'),
    # path('add/', add_and_save, name='add'),
    path('read/<int:rec_id>/', detail, name='read'),
    # path('add/', BbCreateView.as_view(), name='add'),
    path('add/', BbAddView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
]
