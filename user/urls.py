from django.conf.urls import url
from . import views

app_name = 'user' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    url('register/', views.user_register, name='user_register')
]