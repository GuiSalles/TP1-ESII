def calcular_imc(peso, altura):
    if altura <= 0 or peso <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")
    if not 0.5 <= altura <= 2.5:
        raise ValueError("Altura fora do intervalo esperado. Use metros (ex: 1.70).")
    return round(peso / (altura ** 2), 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Peso normal"
    elif imc <= 29.9:
        return "Sobrepeso"
    elif imc <= 34.9:
        return "Obesidade grau I"
    elif imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
