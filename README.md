# Adversarial Search
Artificial Intelligence Assignment 3
Rules of the games are as follows:
1. The game consists of a board of length N.

2. Each block on the board may contain a black
coin, white coin or be empty. Initially, the
board need not be empty.
3. Each player can place a coin only on an empty
block.
4. Player 1 always uses black coin and Player 2
always uses white coin. Player 1 and Player 2
moves alternatively. Player 1 always moves first.
5. Whenever a player places a coin on a block and
adjacent blocks are not empty. Then all the black
coins in continuity becomes white coins and all
the white coins in continuity becomes black
coins.
6. Terminal state is when there is no empty block
on the board.
7. The utility of Player 1 is the number of black
coins on the board in terminal state. The utlity
of Player 2 is the number of white coins in the
terminal state.

Input
Your program should read input as a string
"0000W00BBW0"
0 - empty
W - white coin
B - black coin

Output
Output the utility of Player 1 (Player MAX) using
mini-max algorithm.
