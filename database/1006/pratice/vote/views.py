from django.shortcuts import render, redirect
from .models import Vote, Comment
from .forms import CommentForm, VoteForm

def index(request):
    votes = Vote.objects.all()
    context = {
        'votes': votes,
    }
    return render(request, 'vote/index.html', context)

def create(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            form.save()            
        return redirect('votes:index')
    form = VoteForm()
    context = {
        'form': form,
    }
    return render(request,'vote/create.html', context)

def detail(request,pk):
    vote = Vote.objects.get(pk=pk)
    comments = vote.comment_set.all()
    comments_form = CommentForm()
    left_cnt = 0
    right_cnt = 0
    for comment in comments:
        if comment.team == "왼쪽":
            left_cnt += 1
        else:
            right_cnt += 1
    if len(comments) != 0:
        left_percent = round(((left_cnt / len(comments)) * 100), 2)
        right_percent = round(((right_cnt / len(comments)) * 100), 2)
    else:
        left_percent = 0
        right_percent = 0
    context = {
        'vote': vote,
        'comments': comments,
        'comments_form': comments_form,
        'left': left_percent,
        'right': right_percent, 
    }
    return render(request,'vote/detail.html', context)

def comment_add(request,pk):
    comment_form = CommentForm(request.POST)
    vote = Vote.objects.get(pk=pk)
    comment = comment_form.save(commit=False)
    comment.question = vote
    comment.save()
    return redirect('votes:detail', pk)