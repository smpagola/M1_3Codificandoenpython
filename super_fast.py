# **********************
# ANIMALES SUPER RÁPIDOS
# **********************

def run(speed_km_h: float) -> float:
    # Calcula la velocidad en cm/s usando la fórmula
    speed_cm_s = speed_km_h * (100000 / 3600)
    return speed_cm_s  # Retorna la velocidad convertida

if __name__ == '__main__':
    # Llama a la función run con una velocidad de 1.08 km/h y muestra el resultado
    print(run(1.08))
