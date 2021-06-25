from django.urls import path
from . import views

urlpatterns = [

    path('status',views.StatusList.as_view()),
    path('status/<int:pk>',views.StatusAct.as_view()),
    
    path('',views.TaskView.as_view({
            'get': 'list',
            'post': 'create',
        })),
    
    path('<int:pk>', views.TaskView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })),

    path('user/<int:pk>', views.TaskView.as_view({
            'get': 'get_all_task_user',
        }))
]