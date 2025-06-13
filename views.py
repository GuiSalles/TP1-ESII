from flask import render_template, request
from datetime import datetime
from main import app
from imc_utils import calcular_imc, classificar_imc
from database_manager import inserir_avaliacao, buscar_historico

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
            nome = request.form.get("nome", "").strip().title()
            idade = request.form.get("idade", "").strip()
            sexo = request.form.get("sexo", "")
            peso = float(request.form.get("peso", 0))
            altura = float(request.form.get("altura", 0))

            imc = calcular_imc(peso, altura)
            classificacao = classificar_imc(imc)

            # Salvar no banco
            inserir_avaliacao({
                "nome": nome,
                "idade": idade,
                "sexo": sexo,
                "peso": peso,
                "altura": altura,
                "imc": imc,
                "classificacao": classificacao,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

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


@app.route("/perfil")
def perfil():
    nome = request.args.get("nome", "").strip().title()
    registros = buscar_historico(nome)

    return render_template(
        "perfil.html",
        nome=nome,
        historico=registros
    )