import tkinter as tk

class Piece:
    def __init__(self, color, king = False):
        self.color = color 
        self.king = king

class CheckersGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Warcaby")
        self.canvas = tk.Canvas(root, width = 640, height = 640)
        self.canvas.pack()
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.turn = 'w'
        self.selected = None
        self.valid_moves = {}
        self.must_continue_capture = False
        self.capture_origin = None
        self.init_board()
        self.canvas.bind("<Button-1>", self.click)
        self.draw_board()

    def init_board(self):
        for row in range(2):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Piece('b')
        for row in range(6, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Piece('w')
