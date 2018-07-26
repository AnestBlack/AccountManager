from django.shortcuts import render
from django.http import HttpResponse
import hashlib , re , base64 ,time , string ,random
from struct import pack

MyCode = 'anyword'+  # please change the value of left and delete the "+"
r=random.Random(MyCode)

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

#///////////////////////////////////////////////////////////////////////////////////////////////////////////

getPassword_max_get_num = lambda x=0:[string.digits[r.randrange(0,10)],string.digits[r.randrange(0,10)],string.digits[r.randrange(0,10)]]
getPassword_max_get_lowercase = lambda x=0:[string.ascii_lowercase[r.randrange(0,26)],string.ascii_lowercase[r.randrange(0,26)],string.ascii_lowercase[r.randrange(0,26)]]
getPassword_max_get_uppercase = lambda x=0: [string.ascii_uppercase[r.randrange(0,26)],string.ascii_uppercase[r.randrange(0,26)],string.ascii_uppercase[r.randrange(0,26)]]
getPassword_max_get_word = lambda x=0: [string.ascii_letters[r.randrange(0,52)],string.ascii_letters[r.randrange(0,52)],string.ascii_letters[r.randrange(0,52)]]
getPassword_max_get_punctuation = lambda x=0: [string.punctuation[r.randrange(0,32)],string.punctuation[r.randrange(0,32)],string.punctuation[r.randrange(0,32)]]
getPassword_max_get_all = lambda x=0: [string.printable[r.randrange(0,94)],string.printable[r.randrange(0,94)],string.printable[r.randrange(0,94)]]

def getPassword_max(request):
    password_list = getPassword_max_get_num() + getPassword_max_get_lowercase() + \
                    getPassword_max_get_uppercase() + getPassword_max_get_word() + \
                    getPassword_max_get_punctuation() + getPassword_max_get_all()
    result_password=""
    for i in range(len(password_list)):
        num_randrange=r.randrange(len(password_list))
        result_password += password_list[num_randrange]
        del password_list[num_randrange]
    return HttpResponse(result_password)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////



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