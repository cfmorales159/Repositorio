from decimal import Decimal
suma_float = 0.0
for _ in range(10):
    suma_float += 0.1
print(f"Redultado con float: {suma_float}")
suma_decimal = Decimal('0.0')
for _ in range(10):
    suma_decimal += Decimal('0.1')
print (f"Resultado con Decimal: {suma_decimal}")