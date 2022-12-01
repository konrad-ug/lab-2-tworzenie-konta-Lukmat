from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["name"], dane["lastname"], dane["pesel"])
    RejestrKont.add_account(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print("Request o liczbe kont")
    return jsonify(RejestrKont.count_accounts()), 200 

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z pesel: {pesel}")
    konto = RejestrKont.find_account(pesel)
    if konto:
        return jsonify(konto.__dict__), 200
    return jsonify("Account not found"), 404