from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    now = datetime.now() #현재시간을 변수에 담는다.
    context = {
        'current_date': now
    } #삽입할 데이터를 집어넣는 곳
    return render(request, 'index.html', context)

def select(request):
    context = {'number': 4}
    return render(request, 'select.html', context)

def result(request):
    context = {'numbers':[1,2,3,4,5,6]}
    return render(request, 'result.html', context)