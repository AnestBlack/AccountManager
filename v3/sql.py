from django.shortcuts import render
from django.http import HttpResponse
import base64 ,time ,sqlite3


def Save_Result_to_sql(request,AddressStr,AccountStr,password,Text):
    if not AddressStr and not AccountStr and not password:
        return 0
    if len(password)%4 != 0:
        password+='='*(4-len(password)%4)
    password=base64.b64decode( password.encode('utf-8') ).decode('utf-8')

    AddressStr = base64.b64encode(AddressStr.encode()).decode()
    AccountStr = base64.b64encode(AccountStr.encode()).decode()
    password = base64.b64encode(password.encode()).decode()
    if Text:
        Text = base64.b64encode(Text.encode()).decode()
    else:
        Text="NoValue"
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('insert into Data values("'+AddressStr+'","'+AccountStr +'","'+ password +'","'+ base64.b64encode( time.strftime(r"%Y-%m-%d--%H-%M-%S--%A").encode() ).decode()+'","'+Text+'");')
    conn.commit()
    c.close();conn.close();c,conn=None,None
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
    keywordStr = base64.b64encode(keywordStr.encode()).decode()

    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('select Address,Account,Password,Date,Text from Data where '+KeyMode_Str+' = "'+keywordStr+'";')
    result_Str='<font size=5>'
    for Item in c.fetchall():
        result_Str+='<table border="1"><tr><td>Address</td><td>'+base64.b64decode(Item[0].encode()).decode()+'</td></tr> \
         <tr><td>Account</td><td>'+base64.b64decode(Item[1].encode()).decode()+'</td></tr> \
          <tr><td>Password</td><td>'+base64.b64decode(Item[2].encode()).decode()+'</td></tr>\
          <tr><td>Date</td><td>'+base64.b64decode(Item[3].encode()).decode()+'</td></tr>\
          <tr><td>Text</td><td>'+base64.b64decode(Item[4].encode()).decode()+'</td></tr></table><br>'
    result_Str+='</font>'
    c.close();conn.close();c,conn=None,None
    return HttpResponse(result_Str)

def Delete_Item(request,keywordStr):
    if not keywordStr:
        return 0
    keywordStr = base64.b64encode(keywordStr.encode()).decode()
    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('delete from Data where Date = "'+keywordStr+'";')
    conn.commit()
    return HttpResponse('succ')

def Backup_Database(request):
	Database_file=open('Database.db',"rb")
	
	response_file=HttpResponse(Database_file.read())
	response_file['Content-Type']=r'application/octet-stream'
	response_file['Content-Disposition'] = 'attachment; filename="'+time.strftime("%Y-%m-%d (%H-%M-%S) AM3.2_backup.db")+'"'
	
	Database_file.close()
	Database_file=None
	return response_file

def Update_Text(request,DateStr,TextStr):
    if not DateStr or not TextStr:
        return 0
    DateStr=base64.b64encode(DateStr.encode()).decode()
    TextStr=base64.b64encode(TextStr.encode()).decode()

    conn = sqlite3.connect('Database.db')
    c = conn.cursor()
    c.execute('update Data set Text="'+TextStr+'" where Date="'+DateStr +'";')
    conn.commit()
    c.close();conn.close();c,conn=None,None
    return HttpResponse('succ')
    
"""
def Restore_Database(request):
	pass
"""