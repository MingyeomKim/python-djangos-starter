from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
import random

# Create your views here.
def index(request):
    template = loader.get_template('first/index.html')
    now = datetime.now() #현재시간을 변수에 담는다.
    context = {
        'current_date': now
    } #삽입할 데이터를 집어넣는 곳
    return render(request, 'first/index.html', context)

def select(request):
    context = {'number': 4}
    return render(request, 'first/select.html', context)

def result(request):
    chosen = int(request.GET['number'])
    list = []
    if chosen >= 1 and chosen <= 45:
        list.append(chosen)
    box = []
    for i in range(0, 46):
        if chosen != i+1:
            box.append(i)
    random.shuffle(box)

    while len(list) < 6:
        list.append(box.pop())
    context = {
        'numbers' : list
    }
    return render(request, 'first/result.html', context)

def sum(request):
    numbers = [1,2,3,4,5]
    sum = 0
    for num in numbers:
        sum += num
    context = {'numbers':numbers, 'sum': sum}
    return render(request, 'first/sum.html', context)