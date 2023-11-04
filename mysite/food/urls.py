from . import views
from django.urls import path

app_name= 'food'
urlpatterns = [
    path('', views.index,name='index'),
    path('item/',views.item, name='item'),
    path('<int:pk>',views.Fooddetail.as_view(),name='detail'),
    # edit function
    path('add',views.create_item, name='create_item'),
# update function
    path('update/<int:id>',views.update_item,name='update_item' ),
]
#delete functionality
path('delete/<int:id'>,views.delete_item,name='delete_item')
