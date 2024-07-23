from sympy import sympify, SympifyError, symbols, evalf

def is_valid(function):
    try:
        sympify(function)
    except SympifyError:
        raise ValueError
    
def resolve(function, value):
    x = symbols('x')
    func = sympify(function)
    result = func.subs(x, value).evalf()
    return result