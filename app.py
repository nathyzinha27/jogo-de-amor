from flask import Flask, render_template, request, redirect, url_for, session
from data import fases

app = Flask(__name__)
app.secret_key = "amor_secreto"

@app.route("/", methods=["GET", "POST"])
def index():
    if "fase" not in session:
        session["fase"] = 0

    fase_atual = session["fase"]

    if request.method == "POST":
        session["fase"] += 1
        if session["fase"] >= len(fases):
            return redirect(url_for("pedido"))
        return redirect(url_for("index"))

    return render_template("index.html", fase=fases[fase_atual])

@app.route("/pedido")
def pedido():
    return render_template("pedido.html")

@app.route("/resposta", methods=["POST"])
def resposta():
    escolha = request.form.get("escolha")
    if escolha == "sim":
        return render_template("sim.html")
    return render_template("nao.html")

if __name__ == "__main__":
    app.run()

