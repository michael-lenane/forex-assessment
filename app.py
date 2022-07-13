from sre_parse import FLAGS
from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates
from forex_python.converter import Decimal


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/", methods=["POST", "GET"])
def show_test_page():

    currencies = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD",
                  "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]

    common_currencies = ["AUD", "CAD", "CNY", "EUR",
                         "GBP", "INR", "JPY", "MXN"]

    flags = ["class='flag flag-australia'"]

    currency_codes = CurrencyCodes()
    currency_rates = CurrencyRates()
    amount = Decimal(1.00)

    return render_template("base.html", currencies=currencies, currency_codes=currency_codes, common_currencies=common_currencies, currency_rates=currency_rates, amount=amount, flags=flags)


@app.route("/convert", methods=["POST", "GET"])
def show_conversion_page():

    currencies = ["AUD", "BGN", "BRL", "CAD", "CHF", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "HRK", "IDR", "ILS",
                  "INR", "JPY", "KRW", "MYR", "MXN", "NOK", "NZD", "PHP", "PLN", "RON", "RUB", "SEK", "SGD", "THB", "TRY", "USD", "ZAR"]

    common_currencies = ["AUD", "CAD", "CNY", "EUR",
                         "GBP", "INR", "JPY", "MXN"]

    currency_codes = CurrencyCodes()
    currency_rates = CurrencyRates()
    convert_start = request.form["start-choice"]
    convert_end = request.form["end-choice"]
    convert_amount = request.form["amount"]
    amount = Decimal(convert_amount)

    return render_template("conversion.html", currencies=currencies, currency_codes=currency_codes, convert_start=convert_start, convert_end=convert_end, amount=amount, currency_rates=currency_rates, common_currencies=common_currencies)
