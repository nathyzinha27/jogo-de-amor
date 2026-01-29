from flask import Flask, session, request, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = "chave-secreta-super-romantica"

# Todas as fases, incluindo a última sobre aliança
fases = [
    {"texto": "Antes de tudo começar…", "pergunta": "O que você sentiu quando me viu pela primeira vez?"},
    {"texto": "Nem tudo começou com certeza.", "pergunta": "O que te fez querer continuar falando comigo?"},
    {"texto": "Com o tempo, algo mudou.", "pergunta": "Quando você percebeu que eu já fazia falta?"},
    {"texto": "Existiram dúvidas.", "pergunta": "Mesmo assim, por que você escolheu ficar?"},
    {"texto": "O amor não é perfeito.", "pergunta": "O que faz nosso relacionamento valer a pena?"},
    {"texto": "Eu nem sempre demonstro tudo.", "pergunta": "Mas o que te faz saber que eu te amo?"},
    {"texto": "Às vezes eu me fecho.", "pergunta": "O que você acha que passa na minha cabeça nesses momentos?"},
    {"texto": "O tempo passou rápido.", "pergunta": "Qual momento nosso você nunca esqueceria?"},
    {"texto": "Entre tantas pessoas no mundo…", "pergunta": "Por que você acha que eu escolhi você?"},
    {"texto": "Amar também é confiar.", "pergunta": "O que faz você se sentir segura comigo?"},
    {"texto": "Nem todos os dias são leves.", "pergunta": "O que te faz continuar acreditando na gente?"},
    {"texto": "O amor mora nos detalhes.", "pergunta": "Qual detalhe meu te faz sorrir?"},
    {"texto": "Quando penso em você…", "pergunta": "O que você acha que eu sinto?"},
    {"texto": "Pensar no futuro dá medo.", "pergunta": "Mas como você imagina a gente daqui a alguns anos?"},
    {"texto": "Se tudo acabasse hoje…", "pergunta": "O que você levaria da nossa história?"},
    {"texto": "Entre erros e acertos…", "pergunta": "O que você acha que aprendemos juntos?"},
    {"texto": "O amor também é escolha.", "pergunta": "Por que você escolheria ficar comigo todos os dias?"},
    {"texto": "Depois de tudo isso…", "pergunta": "Você sente que esse amor é real?"},
    {"texto": "E para selar tudo…", "pergunta": "Você gostaria de usar uma aliança como símbolo do nosso amor?"}
]

@app.route("/", methods=["GET", "POST"])
def index():
    # Inicializa fase na sessão
    if "fase" not in session:
        session["fase"] = 0

    # Lida com o clique no botão Próxima
    if request.method == "POST":
        # Avança para a próxima fase
        session["fase"] += 1

        # Se passou do total de fases, vai para pedido
        if session["fase"] >= len(fases):
            return redirect(url_for("pedido"))

        # Redireciona para evitar reenvio de POST
        return redirect(url_for("index"))

    # Garante que a fase atual está dentro do intervalo
    fase_atual = session.get("fase", 0)
    if fase_atual >= len(fases):
        return redirect(url_for("pedido"))

    # Passa a fase atual para o template
    fase = fases[fase_atual]

    return render_template("index.html", fase=fase)

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
    app.run(debug=True)
