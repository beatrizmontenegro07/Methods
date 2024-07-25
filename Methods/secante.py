import sys
import os

# Adiciona o caminho do diretório pai (ativ1) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Module.functions as f
from prettytable import PrettyTable

# Define a formula da Secante
def formula(function, x0, x1):
    f_x1 = f.resolve(function, x1)
    f_x0 = f.resolve(function, x0)
    valor1 = (x0 * f_x1) - (x1 * f_x0)
    valor2 = f_x1 - f_x0
    return (valor1/valor2)

# Método da Secante com formula numérica
def metodoSecante(function, x0, x1, precisao, max):
    table = PrettyTable()
    table.field_names = ["n", "x0", "x1", "f(x0)", "f(x1)", "x2", "f(x2)"]
    for n in range(max):
        #Checando se esta chegando a zero
        if abs(f.resolve(function, x1) - f.resolve(function, x0)) < precisao:
            print("Valor beirando a divisao por zero")
            return None
        
        f_x1 = f.resolve(function, x1)
        f_x0 = f.resolve(function, x0)
        
        #Usando a formula da Secante
        x2 = formula(function, x0, x1)
        f_x2 = f.resolve(function, x2)

        table.add_row([n, x0, x1, f_x0, f_x1, x2, f_x2])

        #Checando se chegou no resultado
        if abs(x2-x1) < precisao:
            print(table)
            print(f"Convergiu para {x2} após {n+1} iterações.")
            return x2
        else:
            x0 = x1 #Atualizando os valores
            x1 = x2
    
    print("Número máximo de iterações atingido. Método da Secante falhou.")
    return None

#Codigo Principal
try: 
    print("\tCalculo do Metodo da Secante\t\n")

    func = str(input("Function f(x) = "))
    f.is_valid(func)
    x0 = float(input("Digite o valor x0: "))
    x1 = float(input("Digite o valor x1: "))
    erro = float(input("Digite o nivel do erro: "))
    n = int(input("Digite o número máximo de interações: "))

    raiz = metodoSecante(func, x0, x1, erro, n)

    print(f"A raiz encontrada é: {raiz}\n")
except ValueError:
    print("Erro! Verifique se os valores digitados na entrada estão corretos")
finally:
    print("Fim de programa")