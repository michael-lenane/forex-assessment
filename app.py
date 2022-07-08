from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates
from forex_python.converter import Decimal


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/convert")
def show_test_page():

    currencies = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD",
                  "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]

    currency_codes = CurrencyCodes()

    return render_template("base.html", currencies=currencies, currency_codes=currency_codes)


@app.route("/convert", methods=["POST"])
def show_conversion_page():

    currencies = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD",
                  "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]

    currency_codes = CurrencyCodes()
    currency_rates = CurrencyRates()
    convert_start = request.form["start"]
    convert_end = request.form["end"]
    convert_amount = request.form["amount"]
    amount = Decimal(convert_amount)

    return render_template("conversion.html", currencies=currencies, currency_codes=currency_codes, convert_start=convert_start, convert_end=convert_end, amount=amount, currency_rates=currency_rates)
