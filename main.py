#
# autor: Michel
# data: 28-08-2024

# importar a classe Calculadora
from aula.calculadora import Calculadora

# instancia
c1 = Calculadora()

c1.valor1 = 2
c1.valor2 = 3
soma = c1.valor1 + c1.valor2
print(f"{c1.valor1}+{c1.valor2}={soma}")

c1.somar()