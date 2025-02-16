import pygame
from .Constantes import LADO_QUADRADO,CINZA_UM,LINHAS,COLUNAS,BRANCO,CINZA_DOIS
from .Move import Move

class Peça():
    ESPAÇAMENTO=7
    def __init__(self,COR,Pos,TELA,TABULEIRO,INIMIGOS):
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
        self.verif_movs=[]
        self.tabuleiro=TABULEIRO
        self.inimigos=INIMIGOS

    def desenha_peça(self):
        pygame.draw.circle(self.tela,self.cor,(self.posY*LADO_QUADRADO + LADO_QUADRADO/2,self.posX*LADO_QUADRADO + LADO_QUADRADO/2),
                            LADO_QUADRADO/2-self.ESPAÇAMENTO)
        if self.dama==True:
            pygame.draw.circle(self.tela,BRANCO,(self.posY*LADO_QUADRADO + LADO_QUADRADO/2,self.posX*LADO_QUADRADO + LADO_QUADRADO/2),
                            LADO_QUADRADO/4-self.ESPAÇAMENTO)

            
    def noLimite(self,posX,posY):
        return ((posX>=0 and posX< COLUNAS) and (posY>=0 and posY<LINHAS))
    
    def ehInimigo(self,peçaIni):
        return peçaIni.cor!=self.cor
    
    def setPos(self, pos):
        self.posX=pos[0]
        self.posY=pos[1]
        if self.posX==7 and self.cor==CINZA_UM:
            self.dama=True
            print(self.dama)
        elif self.posX==0 and self.cor==CINZA_DOIS:
            self.dama=True
            print(self.dama)

        self.desenha_peça()

    def mov_dama(self,posX,posY):
        i=1
        c1=True
        c2=True
        c3=True
        c4=True
        while(c1 or c2 or c3 or c4):
            if(self.noLimite(posX+i,posY+i) and c1):
                if(self.tabuleiro[posX+i][posY+i]==0):
                    self.calcular_mov(posX+i,posY+i,(posX+i,posY+i),None)
                elif(self.tabuleiro[posX+i][posY+i]!=0):
                    self.calcular_mov(posX,posY,(posX,posY),None)
            else:
                c1=False

            if(self.noLimite(posX-i,posY+i) and c2):
                if(self.tabuleiro[posX-i][posY+i]==0):
                    self.calcular_mov(posX-i,posY+i,(posX-i,posY+i),None)
                elif(self.tabuleiro[posX-i][posY+i]!=0):
                     self.calcular_mov(posX,posY,(posX,posY),None)
            else:
                c2=False
            
            if(self.noLimite(posX+i,posY-i) and c3):
                if(self.tabuleiro[posX+i][posY-i]==0):
                    self.calcular_mov(posX+i,posY-i,(posX+i,posY-i),None)
                elif(self.tabuleiro[posX+i][posY-i]!=0):
                    self.calcular_mov(posX,posY,(posX,posY),None)
            else:
                c3=False
            
            if(self.noLimite(posX-i,posY-i) and c4):
                if(self.tabuleiro[posX-i][posY-i]==0):
                    self.calcular_mov(posX-i,posY-i,(posX-i,posY-i),None)
                elif(self.tabuleiro[posX-i][posY-i]!=0):
                    self.calcular_mov(posX,posY,(posX,posY),None)
            else:
                c4=False
            i+=1
            
            
        '''
        i=1
        while(self.noLimite(posX+i,posY+i)):
            if(self.tabuleiro[posX+i][posY+i]!=0  and self.ehInimigo (self.tabuleiro[posX+i][posY+i])):
                self.calcular_mov(posX+i-1,posY+i-1,(posX+i-1,posY+i-1),None)
                break
            elif(self.tabuleiro[posX+i][posY+i]==0):
                new_move=Move((posX+i,posY+i),(-1,-1),None)
                self.verif_movs.append(new_move)
            else:
                break
            i+=1
        i=1
        while(self.noLimite(posX-i,posY+i)):
            if(self.tabuleiro[posX-i][posY+i]!=0 and self.ehInimigo(self.tabuleiro[posX-i][posY+i])):
                self.calcular_mov(posX-i-1,posY+i-1,(posX-i+1,posY+i-1),None)
                break
            elif(self.tabuleiro[posX-i][posY+i]==0 ):
                new_move=Move((posX-i,posY+i),(-1,-1),None)
                self.verif_movs.append(new_move)
            else:
                break
            i+=1
        i=1
        while(self.noLimite(posX+i,posY-i)):
            if(self.tabuleiro[posX+i][posY-i]!=0 and self.ehInimigo(self.tabuleiro[posX+i][posY-i])):
                self.calcular_mov(posX+i-1,posY-i-1,(posX+i-1,posY-i+1),None)
                break
            elif(self.tabuleiro[posX+i][posY-i]==0 ):
                new_move=Move((posX+i,posY-i),(-1,-1),None)
                self.verif_movs.append(new_move)
            else:
                break
            i+=1
        i=1
        while(self.noLimite(posX-i,posY-i)):
            if(self.tabuleiro[posX-i][posY-i]!=0 and self.ehInimigo (self.tabuleiro[posX-i][posY-i])):
                self.calcular_mov(posX-i-1,posY-i-1,(posX-i+1,posY-i+1),None)
                break
            elif(self.tabuleiro[posX-i][posY-i]==0):
                new_move=Move((posX-i,posY-i),(-1,-1),None)
                self.verif_movs.append(new_move)
            else:
                break
            i+=1
        i=1
'''

    def calcular_mov(self,posX,posY,pos_ant,move_ant):

        if(self.noLimite(posX,posY)):
            #diagonal direita
            if(self.noLimite(posX+1,posY+1) and self.tabuleiro[posX+1][posY+1]!=0 and 
               self.ehInimigo(self.tabuleiro[posX+1][posY+1]) and self.noLimite(posX+2,posY+2)
               and self.tabuleiro[posX+2][posY+2]==0):
                
                if(pos_ant!=(posX+2,posY+2)):
                    new_move=Move((posX+2,posY+2),(posX+1,posY+1),move_ant)
                    new_move.lenght+=1
                    self.possiv_movs.append(new_move)
                    self.calcular_mov(posX+2,posY+2,(posX,posY),new_move)

            if(self.noLimite(posX-1,posY+1) and self.tabuleiro[posX-1][posY+1]!=0 and 
               self.ehInimigo(self.tabuleiro[posX-1][posY+1]) and self.noLimite(posX-2,posY+2)
               and self.tabuleiro[posX-2][posY+2]==0):
                  
                if(pos_ant!=(posX-2,posY+2)):
                    new_move=Move((posX-2,posY+2),(posX-1,posY+1),move_ant)
                    new_move.lenght+=1
                    self.possiv_movs.append(new_move)
                    self.calcular_mov(posX-2,posY+2,(posX,posY),new_move)

            if(self.noLimite(posX-1,posY-1) and self.tabuleiro[posX-1][posY-1]!=0 and 
               self.ehInimigo(self.tabuleiro[posX-1][posY-1]) and self.noLimite(posX-2,posY-2)
               and self.tabuleiro[posX-2][posY-2]==0):
                
                if(pos_ant!=(posX-2,posY-2)):
                    new_move=Move((posX-2,posY-2),(posX-1,posY-1),move_ant)
                    new_move.lenght+=1
                    self.possiv_movs.append(new_move)
                    self.calcular_mov(posX-2,posY-2,(posX,posY),new_move)
    
            if(self.noLimite(posX+1,posY-1) and self.tabuleiro[posX+1][posY-1]!=0 and 
               self.ehInimigo(self.tabuleiro[posX+1][posY-1]) and self.noLimite(posX+2,posY-2)
               and self.tabuleiro[posX+2][posY-2]==0):
                
                 if(pos_ant!=(posX+2,posY-2)):
                    new_move=Move((posX+2,posY-2),(posX+1,posY-1),move_ant)
                    new_move.lenght+=1
                    self.possiv_movs.append(new_move)
                    self.calcular_mov(posX+2,posY-2,(posX,posY),new_move)

            if(len(self.possiv_movs)==0 and self.dama==False):
                if(self.noLimite(posX+self.andar,posY+1) and self.tabuleiro[posX+self.andar][posY+1]==0):
                    new_move=Move((posX+self.andar,posY+1),(-1,-1),None)
                    self.verif_movs.append(new_move)

                if(self.noLimite(posX+self.andar,posY-1) and self.tabuleiro[posX+self.andar][posY-1]==0):
                    new_move=Move((posX+self.andar,posY-1),(-1,-1),None)
                    self.verif_movs.append(new_move)
            elif(len(self.possiv_movs)==0 and self.dama==True and posX!=self.posX and posY!=self.posY):
                new_move=Move((posX,posY),(-1,-1),None)
                self.verif_movs.append(new_move)
            
            return
        else:
            return 

    def organiza_movs(self,posX,posY):
        if(self.dama):
            self.mov_dama(posX,posY)
        else:
            self.calcular_mov(posX,posY,(posX,posY),None)
        if(not len(self.possiv_movs)==0):
            #self.possiv_movs.sort(reverse=True,key=self.GetLenght)
            for i in range(len(self.possiv_movs)):
                j=i
            while(j > 0 and self.possiv_movs[j].getLenght() > self.possiv_movs[j-1].getLenght()):
                    aux = self.possiv_movs[j]
                    self.possiv_movs[j] = self.possiv_movs[j - 1]
                    self.possiv_movs[j - 1] = aux
                    j -= 1

            mov=self.possiv_movs[0]
            i=1
            while(i<len(self.possiv_movs) and mov.getLenght()==self.possiv_movs[i].getLenght()):
                i+=1

            for  x in range(i):
                self.verif_movs.append(self.possiv_movs[x])


    def remov(self,move):
        while(move!=None):
            coord=move.getPeça()
            peça=self.tabuleiro[coord[0]][coord[1]]
            self.tabuleiro[coord[0]][coord[1]]=0
            print("Peça deletada: ",peça)
            if(peça!=0):
                self.inimigos.remove(peça)
            del peça
            move=move.getAnt()

    def verif_mov_repetido(self,move):
        if(len(self.possiv_movs)!=0):
            for mov in self.possiv_movs:
                if(mov.pos==move.pos):
                    return True
                else:
                    return False
        else:
            return False
        


        