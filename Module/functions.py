from sympy import sympify, SympifyError, symbols, evalf


#Analisa se a função de entrada do usuário é válida, se não for lança ValueError
def is_valid(function):
    try:
        sympify(function)
    except SympifyError:
        raise ValueError
    

#Resolve a função f(x) a partirde um valor x, exemplo f(5) 
def resolve(function, value):
    x = symbols('x')
    func = sympify(function)
    result = func.subs(x, value).evalf()
    return result