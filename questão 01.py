numeroUm = int(input("Digite o primeiro número: "))
numeroDois = int(input("Digite o segundo número: "))
numeroTres = int(input("Digite o terceiro número: "))

if numeroUm > numeroDois and numeroUm > numeroTres:
    print ("O maior número é: " + str(numeroUm))

if numeroDois > numeroUm and numeroDois > numeroTres:
    print ("O maior número é: " + str(numeroDois))

if numeroTres > numeroUm and numeroTres > numeroDois:
    print ("O maior número é: " + str(numeroTres))
