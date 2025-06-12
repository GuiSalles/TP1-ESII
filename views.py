from flask import render_template, request
from main import app

@app.route("/", methods=["GET", "POST"])
def homepage():
    imc = None
    classificacao = None
    nome = ""
    idade = ""
    sexo = ""

    if request.method == "POST":
        try:
            nome = request.form.get("nome", "")
            idade = request.form.get("idade", "")
            sexo = request.form.get("sexo", "")
            peso = float(request.form.get("peso", 0))
            altura = float(request.form.get("altura", 0))

            imc = round(peso / (altura ** 2), 2)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 24.9:
                classificacao = "Peso normal"
            elif imc < 29.9:
                classificacao = "Sobrepeso"
            elif imc < 34.9:
                classificacao = "Obesidade grau I"
            elif imc < 39.9:
                classificacao = "Obesidade grau II"
            else:
                classificacao = "Obesidade grau III"

        except Exception as e:
            classificacao = f"Erro ao processar os dados: {e}"

    return render_template(
        "homepage.html",
        imc=imc,
        classificacao=classificacao,
        nome=nome,
        idade=idade,
        sexo=sexo
    )