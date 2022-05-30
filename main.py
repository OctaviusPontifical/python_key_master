from bottle import route, run, get, post, request, HTTPResponse, delete
import authentication
import data

@post('/registr')
def registr():
    body,code =authentication.registration(request)
    return HTTPResponse(status=code, body=body)

@post('/token')
def token():
    body,code =authentication.token(request)
    return HTTPResponse(status=code, body=body)

@post('/record')
def record():
    body,code = data.addrecord(request)
    return HTTPResponse(status=code, body=body)

@delete('/record')
def delrecord():
    body,code = data.delrecord(request)
    return HTTPResponse(status=code, body=body)

@get('/getrecord/<id_record>')
def record(id_record):
    body,code = data.getrecord(request,id_record)
    return HTTPResponse(status=code, body=body)

@get('/getrecord')
def record():
    body,code = data.getrecord(request,None)
    return HTTPResponse(status=code, body=body)

run(host='0.0.0.0', port=8080, debug=True)