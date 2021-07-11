from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('postnew/', views.postnew, name='postnew'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('postshow/<int:post_id>', views.postshow, name='postshow'),
    path('postshow/edit', views.edit, name="edit"),
    path('postshow/postupdate/<int:post_id>', views.postupdate, name='postupdate'),
    path('postshow/postdelete/<int:post_id>', views.postdelete, name='postdelete'),
]