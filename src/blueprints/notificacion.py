from flask import Flask, jsonify, request, Blueprint
from ..commands.create_notificacion import CreateNotificacion
from ..commands.get_notificacion import  GetNotificacion
from ..commands.get_notificacion_user import GetNotificacionUser
from ..commands.reset_notificacion import ResetNotificacion

notificacion_blueprint = Blueprint('notificaciones', __name__)

@notificacion_blueprint.route('/notificaciones', methods = ['POST'])
def create():
    notificacion = CreateNotificacion(request.get_json()).execute()
    return jsonify(notificacion), 201

@notificacion_blueprint.route('/notificaciones/<id>', methods = ['GET'])
def show(id):
    """ Authenticate(auth_token()).execute() """
    notificacion = GetNotificacion(id).execute() 
    return jsonify(notificacion)

@notificacion_blueprint.route('/notificaciones/user/<id>', methods = ['GET'])
def show_notficacion_user(id):
    """ Authenticate(auth_token()).execute() """
    notificacion = GetNotificacionUser(id).execute()
    return jsonify(notificacion)

@notificacion_blueprint.route('/notificaciones/reset', methods = ['POST'])
def reset():
    ResetNotificacion().execute()
    return jsonify({'status': 'OK'})

@notificacion_blueprint.route('/notificaciones/ping', methods = ['GET'])
def ping():
    return 'pong'

def auth_token():
    if 'Authorization' in request.headers:
        authorization = request.headers['Authorization']
    else:
        authorization = None
    return authorization