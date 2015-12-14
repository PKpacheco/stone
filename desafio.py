# -*- coding: utf-8 -*-
from timeit import default_timer as timer
from random import randint


def retorna_naturais_menores_que_101(n):
    numbers = []
    count = 0
    if n is None or n < 0:
        raise ValueError
    while count < n:
        number = randint(0, 101)
        if number not in numbers:
            numbers.append(number)
            count += 1
    return cria_tupla_nao_monotonica(numbers)


def retorna_tupla_monotonica(tupla):
    if tupla is None or len(tupla) <= 0 or type(tupla) != tuple:
        raise ValueError
    lista = list(tupla)
    return tuple(sorted(lista))


def calcula_tempo_indice_da_tupla(tupla, s):
    start = timer()
    retorna_indice_da_tupla(tupla, s)
    end = timer()
    print end - start
    return end - start


def calcula_tempo_indice_da_tupla_simples(tupla, s):
    start = timer()
    retorna_indice_da_tupla_simples(tupla, s)
    end = timer()
    print end - start
    return end - start


def retorna_indice_da_tupla(tupla, s):
    if tupla is None or len(tupla) <= 0 or type(tupla) != tuple:
        raise ValueError
    if True in map(lambda x: x < 0, tupla) or s < 0:
        raise ValueError
    if s not in tupla:
        return -1
    return tupla.index(s)


def retorna_indice_da_tupla_simples(tupla, s):
    if tupla is None or len(tupla) <= 0 or type(tupla) != tuple:
        raise ValueError
    if s < 0:
        raise ValueError
    for t in tupla:
        if t < 0:
            raise ValueError
    for i, v in enumerate(tupla):
        if v == s:
            return i
    return -1


def cria_tupla_nao_monotonica(lista):
    nao_monotonica = []
    old = 0
    seq_mono = 0
    for i, l in enumerate(lista):
        if l - old != seq_mono:
            nao_monotonica.append(l)
            seq_mono = l - old
        else:
            if i % 2 == 0:
                nao_monotonica.insert(i - 1, l)
            else:
                nao_monotonica.append(l)
        old = l
    return tuple(nao_monotonica)

if __name__ == '__main__':
    print "normal"
    calcula_tempo_indice_da_tupla((1, 2, 3, 4), 5)
    print "simples"
    calcula_tempo_indice_da_tupla_simples((1, 2, 3, 4), 5)
