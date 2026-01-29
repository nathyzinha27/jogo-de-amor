from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "chave-secreta-super-romantica"

fases = [
    "Pergunta 1",
    "Pergunta 2",
    "Pergunta 3"
]

@app.route("/", methods=["GET", "POST"])
def index():

    if "fase" not in session:
        session["fase"] = 0

    if request.method == "POST":
        session["fase"] += 1

        if session["fase"] >= len(fases):
            return redirect(url_for("pedido"))

        return redirect(url_for("index"))

    fase_atual = session["fase"]

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
