import chess
import chess.pgn


class saveParty:
    """
    this class is used to save a party in PGN format
    
    """
    def __init__(self,board):
         """
         constructor 
         """
         self.game=chess.pgn.Game() #PGN format
         self.board=board