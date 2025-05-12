# Función principal que determinará si una frase es palíndromo
def esPalindromo(frase):

    '''Descomentar para probar la resolucion del error
    # Comprobar si la entrada es una cadena de texto
    if not isinstance(frase, str):
        # Si no es un string, lanzamos un error controlado
        raise TypeError("La entrada debe ser una cadena de texto")'''

    # Evitar errores por mayuscula y minusculas
    # Convertimos la frase a minúsculas 
    frase = frase.lower()

    # Quitamos comas y puntos ya que nos puede evitar comprobar la lectura en los dos sentidos
    # Vamos a quedarnos solo con las letras y números de la frase
    frase_limpia = ''.join(filter(str.isalnum, frase))

    # Comparar si la frase limpia es igual a su reverso
    # La función devuelve True si es un palíndromo, False si no lo es
    return frase_limpia == frase_limpia[::-1]  # [::-1] invierte la cadena


# Parte principal del script
if __name__ == "__main__":
    """
    Esta es la sección principal del programa, donde pedimos al usuario que 
    ingrese una frase y luego llamamos a la función esPalindromo para evaluar 
    si esa frase es un palíndromo o no.
    """
    
    # Pedir al usuario que ingrese una frase
    frase_usuario = input("Introduce una frase para verificar si es un palíndromo: ")

    # Llamar a la función esPalindromo y almacenar el resultado
    if esPalindromo(frase_usuario):
        # Si la función devuelve True, imprimimos que la frase es un palíndromo
        print(f"La frase introducida si es un palíndromo.")
    else:
        # Si la función devuelve False, imprimimos que no es un palíndromo
        print(f"La frase introducida no es un palíndromo.")
