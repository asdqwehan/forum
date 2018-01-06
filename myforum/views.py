from django.shortcuts import render
from myforum.models import Bbs, Comments, Category
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from myforum.forms import CommentsForm, BbsForm

# Create your views here.
def index(request):
    bbs_list = Bbs.objects.all()
    categories = Category.objects.all()
    context = {'bbs_list': bbs_list, 'categories': categories}
    return render(request, 'myforums/base.html', context)

def bbs_detail(request, bbs_id):
    bbs = Bbs.objects.get(id=bbs_id)
    comments = bbs.comments_set.all()
    context = {'bbs': bbs, 'comments':comments}
    return render(request, 'myforums/detail.html', context)

def comments(request, bbs_id):
    bbs = Bbs.objects.get(id=bbs_id)
    if request.method != 'POST':
        form = CommentsForm()
    else:
        form = CommentsForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.topic = bbs

            new_comment.author = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('myforum:detail', args=[bbs.id]))
    context = {'bbs': bbs, 'form': form}
    return render(request, 'myforums/comments.html', context)

def new_bbs(request):
    if request.method != 'POST':
        form = BbsForm()
    else:
        form = BbsForm(data=request.POST)
        if form.is_valid():
            new_bbs = form.save(commit=False)
            new_bbs.author = request.user
            new_bbs.save()
            return HttpResponseRedirect(reverse('myforum:index'))
    context = {'form': form}
    return render(request, 'myforums/new_bbs.html', context)

def edit_bbs(request, bbs_id):
    bbs = Bbs.objects.get(id=bbs_id)
    if request.method != 'POST':
        form = BbsForm(instance=bbs)
    else:
        form = BbsForm(instance=bbs, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myforum:detail', args=[bbs.id]))
    context = {'form': form, 'bbs': bbs}
    return render(request, 'myforums/edit_bbs.html', context)

def category(request, cate_id):
    cate_id = cate_id
    bbs_list = Bbs.objects.filter(category__id=cate_id)#找出板块下的bbs内容
    categories = Category.objects.all()
    context = {'bbs_list': bbs_list, 'categories': categories, 'cate_id': int(cate_id)}
    return render(request, 'myforums/base.html', context)