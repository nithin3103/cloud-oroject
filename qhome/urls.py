from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:myid>/", views.quiz, name="quiz"),
    path("sub/<int:sid>/", views.SubmitAttempt, name="sub"),

    path('admin_view/', views.admin_view, name='admin_view'),
    path('add_quiz/', views.add_quiz, name='add_quiz'),
    path('add_question/', views.add_question, name='add_question'),
    path('choose_question/', views.choose_question, name='choose_question'),
    path('add_options/<int:myid>/', views.add_options, name='add_options'),
    path('delete_question/<int:myid>/', views.delete_question, name='delete_question'),
]