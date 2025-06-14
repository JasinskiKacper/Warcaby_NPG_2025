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
            while True:
                mr, mc = fr + dr * step, fc + dc * step
                if self.in_bounds(mr, mc) and self.board[mr][mc]:
                    self.board[mr][mc] = None
                    break
                step += 1

        if (piece.color == 'w' and tr == 0) or (piece.color == 'b' and tr == 7):
            piece.king = True

        if was_capture and self.get_captures(tr, tc):
            self.must_continue_capture = True
            self.capture_origin = (tr, tc)
        else:
            self.must_continue_capture = False
            self.capture_origin = None
    
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

      
    def get_moves(self, r, c):
        piece = self.board[r][c]
        moves = []
        if not piece:
            return moves
            
        if piece.king:
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dr, dc in directions:
                step = 1
                while True:
                    nr, nc = r + dr * step, c + dc * step
                    if not self.in_bounds(nr, nc):
                        break
                    if self.board[nr][nc] is None:
                        moves.append((nr, nc))
                    else:
                        break
                    step += 1
        else:
            dr = -1 if piece.color == 'w' else 1
            for dc in [-1, 1]:
                nr, nc = r + dr, c + dc
                if self.in_bounds(nr, nc) and self.board[nr][nc] is None:
                    moves.append((nr, nc))
        return moves
    
    
    def get_captures(self, r, c):
        piece = self.board[r][c]
        captures = []
        if not piece:
            return captures
        directions =[(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            if piece.king:
                step = 1
                enemy_found = False
                while True:
                    nr, nc = r + dr * step, c + dc * step
                    if not self.in_bounds(nr, nc):
                        break
                    target = self.board[nr][nc]
                    if target is None:
                        if enemy_found:
                            captures.append((nr, nc))
                        step += 1
                    elif target.color != piece.color and not enemy_found:
                        enemy_found = True
                        step += 1
                    else:
                        break
            else:
                forward = -1 if piece.color == 'w' else 1
                if dr == forward:
                    mr, mc = r + dr, c + dc
                    nr, nc = r + 2 * dr, c + 2 * dc
                    if self.in_bounds(nr, nc):
                        enemy = self.board[mr][mc]
                        if enemy and enemy.color != piece.color and self.board[nr][nc] is None:
                            captures.append((nr, nc))
            return captures

