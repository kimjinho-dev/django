from django.shortcuts import render

def prices(request,thing,cnt):
    product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}
    if thing in product_price:
        data = product_price[thing] * cnt
    else:
        data = 'None'

    context = {
        'data' : data,
        'thing' : thing,
        'cnt' : cnt,
    }
    return render(request, 'prices.html', context)
# Create your views here.
