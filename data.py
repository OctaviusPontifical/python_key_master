from authentication import authorization
from database import selectdate
from base64 import  b64encode

def addrecord(request):
    code,id = authorization(request.headers['Authorization'])
    if code==0:
        if 'id' in request.json:
            code , message = selectdate('cu_pass',[request.json['id'],id,request.json['login'],to_code(request.json['password']),request.json["description"]])
        else :
            code , message = selectdate('cu_pass',[None,id,request.json['login'],to_code(request.json['password']),request.json["description"]])
        if code ==0:
            return None,200
        else:
            return '{"message":"Server error!"}', 501
    else :
        return '{"message":"token is invalid"}',401

def delrecord(request):
    code, id = authorization(request.headers['Authorization'])
    if code == 0:
        code, message = selectdate('del_pass', [request.json['id'], id])
        if code == 0:
            return None, 200
        else:
            return '{"message":"Server error!"}', 501
    else:
        return '{"message":"token is invalid"}', 401


def getrecord(request,id_record):
    code, id = authorization(request.headers['Authorization'])
    if code == 0:
        code, message,tab = selectdate('get_data', [id_record, id])
        if code == 0:
            return tab, 200
        else:
            return '{"message":"Server error!"}', 501
    else:
        return '{"message":"token is invalid"}', 401

def to_code(text):
    base = b64encode(bytes(text,'utf-8'))
    return str(base,'utf-8')