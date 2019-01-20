from django.urls import path, include
from .views import index, create

app_name = 'board'

urlpatterns = [
    path('create/', create, name="create"),
    path('', index, name="index")
]
