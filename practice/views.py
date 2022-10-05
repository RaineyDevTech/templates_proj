import datetime

from django.views.generic import TemplateView

class FilterView(TemplateView):
    template_name = 'practice/filters.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = 'Webucator'
        context['url'] = 'https://www.webucator.com'
        context['moon_landing'] = datetime.datetime(
            year=1969, month=7, day=21,
            hour=2, minute=56, second=15,
            tzinfo=datetime.timezone.utc
        )

        return context

class HomePageView(TemplateView):
    template_name = 'home.html'

class TagView(TemplateView):
    template_name = 'practice/tags.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['beatles'] = [
            {'firstname': 'Paul', 'lastname': 'McCartney'},
            {'firstname': 'John', 'lastname': 'Lennon'},
            {'firstname': 'George', 'lastname': 'Harrison'},
            {'firstname': 'Ringo', 'lastname': 'Starr'},
        ]
        
        return context