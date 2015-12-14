# -*- coding: utf-8 -*-
import unittest
import desafio


class TestaNaturaisMenoresQue101(unittest.TestCase):

    def test_retorna_naturais_menores_que_101_nao_nulo(self):
        with self.assertRaises(ValueError):
            desafio.retorna_naturais_menores_que_101(None)

    def test_retorna_naturais_menores_que_101_nao_negativo(self):
        with self.assertRaises(ValueError):
            desafio.retorna_naturais_menores_que_101(-10)

    def test_retorna_naturais_menores_que_101_eh_tupla(self):
        self.assertIsInstance(
            desafio.retorna_naturais_menores_que_101(3), tuple)

    def test_cria_tupla_nao_monotonica(self):
        self.assertEquals(
            desafio.cria_tupla_nao_monotonica(
                [1, 2, 3, 4, 5]), (1, 3, 2, 5, 4))
        self.assertEquals(
            desafio.cria_tupla_nao_monotonica(
                [5, 4, 3, 2, 1]), (5, 3, 4, 1, 2))


class TestaTuplaMonotonica(unittest.TestCase):

    def test_retorna_tupla_monotonica(self):
        self.assertEquals(
            desafio.retorna_tupla_monotonica(
                (1, 3, 2, 5, 4)), (1, 2, 3, 4, 5))

    def test_retorna_tupla_monotonica_input_erro(self):
        with self.assertRaises(ValueError):
            desafio.retorna_tupla_monotonica(None)
        with self.assertRaises(ValueError):
            desafio.retorna_tupla_monotonica([1, 2, 3])
        with self.assertRaises(ValueError):
            desafio.retorna_tupla_monotonica(())


class TestaIndiceDaTupla(unittest.TestCase):

    def test_retorna_indice_da_tupla_input_erro(self):
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla(None, 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla([1, 2, 3], 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla((), 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla((1, -2), 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla((1, 2), -1)

    def test_retorna_indice_da_tupla_menos_1(self):
        self.assertEquals(-1, desafio.retorna_indice_da_tupla((1, 2, 3, 4), 5))

    def test_retorna_indice_da_tupla_com_elemento(self):
        self.assertEquals(2, desafio.retorna_indice_da_tupla((1, 2, 3, 4), 3))


class TestaIndiceDaTuplaSimples(unittest.TestCase):

    def test_retorna_indice_da_tupla_input_erro(self):
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla_simples(None, 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla_simples([1, 2, 3], 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla_simples((), 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla_simples((1, -2), 1)
        with self.assertRaises(ValueError):
            desafio.retorna_indice_da_tupla_simples((1, 2), -1)

    def test_retorna_indice_da_tupla_menos_1(self):
        self.assertEquals(
            -1, desafio.retorna_indice_da_tupla_simples((1, 2, 3, 4), 5))

    def test_retorna_indice_da_tupla_com_elemento(self):
        self.assertEquals(
            2, desafio.retorna_indice_da_tupla_simples((1, 2, 3, 4), 3))


class TestaCalculaTempo(unittest.TestCase):

    def calcula_tempo_indice_da_tupla(self):
        simples = desafio.calcula_tempo_indice_da_tupla_simples(
            (1, 2, 3, 4), 5)
        normal = desafio.calcula_tempo_indice_da_tupla(
            (1, 2, 3, 4), 5)
        self.assertGreater(simples, normal)


unittest.main()
