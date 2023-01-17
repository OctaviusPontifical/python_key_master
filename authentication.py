import datetime
import string
import jwt
import database
import random
import hashlib
from config import setting


JWT_KEY = setting.get_param('JWT_KEY') #128 bit key

def generator(size):
    keylist = [random.choice(string.ascii_letters + string.digits) for i in range(size)]
    return ("".join(keylist))

def registration(request):
    salt = generator(5)
    hash = hashlib.sha512(request.json['password'].encode('utf-8') + salt.encode('utf-8')).hexdigest()
    code,message = database.selectdate('registration', [request.json['login'], hash,salt])
    if code==0:
        return None,200
    elif code==2:
        body = '{"message":"login already exist"}'
        return body,400
    else :
        print('Code: ',code,' Message: ',message)
        body = '{"message": "Server error !"}'
        return body,500

def create_token( user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
            'iat': datetime.datetime.utcnow(),
            'id': user_id
        }
        return jwt.encode(payload,JWT_KEY,algorithm='HS256')
    except Exception as e:
        return e



def token (request):
    code,message,hash,salt,user_id = database.selectdate('get_user_data',[request.json['login']])
    if code ==2:
        return '{"message":"login or password is valid"}',401
    elif code ==1:
        body = '{"message": "Server error !"}'
        return body, 500
    else:
        hashedPassword = hashlib.sha512(request.json['password'].encode('utf-8') + salt.encode('utf-8')).hexdigest()
        if hashedPassword==hash:
            body='{"token":"%s"}' % (create_token(user_id))
            return body,200
        else :
            return '{"message":"login or password is valid"}', 401


def authorization(token):
    try:
        payload = jwt.decode(token, JWT_KEY,algorithms="HS256")
        return 0,payload['id']
    except jwt.ExpiredSignatureError:
        return 1,None
    except jwt.InvalidTokenError:
        return 1,None

#print(registration(json.JSONEncoder("{'login':'login','password':'password'}")))

#print(create_token('dsvcsd'))