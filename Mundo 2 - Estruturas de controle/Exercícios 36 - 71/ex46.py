"""Exercício Python 046: Contagem Regressiva"""
from time import sleep
import emoji

for i in range(10,-1, -1):
    print(i)
    sleep(1)
print()
print("BOOM", emoji.emojize(":fireworks:"))
