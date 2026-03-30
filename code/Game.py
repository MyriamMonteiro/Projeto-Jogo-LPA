import pygame
import random

from code.Menu import Menu


class Game :
    def __init__(self) :
        pygame.init ()
        self.window = pygame.display.set_mode ( size=(600, 480) )
        pygame.display.set_caption ( "Kitty: Pegue as Carnes!" )

        # IMAGENS do jogo
        self.img_fundo = pygame.image.load ( "asset/fundo_jogo.png" )
        self.img_kitty = pygame.image.load ( "asset/kitty.png" )
        self.img_carne = pygame.image.load ( "asset/carne.png" )
        self.img_alface = pygame.image.load ( "asset/alface.png" )

    def run(self) :
        while True :
            menu = Menu ( self.window )
            menu.run ()
            self.play_game ()

    def play_game(self) :
        # Posição ajustada para a Kitty aparecer inteira
        kitty_pos = [300, 330]
        vidas = 3
        carnes_coletadas = 0  # Contador para a vitória
        alimentos = []
        clock = pygame.time.Clock ()
        fonte = pygame.font.SysFont ( None, 36 )

        playing = True
        while playing :
            self.window.blit ( self.img_fundo, (0, 0) )

            for event in pygame.event.get () :
                if event.type == pygame.QUIT :
                    pygame.quit ()
                    quit ()

            keys = pygame.key.get_pressed ()
            if keys[pygame.K_LEFT] and kitty_pos[0] > 0 : kitty_pos[0] -= 7
            if keys[pygame.K_RIGHT] and kitty_pos[0] < 550 : kitty_pos[0] += 7

            if random.randint ( 1, 30 ) == 1 :
                tipo = random.choice ( ["carne", "alface"] )
                alimentos.append ( [random.randint ( 0, 570 ), -50, tipo] )

            # Desenha a Kitty
            self.window.blit ( self.img_kitty, (kitty_pos[0], kitty_pos[1]) )

            for item in alimentos[:] :
                item[1] += 5
                imagem_item = self.img_carne if item[2] == "carne" else self.img_alface
                self.window.blit ( imagem_item, (item[0], item[1]) )

                # Criação dos retângulos para colisão
                kitty_rect = pygame.Rect ( kitty_pos[0], kitty_pos[1], 50, 50 )
                item_rect = pygame.Rect ( item[0], item[1], 30, 30 )

                if kitty_rect.colliderect ( item_rect ) :
                    if item[2] == "alface" :
                        vidas -= 1  # Perde vida ao tocar no alface
                    else :
                        carnes_coletadas += 1  # Ganha ponto ao tocar na carne
                    alimentos.remove ( item )

                elif item[1] > 480 :  # Remove se sair da tela
                    alimentos.remove ( item )

            # --- TEXTO DE VIDAS E PONTOS (Parte de cima) ---
            texto_status = fonte.render ( f"Vidas: {vidas}   Carnes: {carnes_coletadas}/20", True, (0, 0, 0) )
            self.window.blit ( texto_status, (20, 20) )

            # --- CONDIÇÕES DE FIM DE JOGO ---
            if vidas <= 0 or carnes_coletadas >= 20 :
                playing = False  # Sai do loop e volta para o menu

            pygame.display.flip ()
            clock.tick ( 60 )