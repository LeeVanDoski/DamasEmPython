import pygame
import random
from Objs.Constantes import COMP, LARG, FPS,LADO_QUADRADO,CINZA_DOIS,CINZA_UM
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
        #quem vai começar
        começa=random.random()
        if(começa==0):
            cor=CINZA_UM
        else:
            cor=CINZA_DOIS
        self.tabuleiro.calcularMovimentoPeças(cor)

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
                    #print(y,x)
                    selec=self.tabuleiro.tabuleiro[y][x]#seleciona posição
                    #print("selec",selec)

                    if selec!=0:
                        if selec !=1 and self.is_member(selec,self.tabuleiro.peçasQuePodemMover):
                            self.tabuleiro.limpa()
                            peça=selec
                            #print("peça:",peça.posX,peça.posY)
                            #peça.organiza_movs(peça.posX,peça.posY)
                            self.tabuleiro.mostraOndeIr(peça)
                        elif selec==1:
                            self.tabuleiro.andar(peça,(y,x))
                            self.tabuleiro.limpa()
                            self.tabuleiro.descalcularMovimentoPeças(cor)
                            if(cor==CINZA_UM):
                                cor=CINZA_DOIS
                            else:
                                cor=CINZA_UM
                            self.tabuleiro.calcularMovimentoPeças(cor)
                    
                    '''
                    if selec!=0:
                        if selec !=1:
                            self.tabuleiro.limpa()
                            peça=selec
                            print("peça:",peça.posX,peça.posY)
                            peça.organiza_movs(peça.posX,peça.posY)
                            self.tabuleiro.mostraOndeIr(peça)
                        elif selec==1:
                            self.tabuleiro.andar(peça,(y,x))
                            self.tabuleiro.limpa()
                    else:
                        self.tabuleiro.limpa()
                    '''
    def is_member(self,value, iterable):
     for item in iterable:
         if value == item:
             return True
     return False