from piezas import *


def recMov():
  flag=True
  while flag:
    s=input()
    s=s.split(" ")
    if(len(s)==2):
      if(type(s[0])==str and type(s[1])==str and s[0]!="" and s[1]!=""):
        flag=False
  return s


q= tablero()
x=0
player="White"
i=0
active=True

'''
print(q)

print(q.table[2][3].isPossible(5,3))
print(q.graveyardW)
q.move(2,3,3,3)
q.move(3,3,4,3)
print(q)
print(q.graveyardW)


q.move(4,3,5,3)
q.move(5,3,6,3)
q.move(6,3,7,3)
q.move(7,3,8,3)

print(q)
print(q.graveyardW)

q.move(8,3,9,3)
print(q)
q.move(8,3,8,4)
print(q)
'''
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
  print("Move from (row  col)")
  mOld=recMov()
  print("Move to (row col)")
  mNew=recMov()
  if(q.move(int(mOld[0]),int(mOld[1]),int(mNew[0]),int(mNew[1]),player)):
    if(player=="White"):
      player="Black"
     
    else:
      player="White"
      i+=1

if(win):
  #si alguien gana
  active=False

  

  
print("Juego Finalizado")