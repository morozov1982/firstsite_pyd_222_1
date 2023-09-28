from django.urls import path

from testapp.views import AddSms, ReadSms, add, edit, index, get, test_cookie, test_mail

app_name = 'testapp'

urlpatterns = [
    path('addsms/', AddSms.as_view(), name='add_sms'),
    path('readsms/<int:pk>/', ReadSms.as_view(), name='read_sms'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('', index, name='index'),
    path('get/<path:filename>/', get, name='get'),
    path('cookie/', test_cookie, name='test_cookie'),

    path('mail/', test_mail, name='test_mail'),
]
