import pygame
from Objs.Constantes import COMP, LARG, FPS,LADO_QUADRADO
from Objs.Tabuleiro import Tabuleiro

class Jogo():
    def __init__(self) :
        self.tela=pygame.display.set_mode((COMP,LARG))
        pygame.display.set_caption("Damas 3000")
        self.tabuleiro=Tabuleiro(self.tela)
        self.executar()

    def executar(self):
        rodando=True
        clock=pygame.time.Clock()
        pygame.display.update()

        while rodando:
            clock.tick(FPS)
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.QUIT:
                    rodando=False
                if event.type == pygame.MOUSEBUTTONDOWN:

                    x,y=pygame.mouse.get_pos()

                    x=x//LADO_QUADRADO#arredondo os pixels para coordenada de matriz
                    y=y//LADO_QUADRADO
                    print(y,x)
                    selec=self.tabuleiro.tabuleiro[y][x]#seleciona posição
                    print("selec",selec)
                    if selec!=0:
                        if selec !=1:
                            self.tabuleiro.limpa()
                            peça=selec
                            print("peça:",peça.posX,peça.posY)
                            peça.calcula_movs(peça.posX,peça.posY)
                            self.tabuleiro.mostraOndeIr(peça)
                        elif selec==1:
                            self.tabuleiro.tabuleiro[y][x]=peça
                            self.tabuleiro.tabuleiro[peça.posX][peça.posY]=0
                            peça.setPos((y,x))
                            peça.possiv_movs.clear()
                            self.tabuleiro.limpa()
                    else:
                        self.tabuleiro.limpa()
