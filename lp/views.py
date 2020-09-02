from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import LeaveReply
from .forms import LeaveReplyForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.backends import *
from django.conf import settings
#from django.contrib import auth
#from django.contrib.auth.models import User




# Create your views here.



def index(request):
    if request.method == 'POST' and 'btnAddReply' in request.POST:
        leave_a_reply = LeaveReplyForm(request.POST)
        if leave_a_reply.is_valid():
            lar = leave_a_reply.save(commit =False)
            lar.date_posted = timezone.now()
            lar.save()

            return HttpResponseRedirect('/thanks')
    else:
        leave_a_reply = LeaveReplyForm()

    args = {}

    args['leave_a_reply'] = leave_a_reply   

    
    return render(request, 'lp/index.html',{
    'leave_a_reply': leave_a_reply,

})


def thanks(request):
    return render(request, 'lp/thanks.html', {
})
