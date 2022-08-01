from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Account


def index(request):
    return render(request, 'finance/index.html', {})


def acounts(request):
    accounts = Account.objects.all()
    return JsonResponse({'foo': 'bar'})
