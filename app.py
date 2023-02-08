import socket
from helpers import Flask, secrets

from routes.index import indexBlueprint

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)
app.config["SESSION_PERMANENT"] = True

app.register_blueprint(indexBlueprint)

match __name__:
    case "__main__":
        app.run(debug=True, host=socket.gethostbyname(socket.gethostname()))
