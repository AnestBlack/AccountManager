from django.shortcuts import render
from django.http import HttpResponse
import ctypes , configparser , hashlib , re , base64 ,time ,os.path ,sqlite3 ,sys
from struct import pack

MyCode = 'YjFkZjVhMWI0Y2M='
def index(request):
    return render(request, 'index.html')

def index_zh(request):
    return render(request, 'index_zh.html')

def search(request):
    return render(request, 'search.html')

def search_zh(request):
    return render(request, 'search_zh.html')


def getAccount(request,AddressStr):
    try:
        Accountmd5Str=hashlib.md5( str(AddressStr+"AM3.0"+time.strftime("%Y-%m-%d %H-%M-%S")+MyCode).encode("utf-8") ).hexdigest()
        AccountStrList=re.compile("[a-z]").findall(Accountmd5Str)
        AccountStr=AccountStrList[0]
        i=int( ( len(Accountmd5Str)-len(AccountStrList) ) /len(Accountmd5Str) )
        while i <len(Accountmd5Str):
            AccountStr += Accountmd5Str[i]
            i+=5
    except IOError:
        print(IOError)
    return HttpResponse(AccountStr)

def getPassword_1(request,AddressStr,AccountStr):
    if not AddressStr or not AccountStr:
        return HttpResponse("")
    try:
        AddressStr_And_Account_md5_str=hashlib.md5( str(AddressStr+AccountStr+"AM3.0"+time.strftime("%Y-%m-%d %H-%M-%S")+MyCode).encode("utf-8")).hexdigest()
        PasswordNumlist=re.compile("[0-9]").findall(AddressStr_And_Account_md5_str)
        return HttpResponse(GenerateFunction_HandleList_to_Str(PasswordNumlist)[:6])
    except IOError:
        print(IOError)

def getPassword_2(request,AddressStr,AccountStr):
    try:
        AddressStr_And_Account_md5_str=hashlib.md5( str(AddressStr+AccountStr+"AM3.0"+time.strftime("%Y-%m-%d %H-%M-%S")+MyCode).encode("utf-8")).hexdigest()
        i = 0
        Password_NumAndWord_Str=""
        while i < len(AddressStr_And_Account_md5_str):
            Password_NumAndWord_Str+=AddressStr_And_Account_md5_str[i]
            i+=3
        return HttpResponse(Password_NumAndWord_Str)
    except IOError:
        print(IOError)

def getPassword_3(request,AddressStr,AccountStr):
    try:
        PasswordHighest_md5_Str = hashlib.md5( str(AddressStr+AccountStr+"AM3.0"+time.strftime("%Y-%m-%d %H-%M-%S")+MyCode).encode("utf-8")).hexdigest()

        i=0;Password3_Str=""
        while i < len(PasswordHighest_md5_Str):
            Password3_Str+=PasswordHighest_md5_Str[i]
            i+=3
        Password3_Str=base64.b64encode(Password3_Str.encode(encoding="utf-8"))
        return HttpResponse( str(Password3_Str).replace("b'","").replace("'","") )
    except IOError:
        print(IOError)

#////////////////////////////////////////////////////////////////////
def getPassword_max(request,Password_3):
    try:
        if len(Password_3) > 10 :
            Password_max = encypt( Password_3.encode('utf-8') , MyCode.encode('utf-8') )
            return HttpResponse( str(Password_max)[2:-1] )
    except IOError:
        print(IOError)
#////////////////////////////////////////////////////////////////////

def encypt(txt, pw):
    temp = bytes()
    j = 0
    for i in txt:
        temp += pack("B", (  i + pw[ j % len(pw) ]  ) % 255)
        j += 1
    return temp

def GenerateFunction_HandleList_to_Str(Keylist=[],mode=0):
    if mode ==0:
        Resulttextstr=""
        for i in range(len(Keylist)):
            Resulttextstr+=Keylist[i]
        return Resulttextstr
    else:
        Resulttextstr=""
        for i in range(len(Keylist)):
            Resulttextstr+=Keylist[i]+"\n"
        return Resulttextstr

def Save_Result_to_sql(request,AddressStr,AccountStr,password):
    if not AddressStr and not AccountStr and not password:
        return 0
    if len(password)%4 != 0:
        password+='='*(4-len(password)%4)
    password=base64.b64decode( password.encode('utf-8') ).decode('utf-8')
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('insert into Data values("'+AddressStr+'","'+AccountStr +'","'+ password +'","'+time.strftime("%Y-%m-%d--%H-%M-%S--%A")+'");')
    conn.commit()
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
    else:
        return 0
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('select Address,Account,Password,Date from Data where '+KeyMode_Str+' = "'+keywordStr+'";')
    result_Str='<font size=5>'
    for Item in c.fetchall():
        result_Str+='<table border="1"><tr><td>Address</td><td>'+Item[0]+'</td></tr> \
         <tr><td>Account</td><td>'+Item[1]+'</td></tr> \
          <tr><td>Password</td><td>'+Item[2]+'</td></tr>\
          <tr><td>Date</td><td>'+Item[3]+'</td></tr><br>'
    result_Str+='</font>'
    return HttpResponse(result_Str)

def Delete_Item(request,keywordStr):
    if not keywordStr:
        return 0
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('delete from Data where Date = "'+keywordStr+'";')
    conn.commit()
    return HttpResponse('succ')
