from django.shortcuts import render
from django.views import View


class Leadership(View):

    def get(self, request):
        context = {
            'heading': 'LEADERSHIP',
            'active': 'active',
        }
        return render(request, 'leadership/index.html', context)
