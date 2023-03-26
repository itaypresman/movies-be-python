from flask import Flask
from lib.config import Config
from controllers.oimdb import oimdb_controller


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(oimdb_controller)
app.run(port=Config.PORT)
