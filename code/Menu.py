import pygame


class Menu :
    def __init__(self, window):
        self.window = window
        # IMAGEM fundo
        self.background_menu = pygame.image.load( 'asset/fundo_menu_600x480.png' )
        self.font = pygame.font.SysFont(None, 24)

    def run(self):
        while True:
            # Desenha a imagem de fundo do menu
            self.window.blit(self.background_menu, (0, 0))
            #TEXTO
            font = pygame.font.SysFont ( None, 20 )
            text = font.render ( "Pressione ESPAÇO para jogar", True, (255, 255, 255) )
            self.window.blit ( text, (200, 450) )

            # Destacar a orientação do texto
            pos_x, pos_y = 200, 450
            rect_fundo = text.get_rect ( topleft=(pos_x, pos_y) )
            pygame.draw.rect ( self.window, (50, 50, 50), rect_fundo )
            self.window.blit ( text, (pos_x, pos_y) )

            pygame.display.flip ()

            for event in pygame.event.get () :
                if event.type == pygame.QUIT :
                    pygame.quit ()
                    quit ()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE :
                        return