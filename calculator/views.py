from django.shortcuts import render
from django.views.generic import TemplateView
from calculator.calcs import calorie_count

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = self.request.GET
        if self.request.GET:
            weight = int(items['weight'])
            age = int(items['age'])
            goal = items['goal']
            active = int(items['active'])
            if items['gender'] == 'M':
                gender = 1.1
            else:
                gender = .9
        else:
            weight = 1
            age = 1
            goal = "M"
            active = 1

        context['stuff'] = calorie_count(weight,goal,active, gender)

        return context
