

#Strings to translation
movementFailed="movement not allowed"
failSelection="You have not selected a correct piece check the coordinates you've entered"
wrongColorSelected="You can only move your chips"
indexOutofRange="Your coordinates are out of the table check it and enter them again"
crowningAsk="Do you want to crown the piece? Y / N : "
pieceCrowned="The piece has been crowned"
pieceNotCrowned="The piece hasn't been crowned"

class Tablero:
  table= [["   " for x in range(9)] for y in range(9)] 
  graveyardW = [] #piezas capturadas por blancas
  graveyardB=[] #piezas capturadas por negras
  
  def __init__(self):
    """crea tablero inicial con cada elemento en su posicion correspondiente"""
    
    self.table[0][0]=Lancer(0,0,True)
    self.table[0][1]=Horse(0,1,True)
    self.table[0][2]=SilverGen(0,2,True)
    self.table[0][3]=GoldenGen(0,3,True)
    self.table[0][4]=King(0,4,True)
    self.table[0][5]=SilverGen(0,5,True)
    self.table[0][6]=GoldenGen(0,6,True)
    self.table[0][7]=Horse(0,7,True)
    self.table[0][8]=Lancer(0,8,True)
    self.table[1][1]=Bishop(1,1,True)
    self.table[1][7]=Tower(1,7,True)
    for k in range(9):
      self.table[2][k]=Pawn(2,k,True)

    self.table[8][0]=Lancer(8,0,False)
    self.table[8][1]=Horse(8,1,False)
    self.table[8][2]=SilverGen(8,2,False)
    self.table[8][3]=GoldenGen(8,3,False)
    self.table[8][4]=King(8,4,False)
    self.table[8][5]=SilverGen(8,5,False)
    self.table[8][6]=GoldenGen(8,6,False)
    self.table[8][7]=Horse(8,7,False)
    self.table[8][8]=Lancer(8,8,False)
    self.table[7][1]=Bishop(7,1,False)
    self.table[7][7]=Tower(7,7,False)
    for k in range(9):
      self.table[6][k]=Pawn(6,k,False)

  def __str__(self):
    """ imprime tablero """
    #print(self.table)
    att="    0   1   2   3   4   5   6   7   8 \n"
    att+="  +-----------------------------------+\n"
    for i in range(9):
      att+=str(i)+"||"
      for j in range(9):
        att+=str(self.table[i][j])+"|"
      att+="|\n"
    att+="  +-----------------------------------+\n"
    return att
      
  def move(self,xOld,yOld,xNew,yNew,player):
    """mueve una pieza desde origen hasta final
    si el movimiento no es posible, o no se puede ocupar devuelve falso"""
    if(xOld>8 or xNew>8 or yNew<0 or yOld<0):
      print(indexOutofRange)
      return False
    piece= self.table[xOld][yOld]
    if(piece=="   "):
      print(failSelection)
      return False
    elif((player=="Black" and piece.white) or (player=="White" and not (piece.white))):
      print(wrongColorSelected)
      return False
    elif(piece.isPossible(xNew,yNew)):
      #print("yes")
      if(self.isPossible(xOld,yOld,xNew,yNew)):
        if(not piece.hasObstacles(self,xNew,yNew)):
          self.send2Graveyard(xOld,yOld,xNew,yNew)
          self.table[xNew][yNew]=piece
          self.table[xOld][yOld]="   "
          piece.refreshMove(xNew,yNew)
          self.checkAutoCrown(xNew,yNew)
          return True
    return False
  
  def isFree(self,x,y):
    if(self.table[x][y]=="   "):
      return True
    else:
      return False

  def send2Graveyard(self,xOld,yOld,xNew,yNew):
    if(self.table[xNew][yNew]!="   "):
      aux=self.table[xNew][yNew]
      aux.crown=False
      if(self.table[xOld][yOld].white==True):
        #dependiendo del color de la ficha coloca la ficha comida en un cementerio u otro
        aux.white=True
        self.graveyardW.append(aux)
      else:
        aux.white=False
        self.graveyardB.append(aux)

  def isPossible(self,xOld,yOld,xNew,yNew):
    """ revisa si es posible efectuar dicho movimiento en el tablero, si lo es, devuelve true"""
    #print(xOld,yOld,xNew,yNew)
    if(xNew>8 or yNew >8 or xNew<0 or yNew <0):
      #index out of range
      print(indexOutofRange)
      return False
    elif(self.table[xNew][yNew]=="   "):
      #el destino es una casilla vacia
      return True
    elif(self.table[xNew][yNew].white==self.table[xOld][yOld].white):
      #el destino esta ocupado por casilla mismo color
      print(movementFailed)
      return False
    elif(self.table[xNew][yNew].white!=self.table[xOld][yOld].white):
      #son distinto color
      return True
    else:
      return False

  def checkAutoCrown(self,x,y):
    """revisa si la ficha no puede hacer mas movimientos y necesita ser autocoronada"""
    aux=self.table[x][y]
    if(aux.isCorunable and not aux.crown):
      #la ficha es coronable y no ha sido coronada
      if(aux.white):
        if(x==8 and aux.autoCorunable):
          #posicion limite para blancas y autocoronamos si la ficha es autocoronable
          aux.crown=True
          print(pieceCrowned)
          return True
        if(x>=6 or aux.canBeCorunated):
          #ask?
          aux.canBeCorunated=True
          a=input(crowningAsk)
          if(a=="Y" or a=="y"):
            aux.crown=True
            print(pieceCrowned)
            return True
          else:
            print(pieceNotCrowned)
            return False
      else:
        if(x==0):
          #posicion limite para negras y autocoronamos
          aux.crown=True
          print(pieceCrowned)
          return True
        if(x<=2 or aux.canBeCorunated):
          #ask?
          aux.canBeCorunated=True
          a=input(crowningAsk)
          if(a=="Y" or a=="y"):
            aux.crown=True
            print(pieceCrowned)
            return True
          else:
            print(pieceNotCrowned)
            return False
    return False
  
  def printGraveyard(self,white):
    att=""
    att+="\t"
    if(white):
      for i in self.graveyardW:
        
        att+=str(i)
        att+="|| "
    else:
      for i in self.graveyardB:
        att+=str(i)
        att+="|| "
    return att
  
  def insert(self,piece,x,y,player):
    self.table[x][y]=piece
    print(piece)
    if(player=="White"):
      self.graveyardW.remove(piece)
    else:
      self.graveyardB.remove(piece)
    return True
    
  
  
  
class GoldenGen:
  posi=0
  posj=0
  white=None
  crown=True
  isCorunable=False
  autoCorunable=False
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white

  def __str__(self):
    if(self.white):
      return ' Gv'
    else:
      return ' G^'
  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
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
      print(movementFailed)
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
      print(movementFailed)
      return False
  
  def hasObstacles(self,table,x,y):
    """solo mueve una posicion"""
    
    return False
    

class Pawn:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  autoCorunable=True
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '*pv'
      else:
        return '*p^'
    else:
      if(self.white):
        return ' pv'
      else:
        return ' p^'
  
  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
    if(self.crown):
      return self.crownedMove(x,y)
    else:
      if(y!=self.posj):
        print(movementFailed)
        return False
      if(self.white):
        if(x==self.posi+1):
          return True
        else:
          print(movementFailed)
          return False
      else:
        if(x==self.posi-1):
          return True
        else:
          print(movementFailed)
          return False
  
  def crownedMove(self,x,y):
    """movimientos posibles una vez coronado"""
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
      print(movementFailed)
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
      print(movementFailed)
      return False

  def hasObstacles(self,table,x,y):
    """solo mueve una posicion"""
    
    return False
    

class SilverGen:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  autoCorunable=True
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '*Sv'
      else:
        return '*S^'
    else:
      if(self.white):
        return ' Sv'
      else:
        return ' S^'

  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
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
        print(movementFailed)
        return False
      else:
        if(x==self.posi-1):
          if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
            return True
        elif(x==self.posi+1):
          if(y==self.posj-1 or y==self.posj+1):
            return True
        print(movementFailed)
        return False

  def crownedMove(self,x,y):
    """movimientos posibles una vez coronado"""
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
      print(movementFailed)
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
      print(movementFailed)
      return False

  def hasObstacles(self,table,x,y):
    """solo mueve una posicion"""
    
    return False


class Horse:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  autoCorunable=True
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '*Hv'
      else:
        return '*H^'
    else:
      if(self.white):
        return ' Hv'
      else:
        return ' H^'
      
  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
    if(self.crown):
      return self.crownedMove(x,y)
    else:
      if(self.white):
        if(x==self.posi+2 and (y==self.posj-1 or y==self.posj+1 )):
          return True
        else:
          print(movementFailed)
          return False
      else:
        if(x==self.posi-2 and (y==self.posj-1 or y==self.posj+1 )):
          return True
        else:
          print(movementFailed)
          return False
  
  def crownedMove(self,x,y):
    """movimientos posibles una vez coronado"""
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
      print(movementFailed)
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
      print(movementFailed)
      return False
  def hasObstacles(self,table,x,y):
    """devuelve False porque siempre salta de posicion"""
    return False
    

class Bishop:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  autoCorunable=False
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '*Bv'
      else:
        return '*B^'
    else:
      if(self.white):
        return ' Bv'
      else:
        return ' B^'

  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
    act=self.posi*9+self.posj
    if(self.crown):
      return self.crownedMove
    if((x*9+y-act)%10==0 or (x*9+y+act)%8==0):
      return True
    else:
      print(movementFailed)
      return False

  def crownedMove(self,x,y):
    if((x==self.posi-1 or x==self.posi+1) and y==self.posj):
      return True
    elif ((y==self.posj-1 or y==self.posj+1) and x==self.posi):
      return True
  
  def hasObstacles(self,table,x,y):
    """revisa si hay otras piezas en el camino devuelve True si hay obstaculos"""
    if (self.posi<x):
      if(self.posj<y):
        for i in range (1,abs(x-self.posi)):
          if(not table.isFree(self.posi+i,self.posj+i)):
            print(movementFailed)
            return True
      else:
        for i in range (1,abs(x-self.posi)):
          if(not table.isFree(self.posi+i,self.posj-i)):
            print(movementFailed)
            return True
    else:
      if(self.posj<y):
        for i in range (1,abs(x-self.posi)):
          if(not table.isFree(self.posi-i,self.posj+i)):
            print(movementFailed)
            return True
      else:
        for i in range (1,abs(x-self.posi)):
          if(not table.isFree(self.posi-i,self.posj-i)):
            print(movementFailed)
            return True
    return False

  
class Tower:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  autoCorunable=False
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '*Tv'
      else:
        return '*T^'
    else:
      if(self.white):
        return ' Tv'
      else:
        return ' T^'
  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
    
    if(self.crown):
      return self.crownedMove(x,y)
    
    if((x)%8==self.posi%8 or y==self.posj):
      return True
    else:
      print(movementFailed)
      return False
  
  def crownedMove(self,x,y):
    if((x==self.posi-1 or x==self.posi+1) and (y==self.posj+1 or y==self.posj-1)):
      return True
  
  def hasObstacles(self,table,x,y):
    """revisa si hay otras piezas en el camino devuelve True si hay obstaculos"""
    if (self.posi<x):
      for i in range (1,abs(x-self.posi)-1):
        if(not table.isFree(self.posi+i,self.posj)):
          print(movementFailed)
          return True
    elif (self.posi>x):
      for i in range (1,abs(x-self.posi)-1):
        if(not table.isFree(self.posi-i,self.posj)):
          print(movementFailed)
          return True
    elif (self.posj<y):
      for i in range (1,abs(y-self.posj)-1):
        if(not table.isFree(self.posj+i,self.posj)):
          print(movementFailed)
          return True
    elif (self.posj>y):
      for i in range (1,abs(x-self.posi)-1):
        if(not table.isFree(self.posj-i,self.posj)):
          print(movementFailed)
          return True
    return False


class Lancer:
  posi=0
  posj=0
  white=None
  crown=False
  isCorunable=True
  autoCorunable=True
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white
  
  def __str__(self):
    if(self.crown):
      if(self.white):
        return '*Lv'
      else:
        return '*L^'
    else:
      if(self.white):
        return ' Lv'
      else:
        return ' L^'
  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
    if(self.crown):
      return self.crownedMove(x,y)
    else:
      if(self.white):
        if(y==self.posj and x>self.posi):
          return True
        else:
          print(movementFailed)
          return False
      else:
        if(y==self.posj and x<self.posi):
          return True
        else:
          print(movementFailed)
          return False
  
  def crownedMove(self,x,y):
    """movimientos posibles una vez coronado"""
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
      print(movementFailed)
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
      print(movementFailed)
      return False
  
  def hasObstacles(self,table,x,y):
    """revisa si hay otras piezas en el camino devuelve True si hay obstaculos"""
    if(self.posi<x):
      for i in range (1,abs(x-self.posi)-1):
        if(not table.isFree(self.posi+i,self.posj)):
          print(movementFailed)
          return True
    else:
      for i in range (1,abs(x-self.posi)-1):
        if(not table.isFree(self.posi-i,self.posj)):
          print(movementFailed)
          return True
    return False
    
    
class King:
  posi=0
  posj=0
  white=None
  crown=True
  isCorunable=False
  autoCorunable=False
  canBeCorunated=False
  
  def __init__(self, posi,posj,white):
    self.posi=posi
    self.posj=posj
    self.white=white

  def __str__(self):
    if(self.white):
      return ' Kv'
    else:
      return ' K^'
  
  def refreshMove(self,xNew,yNew):
    """actualiza la posicion de la pieza"""
    self.posi=xNew
    self.posj=yNew

  def isPossible(self,x,y):
    """ revisa si es posible efectuar el movimiento"""
    if(x==self.posi-1):
      if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
        return True
    elif(x==self.posi+1):
      if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
        return True
    elif(x==self.posi):
      if(y==self.posj-1 or y==self.posj+1):
        return True
    print(movementFailed)
    return False

  def hasObstacles(self,table,x,y):
    return False
