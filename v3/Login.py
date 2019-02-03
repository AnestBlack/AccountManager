from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
import hashlib,time,sqlite3,platform,subprocess,os
import logging

log = logging.getLogger("sql")
log.setLevel(level=logging.INFO)
handler = logging.FileHandler("runserver.log")
handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s <%(funcName)s> %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

get_Auth = lambda x:hashlib.md5( str(x.META['REMOTE_ADDR'] + time.strftime("%Y-%m-%d-%H-")+str( int(time.strftime("%M")) //10)     ).encode("utf-8")).hexdigest()
md5 = lambda x:hashlib.md5(x.encode("utf-8")).hexdigest()

def Login(request):
    try:
        print("Login")
        print(request.COOKIES.get("Auth",""))
        print(request.session.get(request.COOKIES.get("Userid","")))
        if request.COOKIES.get("Auth","") == request.session.get(request.COOKIES.get("Userid",""),""):
            if request.COOKIES.get("Auth","") and request.session.get(request.COOKIES.get("Userid",""),"") :

                return HttpResponseRedirect("/Admin")
                #print(request.session.items())
                #return HttpResponse("test")
        
        try:
            Account_Str = request.POST.get("Account","") ; Password_Str =request.POST.get("Password","")
            if not Account_Str or not Password_Str:
                pass
            else:
                log.info(Account_Str+" try to login.")
                conn = sqlite3.connect("Database.db");c=conn.cursor()
                try:
                    c.execute("select * from User where Account = '"+Account_Str+"';")
                    fa=c.fetchall()
                    for i in fa:
                        if i[0] == Account_Str and i[1]==Password_Str:
                            res = HttpResponse("<script>window.location.reload();</script>")
                            Auth = get_Auth(request)
                            request.session[md5(i[0])] = get_Auth(request)
                            res.set_cookie(key="Auth", value=Auth, max_age=86400)
                            res.set_cookie(key="Userid", value=md5(i[0]), max_age=86400)
                            res.set_cookie(key="id",value=request.session.session_key)
                            log.info("[Account]" +Account_Str+" [Auth] "+Auth+" is log in .")
                            print(request.session.items())
                            return res
                except:
                    pass
            return render(request,"login.html")
        except IOError:
            print(IOError)
        return render(request,"login.html")
    except IOError:
        print(IOError)
        return render(request,"login.html")

def index(request):
    print("\nAdmin\n")
    print(request.COOKIES.items())
    print(request.session.items())
    #if not request.COOKIES.get("Auth"):
    #    return HttpResponseRedirect("/login")
    #if request.COOKIES.get("Auth") == request.session.get(request.COOKIES.get("Userid")):
    #    return render(request,"Admin.html")
    #else:
    #    return HttpResponseRedirect("/login")
    return render(request,"Admin.html")


def load_runserverlog(request):
    print(request.COOKIES.get("Auth"))
    if not request.COOKIES.get("Auth") == hashlib.md5( str(request.META['REMOTE_ADDR'] + time.strftime("%Y-%m-%d-%H-")+str( int(time.strftime("%M")) //10)     ).encode("utf-8")).hexdigest():
        return HttpResponse("Auth fail")
    log.info(request.COOKIES["Userid"]+" is Loaded log.")
    if platform.system() == "Windows":
        return HttpResponse(os.popen("type runserver.log").read().replace("\n",r"<br>"))
    elif platform.system() == "Linux":
        return HttpResponse(os.popen("cat runserver.log").read().replace("\n",r"<br>"))
    else:
        return HttpResponse("System is not supported")