from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Account


def index(request):
    return render(request, 'finance/index.html', {})


def accounts(request):
    accounts = list(Account.objects.all().values())
    return JsonResponse({'accounts': accounts})


def account_view(request, account_id):
    acc = get_object_or_404(Account, id=account_id)
    return JsonResponse({'name': acc.name, 'id': acc.id})

def form_test(request):
    from django import forms
    class UploadFileForm(forms.Form):
        file = forms.FileField()

    form = UploadFileForm()
    context = {'form': form, 'account': get_object_or_404(Account, id=1)}
    return render(request, 'finance/upload.html', context)