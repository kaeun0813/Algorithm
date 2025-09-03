def solution(polynomial):
    x_coef = 0
    const = 0
    
    for term in polynomial.split(" + "):
        if term.endswith("x"):                 
            x_coef += int(term[:-1]) if term[:-1] else 1
        else:                                  
            const += int(term)
    
    if x_coef and const:
        return (("x" if x_coef == 1 else f"{x_coef}x") + f" + {const}")
    elif x_coef:
        return "x" if x_coef == 1 else f"{x_coef}x"
    else:
        return str(const)
