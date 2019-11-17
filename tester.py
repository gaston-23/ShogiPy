from piezas import Tablero,Tower,SilverGen,GoldenGen,King,Horse,Bishop,Pawn,Lancer
from main import recMov,selectPiece

def testmovesPawn(x,y):
  t=Tablero()

  print(t)
  for i in range(x,y):
    for j in range(9):
      t.move(i,j,i+1,j,"White")
      t.move(8-i,8-j,7-i,8-j,"Black")
      print(t)
  t.move(6,5,7,5,"White")
  print(t)
  t.move(7,5,8,6,"White")
  print(t)
  t.move(8,6,7,6,"White")
  print(t)
  t.move(7,6,7,7,"White")
  print(t)
  t.move(7,7,7,6,"White")
  print(t)
  t.move(7,6,8,5,"White")
  print(t)
  t.move(2,4,1,4,"Black")
  print(t)
  t.move(1,4,1,3,"Black")
  print(t)
  t.move(1,3,1,4,"Black")
  print(t)
  t.move(1,4,0,3,"Black")
  print(t)
  t.move(0,3,1,3,"Black")
  print(t)
  t.move(1,3,0,4,"Black")
  print(t)

def silver(t,i,j,player):
  x=i+1
  y=j
  t.move(i,j,x,y,player)
  print(t)
  print(i,j,x,y)
  i=x
  j=y
  x=i+1
  y=j+1
  t.move(i,j,x,y,player)
  print(t)
  print(i,j,x,y)
  i=x
  j=y
  x=i-1
  y=j
  t.move(i,j,x,y,player)
  print(t)
  print(i,j,x,y)
  i=x
  j=y
  x=i+1
  y=j-1
  t.move(i,j,x,y,player)
  print(t)
  print(i,j,x,y)
  i=x
  j=y
  x=i
  y=j-1
  t.move(i,j,x,y,player)
  print(t)
  print(i,j,x,y)
  i=x
  j=y
  x=i
  y=j+1
  t.move(i,j,x,y,player)
  print(t)
  print(i,j,x,y)

def testMovesHorse():
  t=Tablero()
  print(t)
  testmovesPawn(2,5)
  t.move(0,1,2,0,"White")
  print(t)
  t.move(2,0,4,1,"White")
  print(t)
  t.move(4,1,6,0,"White")
  print(t)
  
  silver(t,6,0,"White")

def testMovesBishop():
  t=Tablero()
  print(t)
  testmovesPawn(2,5)
  for i in range(1,8):
    t.move(i,i,i+1,i+1,"White")
    print(t)
    print(i,i,i+1,i+1)

  t.move(1,7,7,1,"White")
  print(t)
  t.move(7,1,0,8,"White")
  print(t)
  player="White"
  while(True):
    print("Move from (row  col) or type 'I' to invoke a captured piece")
    mOld=recMov(t,True,player)

    if(mOld!=True):
      print("Move to (row col)")
      mNew=recMov(t,False,player)
      if(t.move(mOld[0],mOld[1],mNew[0],mNew[1],player)):
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
    print(t)



#testmovesPawn(2,6)
#testMovesHorse()
testMovesBishop()