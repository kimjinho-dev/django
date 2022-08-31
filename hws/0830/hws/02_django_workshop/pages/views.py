from urllib import request
from django.shortcuts import render
import random
# Create your views here.
def lotto(request):
    lotto_num = random.sample(range(1,46),6)
    context = {
        'lotto_num' : lotto_num,
    }
    return render(request, 'lotto.html', context)