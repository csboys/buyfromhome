from django.conf.urls import url

from . import views

app_name = 'form'
urlpatterns = [
    url('', views.feedback_form, name='home'),
]