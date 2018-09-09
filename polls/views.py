# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {latest_question_list: latest_question_list}
    render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
    return HttpResponse("You're looking at question %s" % question_id)

def results(request, question_id):
    response = "You're looking at the results for question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is helper to accecess submitted data by key name. IN this case we're grabbing the choice id from the form
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay question voting form.
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponse to make sure something returned from submit.
        # Otherwise if user hits back button the data can get posted twice
        


    return HttpResponse("You're voting on question %s" % question_id)
