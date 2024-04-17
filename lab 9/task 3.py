import pygame
import math

def draw_rectangle(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    return (x, y, width, height)

def draw_square(x1, y1, x2, y2):
    x = min(x1, x2)
    y = min(y1, y2)
    size = min(abs(x1 - x2), abs(y1 - y2))
    return (x, y, size, size)

def draw_right_triangle(x1, y1, x2, y2):
    x_start = min(x1, x2)
    x_end = max(x1, x2)
    y_start = min(y1, y2)
    y_end = max(y1, y2)
    pygame.draw.line(screen, colors[color_index], (x_start, y_start), (x_start, y_end), 1)
    pygame.draw.line(screen, colors[color_index], (x_start, y_end), (x_end, y_end), 1)
    pygame.draw.line(screen, colors[color_index], (x_end, y_end), (x_start, y_start), 1)

def draw_equilateral_triangle(x1, y1, x2, y2):
    x_start = min(x1, x2)
    y_start = min(y1, y2)
    size = min(abs(x1 - x2), abs(y1 - y2))
    x_end = x_start + size
    y_end = y_start + size
    
    # Calculate the coordinates of the third vertex of the equilateral triangle
    height = size * math.sqrt(3) / 2
    x_mid = (x_start + x_end) // 2
    y_mid = y_start - int(height)
    
    pygame.draw.line(screen, colors[color_index], (x_start, y_start), (x_end, y_start), 1)
    pygame.draw.line(screen, colors[color_index], (x_end, y_start), (x_mid, y_mid), 1)
    pygame.draw.line(screen, colors[color_index], (x_mid, y_mid), (x_start, y_start), 1)

def draw_rhombus(x1, y1, x2, y2):
    x_start = min(x1, x2)
    x_end = max(x1, x2)
    y_start = min(y1, y2)
    y_end = max(y1, y2)
    x_mid = (x_end + x_start) / 2
    y_mid = (y_end + y_start) / 2
    pygame.draw.line(screen, colors[color_index], (x_mid, y_start), (x_end, y_mid), 1)
    pygame.draw.line(screen, colors[color_index], (x_end, y_mid), (x_mid, y_end), 1)
    pygame.draw.line(screen, colors[color_index], (x_mid, y_end), (x_start, y_mid), 1)
    pygame.draw.line(screen, colors[color_index], (x_start, y_mid), (x_mid, y_start), 1)

pygame.init()
screen = pygame.display.set_mode((800, 600))
second_screen = pygame.Surface((800, 600))

done = False
clock = pygame.time.Clock()
fps = 8
start_x = 10
start_y = 10
end_x = 10
end_y = 10
color_index = 0
tool_index = 0
mouse_moving = False

screen.fill((0, 0, 0))

colors = ["Red", "Pink", "Blue", "White", "Green", "Yellow", "Purple"]
tools = ["Rectangle", "Circle", "Square", "Right Triangle", "Equilateral triangle", "Rhombus", "Eraser"]

font = pygame.font.SysFont("comicsansms", 20)
text_color = str("Color: " + str(colors[color_index]))
text_tool = str("Tool: " + str(tools[tool_index]))
text_color_surface = font.render(text_color, True, (255, 0, 255))  # Magenta
text_tool_surface = font.render(text_tool, True, (255, 0, 255))  # Magenta

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                fps = 60
                if tool_index == 6:
                    start_x = event.pos[0]
                    start_y = event.pos[1]   
                    end_x = start_x
                    end_y = start_y     
                if tool_index in [0, 1, 2, 3, 4, 5]:
                    start_x = event.pos[0]
                    start_y = event.pos[1]
                mouse_moving = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                fps = 60
                second_screen.blit(screen, (0, 0))
                mouse_moving = False

        if event.type == pygame.MOUSEMOTION:
            if mouse_moving:
                fps = 60
                if tool_index == 6:
                    start_x = end_x
                    start_y = end_y
                    end_x = event.pos[0]
                    end_y = event.pos[1]   
                if tool_index in [0, 1, 2, 3, 4, 5]:
                    end_x = event.pos[0]
                    end_y = event.pos[1] 
                    screen.blit(second_screen, (0, 0))
                if tool_index == 0:
                    pygame.draw.rect(screen, colors[color_index], pygame.Rect(draw_rectangle(start_x, start_y, end_x, end_y)), 1)
                if tool_index == 1:
                    pygame.draw.ellipse(screen, colors[color_index], pygame.Rect(draw_rectangle(start_x, start_y, end_x, end_y)), 1)
                if tool_index == 2:
                    pygame.draw.rect(screen, colors[color_index], pygame.Rect(draw_square(start_x, start_y, end_x, end_y)), 1)
                if tool_index == 3:
                    draw_right_triangle(start_x, start_y, end_x, end_y)
                if tool_index == 4:
                    draw_equilateral_triangle(start_x, start_y, end_x, end_y)
                if tool_index == 5:
                    draw_rhombus(start_x, start_y, end_x, end_y)
                if tool_index == 6:
                    pygame.draw.line(screen, (0, 0, 0), (start_x, start_y), (end_x, end_y), 7)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]: 
        fps = 7
        color_index += 1
        if color_index == len(colors):
            color_index = 0
        text_color = str("Color: " + str(colors[color_index]))
        text_color_surface = font.render(text_color, True, (255, 0, 255))  # Magenta

    if pressed[pygame.K_LEFT]: 
        fps = 7
        color_index -= 1
        if color_index == -1:
            color_index = len(colors) - 1
        text_color = str("Color: " + str(colors[color_index]))
        text_color_surface = font.render(text_color, True, (255, 0, 255))  # Magenta

    if pressed[pygame.K_UP]:
        fps = 7
        tool_index += 1
        if tool_index == len(tools):
            tool_index = 0
        text_tool = str("Tool: " + str(tools[tool_index]))
        text_tool_surface = font.render(text_tool, True, (255, 0, 255))  # Magenta

    if pressed[pygame.K_DOWN]:
        fps = 7
        tool_index -= 1
        if tool_index == -1:
            tool_index = len(tools) - 1
        text_tool = str("Tool: " + str(tools[tool_index]))
        text_tool_surface = font.render(text_tool, True, (255, 0, 255))  # Magenta

    pygame.draw.rect(screen, "White", (0, 0, 800, 30))
    screen.blit(text_color_surface, (1, 1))
    screen.blit(text_tool_surface, (201, 1))
    pygame.display.flip()
    clock.tick(fps)
