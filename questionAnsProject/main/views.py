from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    questions = Question.objects.all().order_by('-id')
    paginator = Paginator(questions, 1)
    page_num = request.GET.get('page', 1)
    questions = paginator.page(page_num)
    return render(request, 'index.html', {'questions': questions})
