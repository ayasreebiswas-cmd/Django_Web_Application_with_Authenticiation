from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, TaskForm
from .models import Task, CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_custom_admin():
        tasks = Task.objects.select_related('assigned_to').all()
        users_count = CustomUser.objects.count()
        completed_count = Task.objects.filter(status='completed').count()
        context = {
            'tasks': tasks,
            'is_admin': True,
            'total_users': users_count,
            'total_tasks': tasks.count(),
            'completed_tasks': completed_count,
        }
    else:
        tasks = Task.objects.filter(assigned_to=request.user)
        context = {
            'tasks': tasks,
            'is_admin': False,
            'total_tasks': tasks.count(),
            'completed_tasks': tasks.filter(status='completed').count(),
        }
    return render(request, 'tasks/dashboard.html', context)

@login_required
def create_task(request):
    if not request.user.is_custom_admin():
        messages.error(request, "Access restricted to admins.")
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})