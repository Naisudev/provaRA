trabIdade = int(input("Digite sua idade: "))
trabTempo = int(input("Digite seu tempo de trabalho: "))

if trabIdade >= 65:
    print("Você pode se aposentar!")

if trabTempo >= 30:
    print("Você pode se aposentar!")

if trabIdade >= 60 and trabTempo >= 25:
    print("Você pode se aposentar!")