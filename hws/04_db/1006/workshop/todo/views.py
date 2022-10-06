from django.shortcuts import render, redirect
from todo.forms import TodoForm

def todos(request):
    if request.user.is_authenticated:
        author = request.user
        todos = author.todo_set.all()
        context = {
            'todos': todos,
        }
        return render(request, 'todo/todos.html', context)
    return redirect('accounts:login')

def todos_new(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            todo_form = TodoForm(request.POST)
            todo = todo_form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:todos')
        else:
            form = TodoForm()
            context = {
                'form': form,
            }
            return render(request, 'todo/new.html', context)
    else:    
        return redirect('accounts:login')
