import sys
import os

# Adiciona o caminho do diretório pai (ativ1) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Module.functions as f
from prettytable import PrettyTable


try:
    print("\tCalculo do Metodo da Bissecção\t\n")
    func = str(input("Função f(x) = "))
    f.is_valid(func)
    print("\nConsiderando o intervalo [a, b]")
    a = float(input("Digite o valor de a = "))
    b = float(input("Digite o valor de b = "))
    e = float(input("Digite o nível de erro = "))
    n = int(input("Número máximo de interações = "))

    table = PrettyTable()
    table.field_names = ["i", "a", "b", "f(a)", "f(b)", "x", "f(x)"]

    i = 0
    fa = f.resolve(func, a)
    while i < n:

        x = a + (b-a)/2
        fx = f.resolve(func, x)
        fb = f.resolve(func, b)

        table.add_row([i, a, b, fa, fb, x, fx])
        
        if fx == 0 or (b-a)/2 < e:
            print(table)
            print(f'\n\nResultado apos {i+1} interações: {x}\n')
            exit()
        i = i + 1
        if fa*fx > 0:
            a = x
            fa = fx
        else:
            b = x

    print(f"O método falhou após {n} interações")
except (ValueError):
    print("Error")

    