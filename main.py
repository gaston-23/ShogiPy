from piezas import *


q= tablero()

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
