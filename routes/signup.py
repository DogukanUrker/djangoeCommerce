from helpers import Blueprint, render_template


signupBlueprint = Blueprint("signup", __name__)


@signupBlueprint.route("/signup/direct=<direct>")
def signup(direct):
    return render_template("signup.html")
