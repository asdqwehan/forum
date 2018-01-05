from django.shortcuts import render
from myforum.models import Bbs, Comments
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from myforum.forms import CommentsForm

# Create your views here.
def index(request):
    bbs_list = Bbs.objects.all()
    context = {'bbs_list': bbs_list}
    return render(request, 'myforums/index.html', context)

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