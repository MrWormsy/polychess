# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:35:35 2018

@author: MrWormsy
"""

from ModeJoueurContreJoueur import ModeJoueurContreJoueur

def main():
    
    if(input("Mode joueur vs joueur (1) ou Mode joueur vs AI (2) : ") == "1"):
        modeJcJ = ModeJoueurContreJoueur()
        modeJcJ.commencerPartie()
    else:
        
    
if __name__ == "__main__":
    main()  