from authentication import authorization
from database import selectdate

def addrecord(request):
    code,id = authorization(request.headers['Authorization'])
    if code==0:
        if 'id' in request.json:
            code , message = selectdate('cu_pass',[request.json['id'],id,request.json['login'],request.json['password']])
        else :
            code , message = selectdate('cu_pass',[None,id,request.json['login'],request.json['password']])
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