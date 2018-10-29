from django.shortcuts import render
from django.http import HttpResponse
import hashlib,time,sqlite3
import logging

log = logging.getLogger("sql")
log.setLevel(level=logging.INFO)
handler = logging.FileHandler("runserver.log")
handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s <%(funcName)s> %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

def Login(request):
    if request.COOKIES.get("Auth") == hashlib.md5( str(request.META['REMOTE_ADDR'] + time.strftime("%Y-%m-%d-%H-")+str( int(time.strftime("%M")) //10)     ).encode("utf-8")).hexdigest():
        return render(request,"Admin.html")
    try:
        Account_Str = request.POST.get("Account","") ; Password_Str =request.POST.get("Password","")
        if not Account_Str or not Password_Str:
            pass
        else:
            log.info(Account_Str+"try to login.")
            conn = sqlite3.connect("Database.db");c=conn.cursor()
            try:
                c.execute("select * from User where Account = '"+Account_Str+"';")
                fa=c.fetchall()
                for i in fa:
                    if i[0] == Account_Str and i[1]==Password_Str:
                        res = HttpResponse("<script>window.location.reload();</script>")
                        Auth = hashlib.md5(str(request.META['REMOTE_ADDR'] + time.strftime("%Y-%m-%d-%H-") + str(
                            int(time.strftime("%M")) // 10)).encode("utf-8")).hexdigest()
                        res.set_cookie(key="Auth", value=Auth, max_age=600, httponly=True)
                        log.info("[Account]" +Account_Str+" [Auth] "+Auth+" is log in .")
                        return res

            except:
                pass
        return render(request,"login.html")
    except IOError:
        print(IOError)
    return render(request,"login.html")