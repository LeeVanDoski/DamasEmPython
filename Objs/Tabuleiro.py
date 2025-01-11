import pygame
from .Constantes import LINHAS, COLUNAS,PRETO,BRANCO,LADO_QUADRADO,CINZA_UM,CINZA_DOIS,AMARELO
from .Peça import Peça

class Tabuleiro():
    def __init__(self,TELA):
        self.tabuleiro=[]
        self.brancas=12
        self.pretas=12
        self.tela=TELA
        self.peçasCinzas=[]
        self.peçasOutro=[]
        self.peçasQuePodemMover=[]
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
                        peça=Peça(CINZA_UM,(j,i),self.tela,self.tabuleiro)
                        self.peçasCinzas.append(peça)
                        self.tabuleiro[i].append(peça)  #append coloca o termo na linha, na coluna do lado  
                        self.tabuleiro[i][j].desenha_peça()
                    elif i>=5:
                        peça=Peça(CINZA_DOIS,(j,i),self.tela,self.tabuleiro)
                        self.peçasOutro.append(peça)
                        self.tabuleiro[i].append(peça)
                        self.tabuleiro[i][j].desenha_peça()
                    else:
                        self.tabuleiro[i].append(0)
                else:
                    self.tabuleiro[i].append(0)

    def mostraOndeIr(self,selec):
        print("possiveis movs: ",selec.possiv_movs)
        print('verif_movs: ',selec.verif_movs)
        for mov in selec.verif_movs:
            self.tabuleiro[mov.getPos()[0]][mov.getPos()[1]]=1
            pygame.draw.circle(self.tela,AMARELO,(mov.getPos()[1]*LADO_QUADRADO + LADO_QUADRADO/2,mov.getPos()[0]*LADO_QUADRADO + LADO_QUADRADO/2),
                           LADO_QUADRADO/4-selec.ESPAÇAMENTO)

    def limpa(self):
        for i in range(LINHAS):
            for j in range((i+1)%2,COLUNAS,2):
                if self.tabuleiro[i][j]==1 or self.tabuleiro[i][j]==0:
                    self.tabuleiro[i][j]=0
                    pygame.draw.rect(self.tela,PRETO,(j*LADO_QUADRADO,i*LADO_QUADRADO,LADO_QUADRADO,LADO_QUADRADO))



    def andar(self,peça,move):
        for mov in peça.verif_movs:
            print(move)
            print(mov.getPos())
            if(mov.getPos()==move):
                self.tabuleiro[move[0]][move[1]]=peça
                self.tabuleiro[peça.posX][peça.posY]=0
                peça.setPos(move)
                peça.remov(mov)
                peça.possiv_movs.clear()
                peça.verif_movs.clear()

    def calcularMovimentoPeças(self,cor):
        if(cor==CINZA_UM):
            peças=self.peçasCinzas
        else:
            peças=self.peçasOutro
        for peça in peças:
            peça.organiza_movs(peça.posX,peça.posY)
            if(len(peça.verif_movs)!=0):
                self.peçasQuePodemMover.append(peça)

        i=0
        max=self.peçasQuePodemMover[i].verif_movs[0].lenght
        while(i<len(self.peçasQuePodemMover)):
            if(self.peçasQuePodemMover[i].verif_movs[0].lenght<max):
                self.peçasQuePodemMover.remove(self.peçasQuePodemMover[i])
                i+=1
            elif(self.peçasQuePodemMover[i].verif_movs[0].lenght>max):
                max=self.peçasQuePodemMover[i].verif_movs[0].lenght
                i=0
            else:
                i+=1
            
        print("Podem mover:", self.peçasQuePodemMover)
                
    
    def descalcularMovimentoPeças(self,cor):
        if(cor==CINZA_UM):
            peças=self.peçasCinzas
        else:
            peças=self.peçasOutro
        for peça in peças:
            peça.possiv_movs.clear()
            peça.verif_movs.clear()

        self.peçasQuePodemMover.clear()