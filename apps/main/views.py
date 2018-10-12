from django.views import generic
from apps.custom.mixins import TitleMixin


class HomeView(TitleMixin, generic.TemplateView):

    template_name = 'index.html'
    page_title = "Home"
