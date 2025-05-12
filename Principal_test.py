#Importamos la Libreria de texto
import unittest
#importamos la funcion dedes charfu.py
from charfun import esPalindromo

#Creamos la clase tipo unittest
class Testeopalindromo(unittest.TestCase):
    ## Definimos las pruebas
    ## primero que da ok si es un palindromo
    def test_palindromook(correcto):
        correcto.assertTrue(esPalindromo("Anita lava la tina"))

    ## Test si no es palindromo 
    def test_nopalindromo(incorrecto):
        incorrecto.assertFalse(esPalindromo("Anita no lava la tina"))

    #Test si contiene espacios y signos de puntuacion.
    def test_palindromosimbolos(simbolos):
        simbolos.assertTrue(esPalindromo("Anita,,,,lava la tina"))

    #Test si meten una cadena vacia
    def test_cadenavacia(vacia):
        vacia.assertTrue(esPalindromo(""))

    #Test si solo se mete un caracter.
    def test_unasolaletra(solo1):
        solo1.assertTrue(esPalindromo("a"))
        solo1.assertTrue(esPalindromo("Z"))

    #Test si funciona con numeros.
    def test_numerospalindromos(num):
        num.assertTrue(esPalindromo("12321"))
        num.assertFalse(esPalindromo("12345"))

    #Test caracteres especiales
    def test_caracteresespeciales(espe):
        espe.assertTrue(esPalindromo("Anita lava la tina@"))
        espe.assertFalse(esPalindromo("Anita lava la tin@"))

    #Test si no se mete una cadena de texto valida.
    #El número como entero no es válido ya que nova entre ""
    def test_valornostring(nostr):
        
        with nostr.assertRaises(TypeError):
            esPalindromo(12345)

if __name__ == "__main__":
    unittest.main()
