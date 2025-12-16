from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Expense, Category
from datetime import datetime
from django.db.models import Sum

# Create your views here.
@login_required
def add_expense(request):
    if request.method == "POST":
        amount= request.POST.get("amount")
        category= request.POST.get("category")
        date= request.POST.get("date")
        description= request.POST.get("description")
        user= request.user
        
        expense = Expense(
            amount=amount,
            category=category,
            date=date,
            description=description,
            user=request.user 
        )
        expense.save()

        return redirect("expense_list")
        

    return render(request, "add_expense.html")

@login_required
def expense_list(request):
    expenses= Expense.objects.filter(user= request.user).order_by('-date')
    context={
        "expenses": expenses
    }
    return render(request, "expense_list.html", context)

@login_required
def categories(request):
    return render(request, "categories.html")  

def login_view(request):
    if request.method == "POST":
        username= request.POST["username"]
        password= request.POST["password"]    
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return HttpResponse("Ensure password and username are correct")
    return render(request, "login.html")  

@login_required
def dashboard(request):
    user_expenses = Expense.objects.filter(user=request.user)
    today = datetime.today().date()      
    current_month = datetime.today().month  
    current_year = datetime.today().year 
    
    monthly_total = user_expenses.filter(
        date__month=current_month,
        date__year=current_year  
    ).aggregate(total=Sum('amount'))['total'] or 0  
    
    today_total = user_expenses.filter(date=today).aggregate(total=Sum('amount'))['total'] or 0 
    
    recent_expenses = user_expenses.order_by('-date')[:5]  
    
    return render(request, 'dashboard.html', {
        'monthly_total': monthly_total,
        'today_total': today_total,
        'recent_expenses': recent_expenses 
    })  

@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


    
