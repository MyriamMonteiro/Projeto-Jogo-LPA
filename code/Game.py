import pygame

from code.Menu import Menu


class Game:

    def __init__(self):
        # inicializa e define o tamanho da janela do jogo
        pygame.init ()
        self.window = pygame.display.set_mode ( size=(600, 480) )

    def run(self):
        while True:
            menu = Menu(self.window) #envocar parametro
            menu.run()
            pass

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         quit()