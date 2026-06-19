from django.urls import path
from . import views

urlpatterns = [
    path('createpost',views.InsertEdit),
    path('editpost/<int:pk>/',views.InsertEdit,name='editpost'),
    path('deletepost/<int:pk>/',views.DeletePost,name='deletepost'),
    path('allpost',views.AllPost,name="allpost"),
    path('viewpost/<int:pk>/',views.ViewPost,name="viewpost")
]
