from django.shortcuts import render
from django.views import View

from blog.models import Posts


# Create your views here.
class HomeView(View):
    def get(self, request):
        latest_question_list = Posts.objects.order_by('-create_at')[:5]
        context = {
            'latest_post_list': latest_question_list,
            'nav': 'home'
        }
        return render(request, 'homepage/index.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html', {
            'nav': 'about'
        })
