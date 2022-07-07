from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyCodes
from forex_python.converter import CurrencyRates


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)


currency_rates = CurrencyRates()


@app.route("/convert")
def show_test_page():

    currencies = ["EUR", "IDR", "BGN", "ILS", "GBP", "DKK", "CAD", "JPY", "HUF", "RON", "MYR", "SEK", "SGD", "HKD", "AUD",
                  "CHF", "KRW", "CNY", "TRY", "HRK", "NZD", "THB", "USD", "NOK", "RUB", "INR", "MXN", "CZK", "BRL", "PLN", "PHP", "ZAR"]

    currency_codes = CurrencyCodes()

    global currency_value
    currency_value = request.form.get('start')

    return render_template("convert.html", currencies=currencies, currency_codes=currency_codes, currency_value=currency_value)
