from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates


app = Flask(__name__)

debug = DebugToolbarExtension(app)
