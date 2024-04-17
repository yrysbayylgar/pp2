import pygame
import sys
from datetime import datetime

pygame.init()

screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Mouse Clock")

clock_face = pygame.image.load("mainclock.png")
right_hand = pygame.image.load("rightarm.png")
left_hand = pygame.image.load("leftarm.png")

clock_center_x, clock_center_y = screen_width // 2, screen_height // 2

def rotate_hand(image, angle):
    """Rotate the hand image by the specified angle."""
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=(clock_center_x, clock_center_y))
    return rotated_image, rotated_rect

def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        now = datetime.now()
        seconds_angle = -(now.second + now.microsecond / 1000000) * 6 
        minutes_angle = -(now.minute + now.second / 60) * 6  

        rotated_right_hand, right_hand_rect = rotate_hand(right_hand, minutes_angle)
        rotated_left_hand, left_hand_rect = rotate_hand(left_hand, seconds_angle)

        screen.fill((255, 255, 255))
        screen.blit(clock_face, (screen_width // 2 - clock_face.get_width() // 2, screen_height // 2 - clock_face.get_height() // 2))
        screen.blit(rotated_right_hand, right_hand_rect)
        screen.blit(rotated_left_hand, left_hand_rect)

        pygame.display.flip()
        clock.tick(60) 

if __name__ == "__main__":
    main()
