from django.urls import path
from .views.index import index
from .views.user import add_user, edit_user, remove_user

urlpatterns = [
    path('',index, name='index'),
    path('add-user/', add_user, name='add_user'),
    path('edit-user/<int:user_id>/', edit_user, name='edit_user'),
    path('remove-user/<int:user_id>/', remove_user, name='remove_user'),
]