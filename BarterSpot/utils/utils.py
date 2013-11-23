import smtplib
import string
import random
from django.http import HttpResponseRedirect
from constants import VALIDATION_EMAIL, VALIDATION_CODE_LEN,\
    VALIDATION_SUBJECT, VALIDATION_TEXT, SMTP_ADDR
from django.core.mail import send_mail
from threading import Thread
from email.mime.text import MIMEText


class authorizationCheck(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        if request.user.is_authenticated():
            return self.func(request)
        else:
            return HttpResponseRedirect('/users/login/')


def generateRandomString(nLen=VALIDATION_CODE_LEN):
    charset = string.ascii_letters + string.digits
    listRet = [random.choice(charset) for i in range(nLen)]
    return ''.join(listRet)


def sendBlockMail(strSubject, strMessage, strFrom, strTo):
    send_mail(strSubject, strMessage, strFrom, [strTo])
    msg = MIMEText(strMessage)
    msg['Subject'] = strSubject
    msg['From'] = strFrom
    msg['To'] = strTo
    s = smtplib.SMTP(SMTP_ADDR)
    s.sendmail(strFrom, [strTo], msg.as_string())
    s.quit()


def sendNonblockMail(strSubject, strMessage, strFrom, strTo):
    th = Thread(target=sendBlockMail,
                args=(strSubject, strMessage, strFrom, strTo))
    th.start()


def sendValidationMail(strTo, strAddr, strHash, funcSend=sendNonblockMail):
    """
    Sends validation email
    Arguments:
     strTo - string with users login
     strAddr - string with users email
     strHash - validation address hash
     funcSend - function senging message
        it should have form
        funcSend(subject, message, from_email, to_email)
    """
    strMessage = VALIDATION_TEXT % {"username": strTo, "hash": strHash}
    funcSend(VALIDATION_SUBJECT, strMessage, VALIDATION_EMAIL, strAddr)
