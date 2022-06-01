from unittest import TestCase, main
from Palindromo import Palindromo
import string
import random

def random_string(length):
    str= ''.join( random.SystemRandom().choice(string.ascii_latters + string.digits) for _ in range(length))
    return str + ''.join(reversed(str))

    print(random_string(10))

class TestPalindromo(TestCase):
    __palindromo: Palindromo

    def setUp(self) -> None:
        self.__palindromo= Palindromo('')
    
    def test_palindr_vacio(self):
        self.assertTrue(self.__palindromo.esPalindromo())
    
    def test_palindromo_un_caractere(self):
        self.__palindromo.setPalabra('a')
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo_dos_caracteres(self):
        self.__palindromo.setPalabra('aa')
        self.assertTrue(self.__palindromo.esPalindromo())
        
    def test_palindromo_tres_caracteres(self):
        self.__palindromo.setPalabra('aaa')
        self.assertTrue(self.__palindromo.esPalindromo())
    
    def test_palindromo_cuatro_caracteres(self):
        self.__palindromo.setPalabra('aaaa')
        self.assertTrue(self.__palindromo.esPalindromo())
    
    def generarPalindromo(self, palabra):
        self.__palindromo.setPalabra(palabra)
        return self.__palindromo.esPalindromo()
    
if __name__=='__main__':
    main()
    