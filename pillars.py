# **********************
# POSTES EN LA CARRETERA
# **********************

def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    if num_pillars == 1:
        # Si solo hay un poste, la distancia es 0
        inter_distance = 0
    else:
        # Calcula la distancia total entre los postes
        total_gap_distance = gap_pillars * (num_pillars - 1)

        # Calcula la distancia total ocupada por los postes en metros
        total_pillar_width = (pillar_width * num_pillars) / 100

        # Suma ambas distancias
        inter_distance = total_gap_distance + total_pillar_width

    return inter_distance  # Retorna la distancia total ocupada


if __name__ == '__main__':
    # Llama a la función run con 10 postes, 5 metros de distancia entre postes, y 30 cm de ancho por poste
    print(run(10, 5, 30))
