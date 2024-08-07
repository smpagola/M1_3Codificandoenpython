# ******************
# DISTANCIA EUCLÍDEA
# ******************

def run(x1: float, y1: float, x2: float, y2: float) -> float:
    # Calcula la distancia euclídea usando la fórmula
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance  # Retorna la distancia calculada

if __name__ == '__main__':
    # Llama a la función run con los puntos (3, 5) y (-7, -4) y muestra el resultado
    print(run(3, 5, -7, -4))