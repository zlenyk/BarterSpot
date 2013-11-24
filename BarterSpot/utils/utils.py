import smtplib
import string
import random
from django.http import HttpResponseRedirect
from constants import VALIDATION_EMAIL, VALIDATION_CODE_LEN,\
    VALIDATION_SUBJECT, VALIDATION_TEXT, SMTP_ADDR,\
    GMAIL_USER, GMAIL_PASS
from threading import Thread
from email.mime.text import MIMEText
from email.header import Header


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
    try:
        # print("sending mail to ", strTo)
        msg = MIMEText(strMessage, _charset='utf-8')
        msg['Subject'] = Header(strSubject, 'utf-8')
        msg['From'] = strFrom
        msg['To'] = strTo
        s = smtplib.SMTP(SMTP_ADDR)
        s.ehlo()
        s.starttls()
        s.login(GMAIL_USER, GMAIL_PASS)
        s.sendmail(strFrom, [strTo], msg.as_string())
        s.quit()
    except Exception, error:
        print("Unable to send e-mail: '%s'." % str(error))


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
