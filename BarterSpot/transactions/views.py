# Create your views here.
from BarterSpot.users.models import BarterUser
from BarterSpot.announcements.models import Announcement
from BarterSpot.transactions.models import Transaction
from BarterSpot.messages.models import Message
from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime

def index(request):
    me = BarterUser.getUserFromRequest(request)
    finished_from_me = Transaction.getFinishedTransactionsFrom(me)
    finished_to_me = Transaction.getFinishedTransactionsTo(me)
    all_transactions = Transaction.getAllTransactionsFromAndTo(me)   
 
    pending_from_me = Transaction.getPendingTransactionsFrom(me)
    pending_to_me = Transaction.getPendingTransactionsTo(me)

    return render(request, 'transactions/index.html', {
        'finished_from_me': finished_from_me,
        'finished_to_me': finished_to_me,
        #'all_transactions': all_transactions,
        'pending_from_me': pending_from_me,
        'pending_to_me': pending_to_me,
    })


def offer_exchange(request, want_id):
    me = BarterUser.getUserFromRequest(request).id
    anns = Announcement.getUsersAnnouncements(me)
    
    return render(request, 'transactions/my_offers.html', {
        'announcements': anns,
        'want_id': want_id,
    })


def make_transaction(request, want_id, for_id):
    me = BarterUser.getUserFromRequest(request)
    source_ann = Announcement.getAnnouncementById(for_id)
    target_ann = Announcement.getAnnouncementById(want_id)
    target_user = target_ann.user

    Transaction.createTransaction(
        me,
        target_user,
        Transaction.PENDING,
        source_ann,
        target_ann,
    )

    offer_subject = "Exchange Offer"
    body = "Not yet developed..."    

    Message.sendMessage(
        Message.OFFER,
        me,
        target_user,
        offer_subject,
        body,
    )
    return HttpResponseRedirect('/transactions/')

def accept(request, tid):
    t = Transaction.getTransactionById(tid)
    t.status = Transaction.ACCEPTED
    t.response_date = datetime.today()
    t.save()
    
    me = BarterUser.getUserFromRequest(request)
    target_user = t.source_ann.user

    subject = "Offer accepted"
    body = "Not yet developed"
    Message.sendMessage(
        Message.OFFER,
        me,
        target_user,
        subject,
        body,
    )
    return HttpResponseRedirect('/transactions/')

def reject(request, tid):
    t = Transaction.getTransactionById(tid)
    t.status = Transaction.REJECTED
    t.response_date = datetime.today()
    t.save()

    me = BarterUser.getUserFromRequest(request)
    target_user = t.source_ann.user

    subject = "Offer rejected"
    body = "Not yet deve;p[ed"
    Message.sendMessage(
        Message.OFFER,
        me,
        target_user,
        subject,
        body,
    )
    return HttpResponseRedirect('/transactions/')



                    





