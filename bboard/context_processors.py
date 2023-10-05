from django.contrib.auth.models import User

from bboard.models import Rubric
from bboard.views import count_bb
from userapp.models import BbUser


def rubrics(request):
    return {
        'users': BbUser.objects.all(),
        'rubrics': Rubric.objects.all(),
        'count_bb': count_bb(),
    }
