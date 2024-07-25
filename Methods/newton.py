import sys
import os

# Adiciona o caminho do diretório pai (ativ1) ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import Module.functions as f
from prettytable import PrettyTable


# Define a derivada numérica
def derivada(function, x, h=1e-5):
    return (f.resolve(function, x + h) - f.resolve(function, x))/ h

# Método de Newton com derivada numérica
def metodoNewton(function, x0, precisao, max):
    table = PrettyTable()
    table.field_names = ["n", "x_n", "f(x_n)", "f'(x_n)"]
    x_n = x0
    for n in range(max):
        f_x_n = f.resolve(function, x_n)
        f_prime_x_n = derivada(function, x_n)

        table.add_row([n, x_n, f_x_n, f_prime_x_n])
        
        if abs(f_x_n) < precisao:
            print(table)
            print(f"Convergiu para {x_n} após {n+1} iterações.")
            return x_n
        
        if f_prime_x_n == 0:
            print("Derivada zero. Método de Newton falhou.")
            return None
        
        x_n = x_n - f_x_n / f_prime_x_n
    
    print("Número máximo de iterações atingido. Método de Newton falhou.")
    return None

#Codigo Principal
print("\tCalculo do Metodo de Newton\t\n")

try: 
    func = str(input("Function f(x) = "))
    f.is_valid(func)
    x0 = float(input("Digite o valor inicial: "))
    e = float(input("precisão = "))
    n = int(input("Número máximo de interações = "))

    raiz = metodoNewton(func, x0, e, n)
    print(f"A raiz encontrada é: {raiz}")
except ValueError:
    print("Erro! Verifique se os valores digitados na entrada estão corretos")
finally:
    print("Fim de programa")