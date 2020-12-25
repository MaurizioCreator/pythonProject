from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Main Page'),
    path('about', views.about, name='About'),
    path('create', views.create, name='Create'),
    path('<int:pk>', views.TaskDetailView.as_view(), name='Detail'),
    path('<int:pk>/edit', views.TaskEdit.as_view(), name='Edit'),
    path('<int:pk>/delete', views.TaskDelete.as_view(), name='Delete')
]
