# ShogiPy
shogi game at the system console

piezas.py
has a different class for each kind of piece
has a class for handle the table
    class table:
    has a matrix which contains the pieces
    has a "graveyard" which contains the captured pieces

autocoronation feature:
    

Note:the players aren't an object like the pieces, they are just a string

pending changes:
  +fix the bug with the bishop
  +control when someone wins
  \\incorporate dead pieces to the table (added)
  fix -1 index in table 
  
pending test:
  -bishop moves
  -obstacles
  -invoking