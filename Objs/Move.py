class Move():
    def __init__(self,pos,pos_peça_remov,move_ant):
        self.pos=pos
        self.pos_peça_remov=pos_peça_remov
        self.lenght=0
        if(move_ant!=None):
            self.move_ant=move_ant
            self.lenght=move_ant.getLenght()+1
        else:
            self.move_ant=None
        
        
    def getPos(self):
        return self.pos
    
    def getPeça(self):
        return self.pos_peça_remov
    
    def getAnt(self):
        return self.move_ant
    
    def getLenght(self):
        return self.lenght
