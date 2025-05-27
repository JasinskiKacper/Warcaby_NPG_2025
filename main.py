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
            for col in ra   nge(8):
                if (row + col) % 2 == 1:
                    self.board[row][col] = Piece('w')

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["#EEE", "#444"]
        for r in range(8):
            for c in range(8):
                x1, y1 = c * 80, r * 80
                x2, y2 = x1 + 80, y1 + 80
                self.canvas.create_rectangle(x1, y1, x2, y2, fill = colors[(r + c) % 2])
                piece = self.board[r][c]

    def in_bounds(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8


    def get_all_valid_moves(self):
        moves = {}
        if self.must_continue_capture and self.capture_origin:
            captures = self.get_captures(*self.capture_origin)
