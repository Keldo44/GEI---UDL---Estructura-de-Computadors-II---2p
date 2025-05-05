def convertir_letra(letra):
    if len(letra) != 1:
        raise ValueError("Debes ingresar solo una letra.")

    ascii_val = ord(letra)  # Valor ASCII (8 bits)
    binario_bajo = format(ascii_val, '08b')  # A binario con 8 bits
    binario_completo = '00000111' + binario_bajo  # Añadir byte alto
    valor_final = int(binario_completo, 2)  # A entero
    hex_final = format(valor_final, '04X')  # A hex de 4 cifras, mayúsculas

    return f"{hex_final}h"

# Ejemplo de uso

frase = input("Introduce una frase: ")

resultado = frase+" VALOR " 
for letra in frase:
    try:
        resultado += convertir_letra(letra)+", "
    except ValueError as e:
        resultado = "Tenias que hacer algo mal, un trabajo tenias...  "
# remove two last chars
resultado = resultado[:-2]
print(resultado)





