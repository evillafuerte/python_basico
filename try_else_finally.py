#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

print("Vamos dividir dois números inseridos por você\n ")
num1 = raw_input("Digite o primeiro número: ")
num2 = raw_input("Digite o segundo número: ")
try:
    resultado = (int(num1) / int(num2))
    print("O resultado é " + str(resultado))
except ZeroDivisionError:
    print("O segundo número não pode ser zero")
except ValueError:
    print("Você deve entrar apenas com números")
else:
    print("divisao feita!")



