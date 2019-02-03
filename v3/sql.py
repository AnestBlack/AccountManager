from django.shortcuts import render
from django.http import HttpResponse
import base64 ,time ,sqlite3 ,hashlib
import logging

log = logging.getLogger("sql")
log.setLevel(level=logging.INFO)
handler = logging.FileHandler("runserver.log")
handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s <%(funcName)s> %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

def Save_Result_to_sql(request):
    """if not AddressStr and not AccountStr and not password:
        return 0"""
    if request.method=="POST":
        if not request.POST.get('AddressStr','') and request.POST.get('AccountStr','') and request.POST.get('password',''):
            return 0

        AddressStr=request.POST.get('AddressStr','')
        AccountStr=request.POST.get('AccountStr','')
        password=request.POST.get('password','')
        Text=request.POST.get('Text','')

        log.info(request.META['REMOTE_ADDR']+" Address { "+AddressStr+" } Account { "+AccountStr+" }")

        AddressStr = base64.b64encode(AddressStr.encode()).decode()
        AccountStr = base64.b64encode(AccountStr.encode()).decode()
        password = base64.b64encode(password.encode()).decode()
        if Text:
            Text = base64.b64encode(Text.encode()).decode()
        else:
            Text="Tm9WYWx1ZQ==" # NoValue
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute('insert into Data values("'+AddressStr+'","'+AccountStr +'","'+ password +'","'+ base64.b64encode( time.strftime(r"%Y-%m-%d--%H-%M-%S--%A").encode() ).decode()+'","'+Text+'");')
        conn.commit()
        del c,conn
        return HttpResponse("Succ")

def Search_Item(request,keyInt,keywordStr):
    if not keyInt and not keywordStr:
        return 0
    if keyInt == 0:
        KeyMode_Str='Address'
    elif keyInt == 1:
        KeyMode_Str='Account'
    elif keyInt == 2:
        KeyMode_Str='Password'
    elif keyInt == 3:
        KeyMode_Str="Text"
        return 0
    #////////////////////////////////////////////////////////////////////////////////////////////////
    """if KeyMode_Str == "Text":
        conn = sqlite3.connect('Database.db')
        c = conn.cursor()
        c.execute('select Text from Data;')
        for item in c.fetchall():
            if item == 
    """
    #////////////////////////////////////////////////////////////////////////////////////////////////
    log.info(request.META['REMOTE_ADDR']+" ["+KeyMode_Str+"] ["+keywordStr+"]")

    keywordStr = base64.b64encode(keywordStr.encode()).decode()
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('select Address,Account,Password,Date,Text from Data where '+KeyMode_Str+' = "'+keywordStr+'";')
    result_Str='<font size=5>'
    for Item in c.fetchall():
        result_Str+='<table border="1"><tr><td>Address</td><td><input readonly style="width:250px" value="'+base64.b64decode(Item[0].encode()).decode()+'"/></td></tr> \
         <tr><td>  Account  </td><td><input readonly style="width:250px" value="'+base64.b64decode(Item[1].encode()).decode()+'"/></td></tr> \
          <tr><td>  Password  </td><td><input readonly style="width:250px" value="'+base64.b64decode(Item[2].encode()).decode()+'"/></td></tr>\
          <tr><td>  Date  </td><td><input readonly style="width:250px" value="'+base64.b64decode(Item[3].encode()).decode()+'"/></td></tr>\
          <tr><td>  Text  </td><td><input readonly style="width:250px" value="'+base64.b64decode(Item[4].encode()).decode() +'"/></td></tr></table><br>'
    result_Str+='</font>'
    del c,conn
    return HttpResponse(result_Str)

def Delete_Item(request,keywordStr):
    if not keywordStr:
        return 0
    log.warning(request.META['REMOTE_ADDR']+" "+keywordStr)

    keywordStr = base64.b64encode(keywordStr.encode()).decode()
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('delete from Data where Date = "'+keywordStr+'";')
    conn.commit()
    del c,conn
    return HttpResponse('succ')

def Backup_Database(request):
    if not request.COOKIES.get("Auth") == hashlib.md5( str(request.META['REMOTE_ADDR'] + time.strftime("%Y-%m-%d-%H-")+str( int(time.strftime("%M")) //10)     ).encode("utf-8")).hexdigest():
        return HttpResponse("Auth fail")
    log.warning(request.META['REMOTE_ADDR']+" Downloaded backup file ")
    Database_file=open('Database.db',"rb")
    
    response_file=HttpResponse(Database_file.read())
    response_file['Content-Type']=r'application/octet-stream'
    response_file['Content-Disposition'] = 'attachment; filename="'+time.strftime("%Y-%m-%d (%H-%M-%S) AM3.4_backup.db")+'"'
    
    Database_file.close()
    del Database_file
    return response_file

def Update_Text(request,DateStr,TextStr):
    if not DateStr or not TextStr:
        return 0
    log.info(request.META['REMOTE_ADDR']+" DateStr{ "+DateStr+" } TextStr { "+TextStr+" }")
    DateStr=base64.b64encode(DateStr.encode()).decode()
    TextStr=base64.b64encode(TextStr.encode()).decode()

    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('update Data set Text="'+TextStr+'" where Date="'+DateStr +'";')
    conn.commit()
    del c,conn
    return HttpResponse('succ')
    
"""
def Restore_Database(request):
    pass
"""