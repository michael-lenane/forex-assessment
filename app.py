from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/test")
def show_test_page():

    return render_template("base.html")
