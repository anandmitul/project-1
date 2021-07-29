from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("wiki/<title>",views.entry, name="post"),
    path("new_page",views.new_page,name="new"),
    path("search",views.search,name="search"),
    path("random",views.random,name="random"),
    path("edit/<title>",views.edit,name="edit")
    
   
]



