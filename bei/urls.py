from django.urls import path
from .import views

urlpatterns = [
    path('', views.index ),
    path('about/', views.about ),
    path('contact/', views.contact ),
    path('department/', views.department ),
    path('examination/', views.examination ),
    path('admission/', views.admission ),
    path('login/', views.login_user ),
    path('logout/', views.logout_user ),
    path('signup/', views.sign_up_user ),

]
