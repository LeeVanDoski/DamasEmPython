import pygame
from .Constantes import LINHAS, COLUNAS,PRETO,BRANCO,LADO_QUADRADO,CINZA_UM,CINZA_DOIS,AMARELO
from .Peça import Peça

class Tabuleiro():
    def __init__(self,TELA):
        self.tabuleiro=[]
        self.brancas=12
        self.pretas=12
        self.tela=TELA
        self.cria_tabuleiro()

    def desenha_quadrados(self):
        self.tela.fill(PRETO)
        for i in range(LINHAS):
            for j in range(i%2,COLUNAS,2):
                pygame.draw.rect(self.tela,BRANCO,(j*LADO_QUADRADO,i*LADO_QUADRADO,LADO_QUADRADO,LADO_QUADRADO))

    def cria_tabuleiro(self):
        self.desenha_quadrados()
        for i in range(LINHAS):
            self.tabuleiro.append([])
            for j in range(COLUNAS):
                if j % 2 ==((i+1)%2):
                    if i<3:
                        self.tabuleiro[i].append(Peça(CINZA_UM,(j,i),self.tela,self.tabuleiro))  #append coloca o termo na linha, na coluna do lado  
                        peça=self.tabuleiro[i][j].desenha_peça()
                    elif i>=5:
                        self.tabuleiro[i].append(Peça(CINZA_DOIS,(j,i),self.tela,self.tabuleiro))
                        self.tabuleiro[i][j].desenha_peça()
                    else:
                        self.tabuleiro[i].append(0)
                else:
                    self.tabuleiro[i].append(0)

    def mostraOndeIr(self,selec):
        print("possiveis movs: ",selec.possiv_movs)
        for mov in selec.possiv_movs:
            self.tabuleiro[mov[0]][mov[1]]=1
            pygame.draw.circle(self.tela,AMARELO,(mov[1]*LADO_QUADRADO + LADO_QUADRADO/2,mov[0]*LADO_QUADRADO + LADO_QUADRADO/2),
                           LADO_QUADRADO/4-selec.ESPAÇAMENTO)

    def limpa(self):
        for i in range(LINHAS):
            for j in range((i+1)%2,COLUNAS,2):
                if self.tabuleiro[i][j]==1 or self.tabuleiro[i][j]==0:
                    self.tabuleiro[i][j]=0
                    pygame.draw.rect(self.tela,PRETO,(j*LADO_QUADRADO,i*LADO_QUADRADO,LADO_QUADRADO,LADO_QUADRADO))
