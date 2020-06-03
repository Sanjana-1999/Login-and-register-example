
from django.urls import path,include
from proapp import views

app_name='proapp'
urlpatterns = [
    path('',views.reg,name='register'),
    path('user_login/',views.user_login,name='user_login')
]
