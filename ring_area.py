## ***************
# ÁREA DEL ANILLO
# ***************

def run(z: float) -> float:
    # Definir el valor de π (pi)
    pi = 3.141592653589793

    # Calcular el área del anillo
    white_area = pi * (3 * z**2 / 4)

    return white_area  # Retorna el área del anillo

if __name__ == '__main__':
    # Llama a la función run con el radio del círculo exterior como 6 y muestra el resultado
    print(run(6))
