Create a class called SteamUser. Upon initialization it should receive username (string) and games (list). 
It should also have an attribute called played_hours (0 by default). Add three methods to the class:
-	play(game, hours)
o	If the game is in the game list, increase the played_hours by the given hours and return "{username} is playing {game}"
o	Otherwise, return "{game} is not in library"
-	buy_game(game)
o	If the game is not in the game list, add it and return "{username} bought {game}"
o	Otherwise return "{game} is already in your library"
-	status() - returns the following:
    "{username} has {games_count} games. Total play time: {played_hours}"
Submit only the class in the judge system.

