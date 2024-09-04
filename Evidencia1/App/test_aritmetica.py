
from aritmetica import *
from random import *

def test_suma():
    assert sumar(-1.35, 1.36) == 0.01
    print("Validación 1 sumar() - OK")
    assert sumar(2.52 , 2.52) == 5.04
    print("Validación 2 sumar() - OK")
    assert sumar(3.31 , 3.71) == 7.02
    print("Validación 3 sumar() - OK")

def test_restar():
    assert restar(2.35, 1.34) == 1.01
    print("Validación 1 restar() - OK")
    assert restar(2.52 , 2.52) == 0.00
    print("Validación 2 restar() - OK")
    assert restar(3.31 , 3.71) == -0.40
    print("Validación 3 restar() - OK")


def test_multiplicar():
    assert multiplicar(2.00,2.00) == 4.00
    print("Validación 1 multiplicar() - OK")
    assert multiplicar(-2.00,-2.00) == 4.00
    print("Validación 2 multiplicar() - OK")
    assert multiplicar(-2.00,5.25) == -10.50
    print("Validación 3 multiplicar() - OK")

def test_dividir():
    assert dividir (2.25 , 1.00) == 2.25
    print("Validación 1 dividir() - OK")
    assert dividir (2.25 , 2.25) == 1.00
    print("Validación 2 dividir() - OK")
    assert dividir (5.25 , 5.00) == 1.05
    print("Validación 3 dividir() - OK")

def test_sumar_n():
    assert round(sumar_n(1,2,3,4,5), 2) == 15.00
    print("Validación 1 sumar_n() - OK")
    assert round(sumar_n(1,3,5,7,9,10), 2) == 35.00
    print("Validación 2 sumar_n() - OK")
    assert round(sumar_n(1,2,3,4,5,1,2,3,4,5), 2) == 30.00
    print("Validación 3 sumar_n() - OK")

def test_promedio_n():
    assert promedio_n(1.52 , 1.52) == 1.52
    print("Validación 1 promedio_n() - OK")
    assert promedio_n(1.52 , 1.52 , 1.52 , 1.52) == 1.52
    print("Validación 2 promedio_n() - OK")
    assert promedio_n(1.52 , 1.52 , 1.52 , 1.52 , 1.52 , 1.52) == 1.52
    print("Validación 3 promedio_n() - OK")



if __name__ == "__main__": 
    test_suma()
    test_restar()
    test_multiplicar()
    test_dividir()
    test_sumar_n()
    test_promedio_n()
