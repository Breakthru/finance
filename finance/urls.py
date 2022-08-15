from django.urls import path

from . import views

urlpatterns = [
    # single page app
    path('', views.index, name='index'),
    # APIs
    # list accounts
    path('accounts', views.accounts, name='accounts'),
    # fetch account object
    path('accounts/<int:account_id>/', views.account_view, name='account_view'),
    # upload statement
    path('upload', views.upload, name='upload'),
]