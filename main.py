import pygame

print('Setup Start')
pygame.init ()
# tamanho da janela do jogo
window = pygame.display.set_mode ( size=(600, 480) )
print('Setup End')

print('Loop Start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()