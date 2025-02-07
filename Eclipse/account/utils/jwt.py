#restframework import
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError,InvalidToken

#django imports
from django.contrib.auth.models import User

from django.shortcuts import redirect

def pegar_user_jwt(request):
    jwt = JWTAuthentication()
    token = request.COOKIES.get('access',None)
    
    if token is None:
        return None
    
    try : 
        token_validado = jwt.get_validated_token(token)
        user = jwt.get_user(token_validado)
        return user
    except TokenError:
        return None
    except InvalidToken:
        return None
    
def jwt_login_required(func):
    def interno(request,*args,**kwargs):
        if pegar_user_jwt(request) is None:
            return redirect("user")
        return func(request,*args,**kwargs)
    
    return interno