from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Account
from .forms import UploadFileForm


def index(request):
    return render(request, 'finance/index.html', {})


def accounts(request):
    accounts = list(Account.objects.all().values())
    return JsonResponse({'accounts': accounts})


def account_view(request, account_id):
    acc = get_object_or_404(Account, id=account_id)
    return JsonResponse({'name': acc.name, 'id': acc.id})


def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print([l for l in request.FILES['file']])
            return JsonResponse({'status': 'success'});
    else:
        # if a GET (or any other method) we'll create a blank form
        form = UploadFileForm()
    return render(request, 'finance/upload.html', {'form': form})
