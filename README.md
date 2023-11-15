# TicTacToe_PythonConsoleApp

Player can choose one of 3 available gamemodes.
Easy or hard mode against computer and pvp mode.
* In pvp mode players take turns making moves until one of them win or there is no place on board (draw).
* In easy mode computer takes random possible move.
* In hard mode computer first checks if there's a winning move available for the computer ('O').
  * If there is, it chooses that move to win the game.
  * If there's no winning move, it looks for available corners on the board and chooses one randomly. Corners are considered advantageous positions in Tic Tac Toe.
  * If there are no available corners, the code checks if the center position (position 5) is available. If it is, the computer chooses that position.
  * If none of the above conditions are met, the code selects an available edge position randomly. Edges are the remaining positions on the board.
