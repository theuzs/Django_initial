from django.urls import path
from . import views
app_name = 'website'
urlpatterns = [
    #GET /
    path('',views.index, name='index'),
]