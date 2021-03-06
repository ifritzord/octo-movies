from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from recensioni.models import Recensione
from recensioni.utility import latestOfficial
from .settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL

HOMEPAGE_URL = 'index.html'

# Views homepage utenti non registrati
def home (request):
    # Utente registrato
    if request.user.is_authenticated():
        return  HttpResponseRedirect(LOGIN_REDIRECT_URL)
    # Utente anonimo
    recensioni = latestOfficial()
    context = {'recensioni':recensioni, 'homepage':'home'}
    return render(request, HOMEPAGE_URL, context)

# View logout dell'utente
# Per essere rigorosi (seguendo il progetto) bisognerebbe inserire il  
# decoratore @login_required, ma introdurrebbe un ciclo login > logout > home
def logout_view (request):
        logout(request)
        return  HttpResponseRedirect(LOGOUT_REDIRECT_URL)
