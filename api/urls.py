from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('question1-list/', views.question1List, name="question1-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('question1-create/', views.question1Create, name="question1-create"),
	path('question2-list/', views.question2List, name="question2-list"),
	path('question2-create/', views.question2Create, name="question2-create"),
	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
