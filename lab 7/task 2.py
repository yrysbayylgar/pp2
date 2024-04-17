import pygame
import time

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lab7-2")

song1 = "C:\\Users\\wpgg3\\OneDrive\\Рабочий стол\\KBTU\\pp2\\Lab7\\music\\Don Toliver - Way Bigger.mp3"
song2 = "C:\\Users\\wpgg3\\OneDrive\\Рабочий стол\\KBTU\\pp2\\Lab7\\music\\Lambo4oe_SELF_ESTEEM.mp3"

pygame.mixer.init()

pygame.mixer.music.load(song1)
pygame.mixer.music.set_volume(0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:
                pygame.mixer.music.load(song2)
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                pygame.mixer.music.load(song1)
                pygame.mixer.music.play()

    pygame.display.flip()

pygame.quit()
