from flask import Flask
from flask_cors import CORS
from lib.config import Config
from controllers.oimdb import oimdb_controller


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(oimdb_controller)
app.run(port=Config.PORT)
