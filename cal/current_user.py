def user_from_session_key(session_key):
    from django.conf import settings
    from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, load_backend
    from django.contrib.auth.models import AnonymousUser

    session_engine = __import__(settings.SESSION_ENGINE, {}, {}, [''])
    session_wrapper = session_engine.SessionStore(session_key)
    user_id = session_wrapper.get(SESSION_KEY)
    auth_backend = load_backend(session_wrapper.get(BACKEND_SESSION_KEY))

    if user_id and auth_backend:
      return auth_backend.get_user(user_id)
    else:
      return AnonymousUser()



#from .models import *

# def current_user(request):
    # c_usr = Event.objects.filter(user=request.user)
    # print(c_usr)
    # return c_usr