
class tablero:
  table= [["   " for x in range(9)] for y in range(9)] 
  graveyardW = []
  graveyardB=[]
  
  def __init__(self):
    # for i in range(9):
    #   for j in range(9):
    #     self.table[i][j]="  "
    self.table[0][0]=Lancer(0,0,True)
    self.table[0][1]=horse(0,1,True)
    self.table[0][2]=silverGen(0,2,True)
    self.table[0][3]=goldenGen(0,3,True)
    self.table[0][4]=King(0,4,True)
    self.table[0][5]=silverGen(0,5,True)
    self.table[0][6]=goldenGen(0,6,True)
    self.table[0][7]=horse(0,7,True)
    self.table[0][8]=Lancer(0,8,True)
    self.table[1][1]=bishop(1,1,True)
    self.table[1][7]=Tower(1,7,True)
    for k in range(9):
      self.table[2][k]=pawn(2,k,True)

    self.table[8][0]=Lancer(8,0,False)
    self.table[8][1]=horse(8,1,False)
    self.table[8][2]=silverGen(8,2,False)
    self.table[8][3]=goldenGen(8,3,False)
    self.table[8][4]=King(8,4,False)
    self.table[8][5]=silverGen(8,5,False)
    self.table[8][6]=goldenGen(8,6,False)
    self.table[8][7]=horse(8,7,False)
    self.table[8][8]=Lancer(8,8,False)
    self.table[7][1]=bishop(7,1,False)
    self.table[7][7]=Tower(7,7,False)
    for k in range(9):
      self.table[6][k]=pawn(6,k,False)

  def __str__(self):
    #print(self.table)
    att="    0   1   2   3   4   5   6   7   8 \n"
    att+="  +-------------------------------------+\n"
    for i in range(9):
      att+=str(i)+"||"
      for j in range(9):
        att+=str(self.table[i][j])+"|"
      att+="|\n"
    att+="  +-------------------------------------+\n"
    return att
      
  def move(self,xOld,yOld,xNew,yNew):
    piece= self.table[xOld][yOld]
    if(piece.isPossible(xNew,yNew)):
      print("yes")
      if(self.isPossible(xOld,yOld,xNew,yNew)):
        self.table[xNew][yNew]=piece
        self.table[xOld][yOld]="   "
        piece.refreshMove(xNew,yNew)
        self.checkAutoCrown(xNew,yNew)
  

  def isPossible(self,xOld,yOld,xNew,yNew):
    #TODO if theres is a piece
    #print(xOld,yOld,xNew,yNew)
    if(xNew>8 or yNew >8):
      print("No se puede salir del tablero")
      return False
    elif(self.table[xNew][yNew]=="   "):
      return True
    elif(self.table[xNew][yNew].white==self.table[xOld][yOld].white):
      return False
    elif(self.table[xNew][yNew].white!=self.table[xOld][yOld].white):
      if(self.table[xOld][yOld].white==True):
        self.graveyardW.append(self.table[xNew][yNew])
      else:
        self.graveyardB.append(self.table[xNew][yNew])
      return True
    else:
      return False

  def checkAutoCrown(self,x,y):
    aux=self.table[x][y]
    if(aux.isCorunable):
      if(aux.white):
        if(x==8):
          aux.crown=True
          return True
        if(x>=6):
          #ask?
          print("Coronar?")
          return False
      else:
        if(x==0):
          aux.crown=True
          return True
        if(x<=2):
          #ask?
          print("Coronar?")
          return False
    return False
  
  
  
  
  
class goldenGen:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white

  def __str__(self):
    if(self.white):
      return '\033[1m'+' Gv'+'\033[0m'
    else:
      return ' G^'
  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    if(self.white):
      if(x==self.posi+1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi-1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    else:
      if(x==self.posi-1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi+1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
  
  
    

class pawn:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '\033[1m'+'*pv'+'\033[0m'
      else:
        return '*p^'
    else:
      if(self.white):
        return '\033[1m'+' pv'+'\033[0m'
      else:
        return ' p^'
  
  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew


  def isPossible(self,x,y):
    if(self.crown):
      return self.crownedMove(x,y)
    else:
      if(y!=self.posj):
        print("movimiento no permitido")
        return False
      if(self.white):
        if(x==self.posi+1):
          return True
        else:
          print("movimiento no permitido")
          return False
      else:
        if(x==self.posi-1):
          return True
        else:
          print("movimiento no permitido")
          return False
  
  def crownedMove(self,x,y):
    if(self.white):
      if(x==self.posi+1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi-1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    else:
      if(x==self.posi-1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi+1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
  
    

class silverGen:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '\033[1m'+'*Sv'+'\033[0m'
      else:
        return '*S^'
    else:
      if(self.white):
        return '\033[1m'+' Sv'+'\033[0m'
      else:
        return ' S^'

  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew


  def isPossible(self,x,y):
    if(self.crown):
      return self.crownedMove(x,y)
    else:
      if(self.white):
        if(x==self.posi+1):
          if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
            return True
        elif(x==self.posi-1):
          if(y==self.posj-1 or y==self.posj+1):
            return True
        print("movimiento no permitido")
        return False
      else:
        if(x==self.posi-1):
          if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
            return True
        elif(x==self.posi+1):
          if(y==self.posj-1 or y==self.posj+1):
            return True
        print("movimiento no permitido")
        return False

  def crownedMove(self,x,y):
    if(self.white):
      if(x==self.posi+1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi-1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    else:
      if(x==self.posi-1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi+1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    

class horse:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '\033[1m'+'*Hv'+'\033[0m'
      else:
        return '*H^'
    else:
      if(self.white):
        return '\033[1m'+' Hv'+'\033[0m'
      else:
        return ' H^'
      
  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew

  
  def isPossible(self,x,y):
    if(self.crown):
      return self.crownedMove(x,y)
    else:
      if(self.white):
        if(x==self.posi+2 and (y==self.posj-1 or y==self.posj+1 )):
          return True
        else:
          print("movimiento no permitido")
          return False
      else:
        if(x==self.posi-2 and (y==self.posj-1 or y==self.posj+1 )):
          return True
        else:
          print("movimiento no permitido")
          return False
  
  def crownedMove(self,x,y):
    if(self.white):
      if(x==self.posi+1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi-1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    else:
      if(x==self.posi-1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi+1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    

class bishop:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '\033[1m'+'*Bv'+'\033[0m'
      else:
        return '*B^'
    else:
      if(self.white):
        return '\033[1m'+' Bv'+'\033[0m'
      else:
        return ' B^'

  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew


  def isPossible(self,x,y):
    act=self.posi*9+self.posj
    if(self.crown):
      return self.crownedMove
    if((x*9+y-act)%10==0 or (x*9+y+act)%8==0):
      return True
    else:
      print("movimiento no permitido")
      return False

  def crownedMove(self,x,y):
    if((x==self.posi-1 or x==self.posi+1) and y==self.posj):
      return True
    elif ((y==self.posj-1 or y==self.posj+1) and x==self.posi):
      return True
        
  
class Tower:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '\033[1m'+'*Tv'+'\033[0m'
      else:
        return '*T^'
    else:
      if(self.white):
        return '\033[1m'+' Tv'+'\033[0m'
      else:
        return ' T^'
  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew


  def isPossible(self,x,y):
    act=self.posi*9+self.posj
    if(self.crown):
      return self.crownedMove(x,y)
    
    if((x*9+y-act)%8==0 or y==self.posj):
      return True
    else:
      print("movimiento no permitido")
      return False
  
  def crownedMove(self,x,y):
    if((x==self.posi-1 or x==self.posi+1) and (y==self.posj+1 or y==self.posj-1)):
      return True



class Lancer:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '\033[1m'+'*Lv'+'\033[0m'
      else:
        return '*L^'
    else:
      if(self.white):
        return '\033[1m'+' Lv'+'\033[0m'
      else:
        return ' L^'
  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew


  def isPossible(self,x,y):
    if(self.crown):
      return self.crownedMove(x,y)
    else:
      if(self.white):
        if(y==self.posj and x>self.posi):
          return True
        else:
          print("movimiento no permitido")
          return False
      else:
        if(y==self.posj and x<self.posj):
          return True
        else:
          print("movimiento no permitido")
          return False
  
  def crownedMove(self,x,y):
    if(self.white):
      if(x==self.posi+1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi-1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    else:
      if(x==self.posi-1):
        if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
          return True
      elif(x==self.posi+1):
        if(y==self.posj):
          return True
      elif(x==self.posi):
        if(y==self.posj-1 or y==self.posj+1):
          return True
      print("movimiento no permitido")
      return False
    
class King:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white

  def __str__(self):
    if(self.white):
      return '\033[1m'+' Kv'+'\033[0m'
    else:
      return ' K^'
  
  def refreshMove(self,xNew,yNew):
    self.posi=xNew
    self.posj=yNew


  def isPossible(self,x,y):
    
    if(x==self.posi-1):
      if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
        return True
    elif(x==self.posi+1):
      if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
        return True
    elif(x==self.posi):
      if(y==self.posj-1 or y==self.posj+1):
        return True
    print("movimiento no permitido")
    return False

