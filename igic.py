# ***************
# PRECIO SIN IGIC
# ***************

def run(price_with_igic: float, igic: float) -> float:
    # Calcula el precio sin IGIC usando la fórmula
    clean_price = price_with_igic / (1 + igic / 100)
    return clean_price  # Retorna el precio sin IGIC calculado

if __name__ == '__main__':
    # Llama a la función run con el precio de 120 y una tasa de IGIC de 7%
    print(run(120, 7))
