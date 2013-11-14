from django.http import HttpResponseRedirect


class authorizationCheck(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        if request.user.is_authenticated():
            return self.func(request)
        else:
            return HttpResponseRedirect('/users/login/')
