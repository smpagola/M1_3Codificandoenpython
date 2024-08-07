# ****************
# EL CUADRADO ROJO
# ****************

def run(arc_A: float) -> float:
    # Definimos pi manualmente
    pi = 3.141592653589793

    # Calcula el radio del círculo usando el arco dado
    r = arc_A / pi

    # Calcula el área del cuadrado inscrito en el círculo
    area = 2 * (r ** 2)

    return area  # Retorna el área calculada

if __name__ == '__main__':
    # Llama a la función run con el arco de 1 radian y muestra el resultado
    print(run(1))
