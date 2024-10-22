from flask import Flask, render_template, request
import requests

API_KEY = "38df67baaaaebb696644f0c8"


def get_exchange_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{from_currency}/{to_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["conversion_rate"]
    return None


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    from_currency = request.form["from_currency"]
    to_currency = request.form["to_currency"]
    amount = float(request.form["amount"])

    rate = get_exchange_rate(from_currency, to_currency)

    if rate:
        converted_amount = amount * rate
        return f"{amount} {from_currency} est égal à {converted_amount:.2f} {to_currency} au taux de {rate}."
    return "Erreur lors de la récupération du taux de change."


if __name__ == "__main__":
    app.run(debug=True)
