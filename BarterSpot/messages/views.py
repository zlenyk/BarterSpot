# Create your views here.
from BarterSpot.messages.forms import MessageForm
from BarterSpot.utils.utils import authorizationCheck
from django.shortcuts import render
from django.http import HttpResponseRedirect
from BarterSpot.users.models import BarterUser
from models import Message

@authorizationCheck
def index(request):
    form = MessageForm()
    me = BarterUser.getUserFromRequest(request).id
    inbox = Message.getMessagesTo(me)
    outbox = Message.getMessagesFrom(me)
    return render(request, 'messages/index.html', {
        'form': form,
        'inbox': inbox,
        'outbox': outbox,
    })

@authorizationCheck
def send(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            Message.sendMessage(
                Message.ORDINARY,
                BarterUser.getUserFromRequest(request),
                recipient,
                subject,
                body)
    return HttpResponseRedirect('/messages/')

#@authorizationCheck
def show_message(request, msg_id):
    msg = None
    try:
        msg = Message.objects.get(pk=msg_id)
    except Message.DoesNotExist:
        pass
    return render(request, 'messages/message.html', {'msg': msg}) 
