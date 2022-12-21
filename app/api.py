from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    isUsed = RejestrKont.find_account(dane["pesel"])
    if isUsed:
        return jsonify("Konto juz istnieje"), 400
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["name"], dane["lastname"], dane["pesel"])
    RejestrKont.add_account(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print("Request o liczbe kont")
    return jsonify(RejestrKont.count_accounts()), 200 

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel: str):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont.find_account(pesel)
    print(konto)
    if konto:
        return jsonify(name=konto.name, lastname=konto.lastname, pesel=konto.pesel, balance=konto.balance), 200
    return jsonify("Nie znaleziono konta"), 404

@app.route("/konta/update_konto/<pesel>", methods=['PUT'])
def update_konto(pesel: str):
    dane = request.get_json()
    print(f"Request o update konta z danymi: {dane}")
    konto = RejestrKont.find_account(pesel)
    if konto:
        if "name" in dane:
            konto.name = dane["name"]
        if "lastname" in dane:
            konto.lastname = dane["lastname"]
        if "pesel" in dane:
            konto.pesel = dane["pesel"]
        if "balance" in dane:
            konto.balance = dane["balance"]
        return jsonify("Konto zaktualizowane"), 200
    else:
        return jsonify("Nie znaleziono konta"), 404

@app.route("/konta/delete_konto/<pesel>", methods=['DELETE'])
def delete_konto(pesel: str):
    print(f"Request o usuniecie konta z peselem: {pesel}")
    konto = RejestrKont.find_account(pesel)
    if konto:
        RejestrKont.accounts.remove(konto)
        return jsonify("Konto usuniete"), 200
    return jsonify("Nie znaleziono konta"), 404
