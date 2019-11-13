# ShogiPy
shogi game at the system console

piezas.py
has a different class for each kind of piece
has a class for handle the table
  class table:
    has a matrix which contains the pieces
    has a "graveyard" which contains the captured pieces

autocoronation feature:
  when some piece arrives to the promotion zone, the game ask to the user if he want to promote his piece (crowning), if the user answer Yes (y/Y), the game transforms the piece, if user answer No (N/n), the game continue and when the user reach the last possible row, the game crown automatically the piece, if the piece can move without restriction has an attribute named autoCoronate which is false and the game avoid to crown by itself, also each piece has an attribute named canBeCorounated which allows the user to crown a piece without being in the promotion zone

invoke feature:
  when some player capture a piece, the game allows to the user invoke like it were his own, allowing to put where the user wants, and if that place belongs to a promotion zone, the game ask him for crowning

checkmate feature:
  coming soon



Note:the players aren't an object like the pieces, they are just a string

pending changes:
  \\fix the bug with the bishop
  +control when someone wins
  \\incorporate dead pieces to the table (added)
  +fix -1 index in table 
  +add control with pawns (there can't be 2 in same col)

pending test:
  \\bishop moves
  \\obstacles
  -invoking