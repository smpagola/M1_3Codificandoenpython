# **************************
# BUSCANDO EL SIGLO ADECUADO
# **************************

def run(year: int) -> int:
    # Calcula el siglo al que pertenece el año
    century = (year // 100) + 1 if year % 100 != 0 else year // 100
    return century  # Retorna el siglo calculado

if __name__ == '__main__':
    # Llama a la función run con el año 1705 y muestra el resultado
    print(run(1705))
