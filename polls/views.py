from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_questions = Question.objects.order_by('id')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_questions': latest_questions
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
