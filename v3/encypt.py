from django.shortcuts import render
from django.http import HttpResponse
import hashlib , re , base64 ,time , string ,random
from struct import pack

MyCode = """anyword"""+  # please change the value of left and delete the "+"
r=random.Random(MyCode+time.strftime(r"%Y-%m-%d %H-%M-%S"))

get_num = lambda x=0:str( string.digits[r.randrange(0,10)] )
get_lowercase = lambda x=0:string.ascii_lowercase[r.randrange(0,26)]
get_uppercase = lambda x=0:string.ascii_uppercase[r.randrange(0,26)]
get_word = lambda x=0:str( string.ascii_letters[r.randrange(0,52)] )
get_punctuation = lambda x=0:string.punctuation[r.randrange(0,32)]
get_all = lambda x=0:string.printable[r.randrange(0,94)]

def getAccount(request):
    try:
        n=r.randrange(7,11)
        AccountStr = get_word()
        for _ in range(n):
            if r.randrange(0,2) <1:
                AccountStr += get_word()
            else:
                AccountStr += get_num()
    except IOError:
        print(IOError)
    return HttpResponse(AccountStr)

def getPassword_1(request):
    result=""
    for i in range(6):
        result +=get_num()
    return HttpResponse(result)

def getPassword_2(request):
    try:
        n=r.randrange(8,14)
        Password_NumAndWord_Str = str()
        for _ in range(n):
            t =r.randrange(0,3)
            if t <1:
                Password_NumAndWord_Str += get_lowercase()
            elif t<2:
                Password_NumAndWord_Str += get_num()
            else:
                Password_NumAndWord_Str += get_uppercase()
        return HttpResponse(Password_NumAndWord_Str)
    except IOError:
        print(IOError)

def getPassword_3(request):
    try:
        Password3_Str=""
        for _ in range(10):
            if r.randrange(0,2) <1:
                Password3_Str += get_word()
            else:
                Password3_Str += get_num()
        return HttpResponse( base64.b64encode(Password3_Str.encode(encoding="utf-8")).decode() )
    except IOError:
        print(IOError)

def getPassword_max(request):
    password_list = [get_num()] + [get_num()] + [get_num()] + \
                    [get_lowercase()] + [get_lowercase()] + [get_lowercase()] + \
                    [get_uppercase()] + [get_uppercase()] + [get_uppercase()] + \
                    [get_word()] + [get_word()] + [get_word()] + \
                    [get_punctuation()] + [get_punctuation()] + [get_punctuation()] + \
                    [get_all()] + [get_all()] + [get_all()]
    result_password=""
    for i in range(len(password_list)):
        num_randrange=r.randrange(len(password_list))
        result_password += password_list[num_randrange]
        del password_list[num_randrange]
    return HttpResponse(result_password)
