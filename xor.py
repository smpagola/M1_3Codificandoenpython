## ***
# XOR
# ***

def run(v1: bool, v2: bool) -> bool:
    # Realiza la operación XOR
    xor = v1 ^ v2
    return xor  # Retorna el resultado de la operación XOR

if __name__ == '__main__':
    # Llama a la función run con los valores False y False y muestra el resultado
    print(run(False, False))  # False
    print(run(False, True))   # True
    print(run(True, False))   # True
    print(run(True, True))    # False
