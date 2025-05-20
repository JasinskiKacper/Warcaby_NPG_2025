class Piece:
    def __init__(self, color, king = False):
        self.color = color 
        self.king = king

    def __str__(self):
        return self.color.upper() if self.king else self.color