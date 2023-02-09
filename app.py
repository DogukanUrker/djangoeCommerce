import socket

from helpers import Flask, secrets, mongoConnect

from routes.index import indexBlueprint
from routes.signup import signupBlueprint

mongoConnect()

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(32)
app.config["SESSION_PERMANENT"] = True

app.register_blueprint(indexBlueprint)
app.register_blueprint(signupBlueprint)
match __name__:
    case "__main__":
        app.run(debug=True, host=socket.gethostbyname(socket.gethostname()))
