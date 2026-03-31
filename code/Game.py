import pygame
import random
from code.Menu import Menu


class Game :
    def __init__(self) :
        pygame.init ()
        # iniciar a musica
        pygame.mixer.init ()

        self.window = pygame.display.set_mode ( size=(600, 480) )
        pygame.display.set_caption ( "Kitty: Pegue as Carnes!" )

        # IMAGENS do jogo
        self.img_fundo = pygame.image.load ( "asset/fundo_jogo.png" )
        self.img_kitty = pygame.image.load ( "asset/kitty.png" )
        self.img_carne = pygame.image.load ( "asset/carne.png" )
        self.img_alface = pygame.image.load ( "asset/alface.png" )

        try :
            pygame.mixer.music.load ( "asset/musica_fundo.mp3" )
            pygame.mixer.music.set_volume ( 0.5 )
        except :
            print ( "Ixi! O arquivo da música não foi encontrado." )

    def show_end_screen(self, mensagem, cor) :
        fonte_fim = pygame.font.SysFont ( None, 45 )
        fonte_sub = pygame.font.SysFont ( None, 25 )

        waiting = True
        while waiting :
            self.window.fill ( (0, 0, 0) )

            txt = fonte_fim.render ( mensagem, True, cor )
            self.window.blit ( txt, (300 - txt.get_width () // 2, 200) )

            sub_txt = fonte_sub.render ( "Pressione o ESPAÇO para voltar ao inicio", True, (255, 255, 255) )
            self.window.blit ( sub_txt, (300 - sub_txt.get_width () // 2, 300) )

            pygame.display.flip ()

            for event in pygame.event.get () :
                if event.type == pygame.QUIT :
                    pygame.quit ()
                    quit ()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE:
                        waiting = False

    def run(self) :
        pygame.mixer.music.play ( -1 )

        while True :
            menu = Menu ( self.window )
            menu.run ()
            self.play_game ()

    def play_game(self) :
        kitty_pos = [300, 330]
        vidas = 3
        carnes_coletadas = 0
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

            # Personagem Kitty
            self.window.blit ( self.img_kitty, (kitty_pos[0], kitty_pos[1]) )

            for item in alimentos[:] :
                item[1] += 5
                imagem_item = self.img_carne if item[2] == "carne" else self.img_alface
                self.window.blit ( imagem_item, (item[0], item[1]) )

                kitty_rect = pygame.Rect ( kitty_pos[0], kitty_pos[1], 50, 50 )
                item_rect = pygame.Rect ( item[0], item[1], 30, 30 )

                if kitty_rect.colliderect ( item_rect ) :
                    if item[2] == "alface" :
                        vidas -= 1
                    else :
                        carnes_coletadas += 1
                    alimentos.remove ( item )

                elif item[1] > 480 :
                    alimentos.remove ( item )

            texto_status = fonte.render ( f"Vidas: {vidas}   Carnes: {carnes_coletadas}/10", True, (0, 0, 0) )
            self.window.blit ( texto_status, (10, 10) )

            if vidas <= 0 :
                playing = False
                self.show_end_screen ( "Você Perdeu! A Kitty ficou brava.", (255, 0, 0) )
            elif carnes_coletadas >= 10 :
                playing = False
                self.show_end_screen ( "Você Ganhou! A Kitty está feliz!", (0, 255, 0) )

            pygame.display.flip ()
            clock.tick ( 60 )