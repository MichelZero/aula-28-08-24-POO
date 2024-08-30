#
# autor: Michel
# data: 28-08-2024

#Crie uma classe para somar 2 valores.

##### 1 teste ###########
class Calculadora: 
  valor1 = 0 # atributo da classe Calculadora
  valor2 = 0
  
  # def olaMundo(self): # método da classe Calculadora
  #   print("Olá Mundo!")
  
  def somar(self): # método da classe Calculadora
    print(f"{self.valor1}+{self.valor2}={self.valor1 + self.valor2}") # self é uma referência ao objeto que está chamando o método