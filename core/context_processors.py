from django.conf import settings
from django.db.models import Count, Q
from datetime import datetime, timedelta

from mandob.models import Section


def global_context(request):
    section = int(request.COOKIES.get('section', 0))
    sections = Section.objects.all()
    context = {
        'sections': sections,
        'section': section,
    }

    return context