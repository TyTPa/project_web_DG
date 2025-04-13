from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name ='home'),
    path('data/',views.data, name = 'data'),
    path ('test/',views.test, name = 'test'),
    path ('new/',views.new, name ='page2')
]