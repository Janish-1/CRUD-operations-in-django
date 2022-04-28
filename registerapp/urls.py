from unicodedata import name
from django.urls import path
from registerapp import views

urlpatterns=[
    # name is to access the database and register/ is to access the code in html view and views.register is to access the function
    path('register/',views.register,name='register'),
    path('search/',views.search,name='search'),
    path('update/',views.update,name='update'),
    path('index/',views.index,name="index"), # Static Format Implementation 
]
