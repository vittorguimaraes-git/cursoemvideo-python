import pygame

pygame.init()
pygame.mixer.music.load('jk.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
pygame.quit()