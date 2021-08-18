from django.urls import path
from .views import IndexView, TesteView, Erro500

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste/', TesteView.as_view(), name='teste'),
    path('Erro500-url/', Erro500.as_view(), name='erro500')
]