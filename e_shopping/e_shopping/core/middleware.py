from datetime import datetime, timedelta
from django.conf import settings
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import http

class AutoLogout:

    """
    middleware to expire session of a user if user is inactive for 5 minutes
    """

    def process_request(self, request):
        if not request.user.is_authenticated():
            # Can't log out if not logged in
            return
        try:
            if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                auth.logout(request)
                del request.session['last_touch']
                return
        except KeyError as e:
            print ("Unable to logout the user; detail: \n {0}".format(e))
        request.session['last_touch'] = datetime.now()
