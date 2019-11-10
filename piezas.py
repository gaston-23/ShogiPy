class tablero:
  table=[9][9]
  
  def __init__(self):
    for i in self.table:
      for j in self.table[i]:
        self.table[i][j]=" "
  def isfree(self,posi,posj):
    #TODO if theres is a ficha
    if(self.table[posi][posj]==" "):
      return True
    else:
      return False
  
class goldenGral:
  posi=0
  posj=0
  
  def __init__(self, posi,posj):
    self.posi=posi
    self.posj=posj

  def isPosible(self,x,y):
    #añadir del otro lado del tablero
    if(x==self.posi-1):
      if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
        return True
    elif(x==self.posi+1):
      if(y==self.posj-1 or y==self.posj+1):
        return True
    elif(x==self.posi):
      if(y==self.posj-1 or y==self.posj+1):
        return True
    print("movimiento no permitido")
    return False

class pawn:
  posi=0
  posj=0
  
  def __init__(self, posi,posj):
    self.posi=posi
    self.posj=posj
  
  def isPosible(self,x):
    if(x==self.posi-1):
      return True
    else:
      print("movimiento no permitido")
      return False

class silverGral:
  posi=0
  posj=0
  
  def __init__(self, posi,posj):
    self.posi=posi
    self.posj=posj
  
  def isPosible(self,x,y):
    #añadir del otro lado del tablero
    if(x==self.posi-1):
      if(y==self.posj-1 or y==self.posj+1 or y==self.posj):
        return True
    elif(x==self.posi+1):
      if(y==self.posj-1 or y==self.posj+1):
        return True
    print("movimiento no permitido")
    return False

class horse:
  posi=0
  posj=0
  
  def __init__(self, posi,posj):
    self.posi=posi
    self.posj=posj
  
  def isPosible(self,x,y):
    if(x==self.posi-2 and (y==self.posj-1 or y==self.posj+1 )):
      return True
    else:
      print("movimiento no permitido")
      return False

class bishop:
  posActual=0
  
  def __init__(self, pos):
    self.posActual=pos
  
  def isPosible(self,x):
    if(x==self.posActual-9 or x==self.posActual-10 or x==self.posActual-8 or x==self.posActual-1 or x==self.posActual+1 or self.posActual+9):
      return True
    else:
      print("movimiento no permitido")
      return False
