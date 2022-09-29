from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PostForm
from .models import GuessNumbers
# Create your views here.
def index(request):

    lottos = GuessNumbers.objects.all()

    return render(request, 'lotto/default.html', {'lottos': lottos})# {} == context-dict


def post(request):
    #request.method  ==  GET, POST 확인가능

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid(): # 유저가 입력한 내용에 문제가 없는지 확인하는 코드, 문제가 없으면 true를 리턴함

            lotto = form.save(commit=False)
    # true로하면 db에 저장, false 로 하면 db에는 저장하지 않음(중간저장)-> 중간저장하여 데이터를 후처리하여 저장할수 있음
            lotto.generate()
            return redirect('index')

    else:
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})



def hello(request):
    data = GuessNembers.objects.all()
    data = GuessNembers.objects.get(id=1)

    return HttpResponse("<h1 style='color:red;'>Hello, World!</h1>")


def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(id=lottokey)

    return render(request, 'lotto/detail.html', {'lotto' : lotto})



    
