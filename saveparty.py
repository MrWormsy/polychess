import chess
import chess.pgn


class SaveGame:
    """
    this class is used to save a party in PGN format
    
    """
    def __init__(self,board):
         """
         constructor 
         """
         self.game=chess.pgn.Game() #PGN format
         self.board=board
         
    def save_game(self):
        """
        register a game with pgn format in txt fill
        """
        game_pgn = open("gamesave.txt","w",encoding="utf-8")
        register = chess.pgn.FileExporter(game_pgn)
        self.game.accept(register)
        game_pgn.close()
        
# ===================
# Tests
# ===================
        
if __name__ == "__main__":
    
    board = chess.Board()
    a="a2a4"
    b=chess.Move.from_uci(a)
    board.push(b)
    gam = SaveGame(board)
    print("Affichage PGN :")
    print(gam.game)
    gam.save_game()

        