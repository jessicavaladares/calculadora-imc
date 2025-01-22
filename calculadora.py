def calcular_imc():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obesidade"

    print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

print("Bem-vindo à Calculadora de IMC!")

while True:
    calcular_imc()
    repetir = input("Deseja calcular outro IMC? (s/n): ")
    if repetir.lower() != 's':
        print("Até logo!")
        break
