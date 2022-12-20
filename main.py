from bottle import route, run, get, post, request, HTTPResponse, delete, response,app
import authentication
import data
from bottle_cors_plugin import cors_plugin
headers={'Access-Control-Allow-Origin': '*','Content-Type': 'application/json'}

@post('/registr')
def registr():
    body,code =authentication.registration(request)
    return HTTPResponse(status=code, body=body, headers=headers)

@post('/token')
def token():
    body,code =authentication.token(request)
    return HTTPResponse(status=code, body=body, headers=headers)

@post('/record')
def record():
    body,code = data.addrecord(request)
    return HTTPResponse(status=code, body=body, headers=headers)

@delete('/record')
def delrecord():
    body,code = data.delrecord(request)
    return HTTPResponse(status=code, body=body, headers=headers)

@get('/getrecord/<id_record>')
def record(id_record):
    body,code = data.getrecord(request,id_record)
    return HTTPResponse(status=code, body=body, headers=headers)

@get('/getrecord')
def record():
    body,code = data.getrecord(request,None)
    return HTTPResponse(status=code, body=body, headers=headers)

app = app()
app.install(cors_plugin('*'))
run(host='0.0.0.0', port=8080, debug=True)