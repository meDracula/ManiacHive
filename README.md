# ManiacHive
Is a unique game from a underappreciated genre bot programming game.
The points of this genre and so follows this game is that you the player.
Build your own programming bot whom will play for you.
Every game in this genre present a speciall solution and remolding of 
some algorithm and this game follows in their fot step.
But to simplify **Figure it out, Code it, run it, then be victorious!**

## Maniac Hive
Maniac Hive is a Turned based programming bot game. 
Where the two player write their own bots in the programming language python.
The bots then compete against one another by captuering the overmajority domain 
of the playing field. This is achived by moving their queen to a square and by
doing so the square have been captured and add to queen territory.

### Game mechanics
The game is played by moving the queen to new squares which is captured and 
will be indicated by your queens color. The map also have workers living one the 
and these workers can be captuered by the queen and become apart of her hive.

* Worker will do nothing until they have been captured by a queen.
  Then the worker can be controlled and manuverde around the map. 
  Lastly a worker will block the other hive queen from moving
  too the same square as the worker is currently on.

* Queen can move around the map. And each square it lands on it captures. The queen 
  can not be in the same square as a worker or queen from a different hive. If the 
  queen places herself on a squre where a uncaptuered worker is placed. That worker 
  will join the queens hive.

* The game is won when 65% of the map is captuered by a queen. 

###Lets play
In order to play there is a directory/folder called script there is a file called:
- _playerTemplelet.py_
This file contains a structure of *inputs* and *print* which much be followed inorder
to play. It is recommended to copy this file and make your own **!**
You launches the game by the python inpreter through command: 
`$: python main.py`
Once runnig you can select any file from the _script/_ directory but note that the game 
will only run files with .py extensions.
Then select a file with .py for your opponent. Now watch your incredible work come to
life. Then win or improve it. And recursion through these steps.

# Inspiration
* Video game: [Interloper](http://interlopergame.com/) 
* Programming games: [Halite](https://halite.io/), [>_Terminal](https://terminal.c1games.com/)

