import pygame
from .Constantes import LADO_QUADRADO,CINZA_UM,LINHAS,COLUNAS

class Peça():
    ESPAÇAMENTO=7
    def __init__(self,COR,Pos,TELA,TABULEIRO):
        self.tela=TELA
        self.cor=COR
        if self.cor==CINZA_UM:
            self.andar=1
        else:
            self.andar=-1
        self.posX=Pos[1]
        self.posY=Pos[0]
        self.dama=False
        self.possiv_movs=[]
        self.tabuleiro=TABULEIRO

    def desenha_peça(self):
        pygame.draw.circle(self.tela,self.cor,(self.posY*LADO_QUADRADO + LADO_QUADRADO/2,self.posX*LADO_QUADRADO + LADO_QUADRADO/2),
                            LADO_QUADRADO/2-self.ESPAÇAMENTO)
        
    
    def calcula_movs(self,posX,posY):
        if(self.noLimite(posX,posY)):
            if(posX==self.posX and posY==self.posY):
                return self.calcula_movs(posX+self.andar,posY+1) or self.calcula_movs(posX+self.andar,posY-1) 
                'return self.calcula_movs(posX+self.andar,posY-1) '
            
            elif(self.tabuleiro[posX][posY]!=0 and self.ehInimigo(self.tabuleiro[posX][posY])):
                return self.calcula_movs(posX+self.andar,posY+1) or self.calcula_movs(posX+self.andar,posY-1) 
                'return self.calcula_movs(posX+self.andar,posY-1) '
            
            elif(self.tabuleiro[posX][posY]==0):
                if(not(self.noLimite(posX+self.andar,posY+1) and self.tabuleiro[posX+self.andar][posY+1]!=0) and 
                   not(self.noLimite(posX+self.andar,posY-1) and self.tabuleiro[posX+self.andar][posY-1]!=0)):
                    self.possiv_movs.append((posX,posY))
                
                elif(self.noLimite(posX-self.andar,posY-1) and (posX-self.andar==self.posX and (self.posY==posY-1 or self.posY==posY+1))):
                    self.possiv_movs.append((posX,posY))
                else:
                    if(self.noLimite(posX+self.andar,posY+1) and (self.tabuleiro[posX+self.andar][posY+1]!=0) and self.ehInimigo(self.tabuleiro[posX+self.andar][posY+1])):
                        return self.calcula_movs(posX+self.andar,posY+1)
                    if(self.noLimite(posX+self.andar,posY-1) and (self.tabuleiro[posX+self.andar][posY-1]!=0) and self.ehInimigo(self.tabuleiro[posX+self.andar][posY-1])):
                        return self.calcula_movs(posX+self.andar,posY-1)              
        else:
            return

    def noLimite(self,posX,posY):
        return ((posX>=0 and posX< COLUNAS) and (posY>=0 and posY<LINHAS))
    
    def ehInimigo(self,peçaIni):
        return not(peçaIni.cor==self.cor)
    
    def setPos(self, pos):
        self.posX=pos[0]
        self.posY=pos[1]
        self.desenha_peça()