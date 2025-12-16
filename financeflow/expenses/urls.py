from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # homepage
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('categories/', views.categories, name='categories'),
]