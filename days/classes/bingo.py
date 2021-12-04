class Bingo:
    def __init__(self, board):
        self.board = board
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.matches = [[False] * self.width for _ in range(self.height)]
        self.last_numb = 0

    def number_check(self, numb):
        self.last_numb = numb
        for x in range(self.width):
            for k in range(self.height):
                if self.board[x][k] == numb:
                    self.matches[x][k] = True

    def win_condition(self):
        return (any(all(row) for row in self.matches) or
                any(all(col) for col in zip(*self.matches)))

    def score(self):
        score = 0
        for x in range(self.width):
            for k in range(self.height):
                if not self.matches[x][k]:
                    score += int(self.board[x][k])
        return score