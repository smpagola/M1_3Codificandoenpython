# *******************
# TIRO PORQUE ME TOCA
# *******************

def run(current_pos: int, dice: int) -> int:
    # Calcula la nueva posición sumando la posición actual con el valor del dado
    final_pos = current_pos + dice
    return final_pos  # Retorna la nueva posición

if __name__ == '__main__':
    # Llama a la función run con la posición actual 3 y un dado de valor 6, y muestra el resultado
    print(run(3, 6))
