from bottle import route, run, get, post, request, HTTPResponse, delete, response,app
import authentication
import data
from bottle_cors_plugin import cors_plugin
headers={'Access-Control-Allow-Origin': '*','Access-Control-Allow-Methods':'PUT, GET, POST, DELETE','Access-Control-Allow-Headers':'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'}

@post('/registr')
def registr():
    body,code =authentication.registration(request)
    return HTTPResponse(status=code, body=body)

@post('/token')
def token():
    body,code =authentication.token(request)
    return HTTPResponse(status=code, body=body, headers={'Access-Control-Allow-Origin':'*'})

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

app = app()
app.install(cors_plugin('*'))
run(host='0.0.0.0', port=8080, debug=True)