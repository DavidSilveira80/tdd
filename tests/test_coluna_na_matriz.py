"""Teste do programa coluna_na_matriz. Uri-1182"""
from coluna_na_matriz import coluna_na_matriz
from unittest import TestCase


class tests_coluna_na_matriz(TestCase):
    def test_soma_coluna_5(self):
        """5 é a coluna a ser calculada S(soma) é o tipo cálculo 78.0 é o resultado esperado """
        self.assertEqual(coluna_na_matriz(5, 'S'), 'A soma da coluna 5 da matriz é: 78.0')

    def test_media_coluna_5(self):
        self.assertEqual(coluna_na_matriz(5, 'M'), 'A média da coluna 5 da matriz é: 6.5')
