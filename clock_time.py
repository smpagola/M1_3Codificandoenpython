# *********************
# CONTANDO MILISEGUNDOS
# *********************

def run(hours: int, minutes: int, seconds: int) -> float:
    # Convertir horas a milisegundos
    milliseconds_hours = hours * 60 * 60 * 1000

    # Convertir minutos a milisegundos
    milliseconds_minutes = minutes * 60 * 1000

    # Convertir segundos a milisegundos
    milliseconds_seconds = seconds * 1000

    # Sumar todos los milisegundos
    time_since_midnight = milliseconds_hours + milliseconds_minutes + milliseconds_seconds

    return time_since_midnight  # Retorna el tiempo total en milisegundos


if __name__ == '__main__':
    # Llama a la función run con 0 horas, 1 minuto y 1 segundo, y muestra el resultado
    print(run(0, 1, 1))
