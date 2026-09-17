import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT= (500,500)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
title = pygame.display.set_caption(('Image upload...'))

Bg_image = pygame.transform.scale(pygame.image.load('download.jfif').convert(),
(SCREEN_WIDTH,SCREEN_HEIGHT))

person_image = pygame.transform.scale(pygame.image.load('images.png').convert_alpha(),
(200,200))

person_rect = person_image.get_rect(center = (SCREEN_WIDTH //2, SCREEN_HEIGHT//2-30))

text = pygame.font.Font(None,36).render('Hello World', True, pygame.Color('black'))

text_rect = text.get_rect(center = (SCREEN_WIDTH //2, SCREEN_HEIGHT//2+110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
           
           running = False
        
        display.surface.blit(Bg_image, (0,0))
        display.surface.blit(person_image, person_rect)
        display.surface.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()
