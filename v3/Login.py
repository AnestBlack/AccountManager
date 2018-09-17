from django.shortcuts import render
from django.http import HttpResponse
import hashlib,time

admin_account = "admin"
admin_pass = "admin"

def Login(request):
    if request.COOKIES.get("Auth") == hashlib.md5( str(request.META['REMOTE_ADDR'] + time.strftime("%Y-%m-%d-%H-")+str( int(time.strftime("%M")) //10)     ).encode("utf-8")).hexdigest():
        return render(request,"Admin.html")
    try:

        Account_Str = request.POST.get("Account","") ; Password_Str =request.POST.get("Password","")
        if not Account_Str or not Password_Str:
            pass
        elif Account_Str == admin_account and Password_Str == admin_pass:
            res=HttpResponse("<script>window.location.reload();</script>")
            Auth = hashlib.md5( str(request.META['REMOTE_ADDR'] + time.strftime("%Y-%m-%d-%H-")+str( int(time.strftime("%M")) //10)     ).encode("utf-8")).hexdigest()
            res.set_cookie(key="Auth",value=Auth,max_age=600,httponly=True)
            return res
        return render(request,"login.html")
    except IOError:
        print(IOError)
    return render(request,"login.html")