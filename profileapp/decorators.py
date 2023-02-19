from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):        #*args : tuple, **kwargs : dictinary
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()      # reposnse 를 취소
        return func(request, *args, **kwargs)
    return decorated