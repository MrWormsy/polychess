# PolyChess

Tous les codes présent ici permettent de jouer une partie d'échec soit contre l'ordinateur soit contre un autre joueur.
Les étapes permettant de réaliser ceci seront détaillé ci dessous.
Pour permettre de jouer il faut dans tous les cas compiler le fichier polychees et polyglot.
 

### Polychess et Polyglot 

Polychess montre comment la classe chess peut être utilisé, comment réaliser un mouvement par exemple. Polyglot permet de calculer le meilleur coups possible selon des données recensées d'un grand nombre de partie (bookfish).
 
#Contribuors 
* MARTIN ROSA Antonin (Leader)
* DELAGE Lucile (Mascotte)
* PETIT David
* COMBRIÉ Loïck


#Main.py

Pour lancer une partie il faut compiler : 
* polychess.py
* polyglot.py
* ModeJoueurContreJoueur.py
* ModeJoueurContreOrdinateur.py
* ModeOrdinateurContreOrdinateur.py
* AlphaBeta.py 
* MinMax.py
* Main.py (en dernier)
 
Main.py est le fichier permettant l'initialisation de la partie et donc le choix du mode de jeu

###ModeJoueurContreJoueur 

Ce fichier gère une partie d'échec entre deux joeurs. 

##IA

Étant donnée toutes les possibilités d'une partie d'échec, tous ne sont par répertoriés dans bookfish.bin. Il peut alors arriver que la fonction polyglot ne puisse pas retourner de meilleurs coup possible. Il fautut alors utiliser une autre méthode  : 
les fonctions AlphaBeta.py et MinMax.py ont pour role de trouver un bon coup (peut être pas le meilleur).

###ModeJoueurContreOrdiateur

Ce fichier gère une partie d'échec contre l'ordinateur. Les coups jouer par l'ordiateur sont déterminer 
par polyglot ou par AlphaBeta.py

###ModeOrdinateurContreOrdinateur 

Ce fichier gère une partie d'échec entre deux IA. 

