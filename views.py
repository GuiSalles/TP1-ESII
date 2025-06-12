from flask import render_template, request
from main import app
from imc_utils import calcular_imc, classificar_imc

@app.route("/", methods=["GET", "POST"])
def homepage():
    imc = None
    classificacao = None
    nome = ""
    idade = ""
    sexo = ""
    erro = None

    if request.method == "POST":
        try:
            nome = request.form.get("nome", "").strip()
            idade = request.form.get("idade", "").strip()
            sexo = request.form.get("sexo", "")
            peso = float(request.form.get("peso", 0))
            altura = float(request.form.get("altura", 0))

            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)

        except Exception as e:
            erro = str(e)

    return render_template(
        "homepage.html",
        imc=imc,
        classificacao=classificacao,
        nome=nome,
        idade=idade,
        sexo=sexo,
        erro=erro
    )
