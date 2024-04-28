from flask import Flask, jsonify
from src.blueprints.notificacion import notificacion_blueprint
from src.errors.errors import ApiError
from flask_cors import CORS
from src.dynamodb_notificacion import DynamoDbNotificacion

application = Flask(__name__)
application.register_blueprint(notificacion_blueprint)
CORS(application)
DynamoDbNotificacion().create_table()
## add comment
@application.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description 
    }
    return jsonify(response), err.code
##
if __name__ == "__main__":
    application.run(host="0.0.0.0", port = 5005, debug = True)
