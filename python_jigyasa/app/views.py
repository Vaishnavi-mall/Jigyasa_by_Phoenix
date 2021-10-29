from django.shortcuts import render
# Create your views here.
from django.views import View


class LandingPageView(View):
    template_name = 'dev/landing_page.html'

    def get(self, request):
        return render(request, self.template_name)
