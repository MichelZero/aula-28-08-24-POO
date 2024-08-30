#
# autor: Michel
# data: 28-08-2024

# importar a classe Calculadora
# veja que o import é feito a partir do pacote (diretório) aula
from aula.calculadora import Calculadora # importa a classe Calculadora do arquivo calculadora.py

# instancia a classe Calculadora e atribui a variável c1
c1 = Calculadora()

c1.valor1 = 2 # atribui 2 ao atributo valor1 do objeto c1
c1.valor2 = 3
soma = c1.valor1 + c1.valor2 # soma os atributos valor1 e valor2 do objeto c1 
print(f"{c1.valor1}+{c1.valor2}={soma}") # imprime a soma dos atributos valor1 e valor2 do objeto c1

c1.somar() # chama o método somar do objeto c1 que imprime a soma dos atributos valor1 e valor2 do objeto c1