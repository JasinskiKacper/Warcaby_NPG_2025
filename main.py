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

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["#EEE", "#444"]
        for r in range(8):
            for c in range(8):
                x1, y1 = c * 80, r * 80
                x2, y2 = x1 + 80, y1 + 80
                self.canvas.create_rectangle(x1, y1, x2, y2, fill = colors[(r + c) % 2])
                piece = self.board[r][c]
                if piece:
                    fill = "white" if piece.color == 'w' else "black"
                    outline = "gold" if piece.king else "gray"
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill=fill, outline=outline, width=3)
                    if piece.king:
                        self.canvas.create_text(x1 + 40, y1 + 40, text="K", fill="red", font=("Arial", 24, "bold"))
        if self.selected:
            sr, sc = self.selected
            self.canvas.create_rectangle(sc * 80, sr * 80, sc * 80 + 80, sr * 80 + 80, outline="blue", width=3)
            for (mr, mc) in self.valid_moves.get((sr, sc), []):
                self.canvas.create_oval(mc * 80 + 30, mr * 80 + 30, mc * 80 + 50, mr * 80 + 50, fill="green")

    def click(self, event):
        r, c = event.y // 80, event.x // 80
        if self.selected:
            if (r, c) in self.valid_moves.get(self.selected, []):
                self.make_move(self.selected[0], self.selected[1], r, c)
                if self.must_continue_capture:
                    self.selected = (r, c)
                    self.valid_moves = {self.selected: self.get_captures(r, c)}
                else:
                    self.selected = None
                    self.turn = 'b' if self.turn == 'w' else 'w'
                    self.valid_moves = self.get_all_valid_moves()
                    self.capture_origin = None
            else:
                self.selected = None
        else:
            piece = self.board[r][c]
            if piece and piece.color == self.turn:
                if self.must_continue_capture and (r, c) != self.capture_origin:
                    return
                self.valid_moves = self.get_all_valid_moves()
                if (r, c) in self.valid_moves:
                    self.selected = (r, c)
        self.draw_board()
    
    def in_bounds(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def make_move(self, fr, fc, tr, tc):
        piece = self.board[fr][fc]
        self.board[tr][tc] = piece
        self.board[fr][fc] = None

        was_capture = abs(tr - fr) > 1

        if was_capture:
            dr = (tr - fr) // abs(tr - fr)
            dc = (tc - fc) // abs(tc - fc)
            step = 1
    
    def get_all_valid_moves(self):
        moves = {}
        if self.must_continue_capture and self.capture_origin:
            captures = self.get_captures(*self.capture_origin)
            if captures:
                moves[self.capture_origin] = captures
            return moves
            
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]        
                if piece and piece.color == self.turn:
                    captures = self.get_captures(r, c)
                    normal = self.get_moves(r, c)
                    moves[(r, c)] = captures + normal

        return {k: v for k, v in moves.items() if v}
