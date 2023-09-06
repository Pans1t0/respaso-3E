def metros_a_pulgadas(metros):
    formula = metros * 39,37
    return f"Resultado: {formula}  pulgadas"


def pulgadas_a_metros(pulgadas):
    formula = pulgadas * 0.0254 
    return f"Resultado: {formula} metros"

if __name__ == '__main__':
    #Si es ejecutada desde este Archivo osea " Longitud.py " se crearan estas dos varibles de datos e imprimira las dos Funciones
    metros= 2
    pulgadas = 10 
    print(metros_a_pulgadas(metros))
    print(pulgadas_a_metros(pulgadas))