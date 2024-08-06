# *****************
# INTERÉS COMPUESTO
# *****************


def run(amount: float, rate: float, years: int) -> float:
    # TU CÓDIGO AQUÍ
    future_amount = amount * (1 + rate / 100) ** years
    return future_amount  # Retorna el monto futuro calculado


if __name__ == '__main__':
    run(10000, 3.5, 7)