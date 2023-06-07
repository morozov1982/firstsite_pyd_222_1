from django.urls import path

from testapp.views import AddSms, ReadSms

app_name = 'testapp'

urlpatterns = [
    path('addsms/', AddSms.as_view(), name='add_sms'),
    path('readsms/<int:pk>/', ReadSms.as_view(), name='read_sms'),
]
