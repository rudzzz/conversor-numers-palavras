print("-----Conversor de números em palavras-----")
numeros = input("Numero: ")
digitos = {
    "0": "Zero",
    "1": "Um",
    "2": "Dois",
    "3": "Três",
    "4": "Quatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Sete",
    "8": "Oito",
    "9": "Nove"
}
mensagem = ""

for numero in numeros:
    mensagem += digitos.get(numero, "Comando inválido!") + ", "
print(mensagem)