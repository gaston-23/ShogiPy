from piezas import Tablero


def recMov(table,first,player):
  flag=True
  while flag:
    s=input()
    if(s=='I' and first):
      s=invoke(table,player)
      if(s==True):
        flag=False
      else:
        print("Please, try again")
    else:
      s=s.split(" ")
      if(len(s)==2):
        if(type(s[0])==str and type(s[1])==str and s[0]!="" and s[1]!="" and int(s[0])<9 and int(s[1])<9):
          flag=False
          s[0]=int(s[0])
          s[1]=int(s[1])
          return s
      print("Please, try again")
  return s

def selectPiece(table,player):
  if(player=="White"):
    grave=table.graveyardW
  else:
    grave=table.graveyardB
  auxDic={i:str(grave[i]) for i in range(len(grave))}
  print(grave)
  print(auxDic)
  flag=True
  while flag:
    
    print("Select a piece to invoke or -1 to Cancel:")
    x=int(input())
    print(x in auxDic)
    print(x)
    print(grave)
    print(grave[x])
    if(x==-1):
      return None
    if(x in auxDic):
      flag=False
      return grave[x]



def invoke(table,player):
  if(player=="White" and len(table.graveyardW)==0 ):
    print("You don't have pieces to invoke")
    return False
  elif(player=="Black" and len(table.graveyardB)==0 ):
    print("You don't have pieces to invoke")
    return False
  print("select the piece ")
  piece=selectPiece(table,player)
  if(piece!=None):
    print("select where the ",str(piece)," is going to be put")
    x=recMov(table,False,player)
    while not table.isFree(x[0],x[1]):
      print("select an empty space where the ",str(piece)," is going to be put")
      x=recMov(table,False,player)
    print(piece)
    return(table.insert(piece,x[0],x[1],player))
      
  else:
    return None


def main():
  q= Tablero()
  player="White"
  i=0
  active=True

  win=False
  while(active):
    print("===========White (v)===========\n")
    print("Captured: ")
    print(q.printGraveyard(True))
    print("\n")
    print(q)
    print("Captured: ")
    print(q.printGraveyard(False))
    print("\n")
    print("===========Black (^)===========\n")
    

    print("Turn #",i,player)

    print("Move from (row  col) or type 'I' to invoke a captured piece")
    mOld=recMov(q,True,player)

    if(mOld!=True):
      print("Move to (row col)")
      mNew=recMov(q,False,player)
      if(q.move(mOld[0],mOld[1],mNew[0],mNew[1],player)):
        if(player=="White"):
          player="Black"
        
        else:
          player="White"
          i+=1
    else:
      if(player=="White"):
        player="Black"
      else:
        player="White"
        i+=1

  if(win):
    #si alguien gana
    active=False    
  print("Juego Finalizado")

main()