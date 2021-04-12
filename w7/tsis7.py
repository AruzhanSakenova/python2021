import pygame
import math
pygame.init()

width, height = (900, 660) #x,y
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Functions')

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
pi = math.pi

running= True
while running:
  # Even loop
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(WHITE)
  pygame.display.flip()

   
  for x in range(90, 741, 120): #сетка по верт
    if x != 570:
          pygame.draw.line(screen, BLACK, (x, 50), (x, 610))
    else:
        pygame.draw.line(screen, BLACK, (x, 50), (x, 90))
        pygame.draw.line(screen, BLACK, (x, 150), (x, 610))
        
        
  for x in range(150, 811, 120): #большие сверх низ 
      pygame.draw.line(screen, BLACK, (x, 50), (x, 85))
      pygame.draw.line(screen, BLACK, (x, 610), (x, 575))

  for x in range(120, 811, 30): #средние сверх низ
      pygame.draw.line(screen, BLACK, (x, 50), (x, 75))
      pygame.draw.line(screen, BLACK, (x, 610), (x, 585))
    
  for x in range(105, 811, 15): #маленькие свер низ
      pygame.draw.line(screen, BLACK, (x, 50), (x, 60))
      pygame.draw.line(screen, BLACK, (x, 610), (x, 600))


  for y in range(90, 571, 60): #сетка по гор
      pygame.draw.line(screen, BLACK, (50, y), (850, y))

  for y in range(90, 571, 30): #сред слев справ
      pygame.draw.line(screen, BLACK, (50, y), (80, y))
      pygame.draw.line(screen, BLACK, (820,y), (850, y))
  for y in range(90, 571, 15): #сред слев справ
      pygame.draw.line(screen, BLACK, (50, y), (65, y))
      pygame.draw.line(screen, BLACK, (835,y), (850, y))
  
  for x in range(90, 810):
    sin_y1 = 240 * math.sin((x - 90) / 120 * pi)
    sin_y2 = 240 * math.sin((x - 89) / 120 * pi)
    pygame.draw.aalines(screen, RED, False, [(x, 330 + sin_y1), ((x + 1), 330 + sin_y2)])

  for x in range(90, 810, 2):
        cos_y1 = 240 * math.cos((x - 90) / 120 * pi)
        cos_y2 = 240 * math.cos((x - 89) / 120 * pi)
        pygame.draw.aalines(screen, BLUE, False, [(x, 330 + cos_y1),((x + 1),330 + cos_y2)])
  
  f1 = pygame.font.Font(None, 25)
  s= f1.render('sin x', False, RED)
  f2 = pygame.font.SysFont(None, 25)
  c = f2.render('cos x', False, BLUE)
  screen.blit(s, (555, 105))
  screen.blit(c, (555, 125))
  for x in range(600, 620): #линия кос
    pygame.draw.line(screen, RED, (x, 113), (x, 113))
  for x in range(600, 620): #линия син
    pygame.draw.line(screen, BLUE, (x, 133), (x, 133))
  osx = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
  osy = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']
  f3=pygame.font.Font(None, 25)

  for x in range(90, 850, 60):
    screen.blit(f3.render(osx[(x -85) // 60], False, BLACK), (x - 10, 610))
  for y in range(90, 620, 60):
    screen.blit(f3.render(osy[(y - 90) // 60], False, BLACK), (5, (y - 10)))
  
  pygame.draw.rect(screen, BLACK, (50, 50, 800, 560), 3)  
  pygame.draw.line(screen, BLACK, (50, 330), (850, 330), 3)  
  pygame.draw.line(screen, BLACK, (450, 50), (450, 610), 3)  
  pygame.draw.line(screen, BLACK, (50, 90), (850, 90))  
  pygame.draw.line(screen, BLACK, (50,570), (850, 570))  
  pygame.draw.line(screen, BLACK, (90, 50), (90, 610))  
  pygame.draw.line(screen, BLACK, (810, 50), (810, 610)) 
    
pygame.quit()