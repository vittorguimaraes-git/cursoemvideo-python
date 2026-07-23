from math import cos, sin, tan,radians, degrees

angulo = float(input("Digite um ângulo: "))
rad = radians(angulo)
graus = degrees(angulo)

print(f"O coseno de {angulo} é {round(cos(rad))}" 
      f"\nO seno de {angulo} é {round(sin(rad))}"
      f"\nA tangente de {angulo} é {round(tan(rad))}")

print(f"O coseno de {angulo} em radianos é:  {round(cos(graus))}" 
      f"\nO seno de {angulo} em radianos é: {round(sin(graus))}"
      f"\nA tangente de {angulo} em radianos é: {round(tan(graus))}")
