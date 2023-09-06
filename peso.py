def kilogramos_a_gramos(kilogramos):
    formula = kilogramos * 1000
    return f"Resultado: {formula} gramos"

def gramos_a_kilogramos(gramos):
    formula = gramos * 0.001
    return f"Resultado: {formula}  kilogramos"

if __name__ == '__main__':
    #ejemplo de uso de las dos funciones
    kilogramos= 80
    gramos = 3600
    print(kilogramos_a_gramos(kilogramos))
    print(gramos_a_kilogramos(gramos))